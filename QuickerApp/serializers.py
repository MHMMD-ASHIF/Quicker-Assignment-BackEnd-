from rest_framework import serializers
from . models import ShopList, User
from rest_framework_simplejwt.tokens import RefreshToken, TokenError







class ShopListSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShopList
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    global email,phoneNumber
    password = serializers.CharField(max_length=65, min_length=8,
                                     write_only=True)
    email = serializers.EmailField(max_length=255)
    first_name = serializers.CharField(max_length=255)
    phoneNumber = serializers.CharField(max_length=100)


    class Meta:

        model = User
        fields = ['email','first_name','phoneNumber', 'password','tokens']

    def validate(self, attrs):
        email = attrs.get('email', '')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'email', ('Email is already in use')})
        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=65, min_length=8, write_only=True)
    email = serializers.EmailField()
    tokens = serializers.SerializerMethodField()

    def get_tokens(self, obj):
        user = User.objects.get(email=obj['email'])

        return {
            'refresh': user.tokens()['refresh'],
            'access': user.tokens()['access']
        }
 

    class Meta:
        model = User
        fields = [ 'email','password', 'tokens']







class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_message = {
        'bad_token': ('Token is expired or invalid')
    }

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):

        try:
            RefreshToken(self.token).blacklist()

        except TokenError:
            self.fail('bad_token')
