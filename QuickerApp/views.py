from django.views.decorators.csrf import csrf_exempt
from . models import ShopList
from . serializers import ShopListSerializer, UserSerializer, LogoutSerializer,LoginSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from django.core.files.storage import default_storage
from rest_framework.generics import GenericAPIView
from rest_framework import status, generics, permissions
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib import auth
from rest_framework_simplejwt.authentication import JWTAuthentication
from oauth2_provider.contrib.rest_framework import OAuth2Authentication






class ShopListView(APIView):
    authentication_classes = [OAuth2Authentication,JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]


    def post(self, request):

            serializer = ShopListSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)

    def get(self, request,format=None):
        shops = ShopList.objects.all()
        serializer = ShopListSerializer(shops, many=True)
        return Response(serializer.data)
    

  


class ShopListModify(APIView):
    def get(self, request, **kwargs):
        ids = kwargs.get("shop_id")
        shop = ShopList.objects.get(id=ids)
        serializer = ShopListSerializer(shop)
        return Response(serializer.data)

    def put(self, request, **kwargs):
        ids = kwargs.get("shop_id")
        shop = ShopList.objects.get(id=ids)
        serializer = ShopListSerializer(instance=shop, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, **kwargs):
        ids = kwargs.get('shop_id')
        shop = ShopList.objects.get(id=ids)
        shop.delete()
        return Response({'msg': 'Data Deleted'})


@csrf_exempt
def save(request):
    file = request.FILES['uploadedFile']
    file_name = default_storage.save(file.name, file)

    return JsonResponse(file_name, safe=False)


class RegisterAPIView(GenericAPIView):

    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print()
        return Response(serializer, status=status.HTTP_400_BAD_REQUEST)





class LoginView(APIView):

    serializer_class = LoginSerializer
    success = 0

    def post(self, request, format=None):
        data = request.data
        email = data.get('email', '')
        password = data.get('password', '')

        user = auth.authenticate(email=email, password=password)
        

        if user:
            success = 1
            # auth_token = jwt.encode(
            #     {'email': user.email}, settings.JWT_SECRET_KEY, algorithm="HS256")

            serializer = UserSerializer(user)

            # data={
            #     'user':serializer.data,'token':auth_token,'success':success
            # }
            data = {
                'user': serializer.data, 'success': success
            }
            return Response(data,
                            status=status.HTTP_200_OK)
        else:
            success = 0
            return Response('User name Error')

        return Response({'detail': 'Invalid credentials'},
                        status=status.HTTP_401_UNAUTHORIZED)


class LogoutAPIView(GenericAPIView):
    serializer_class = LogoutSerializer

    permission_classes = [IsAuthenticated]

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_204_NO_CONTENT)
