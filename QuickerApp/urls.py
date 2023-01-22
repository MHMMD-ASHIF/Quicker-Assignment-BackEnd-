from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [

    path('post/', views.ShopListView.as_view()),
    path('post/<int:shop_id>', views.ShopListModify.as_view()),
    path('saveFile/', views.save),
    path('register', views.RegisterAPIView.as_view()),
    path('login', views.LoginView.as_view()),
    path('logout', views.LogoutAPIView.as_view()),




]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
