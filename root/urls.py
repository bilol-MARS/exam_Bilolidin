"""
URL configuration for root project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from apps.views import homepage
from apps.views import about
from apps.views import products
from apps.views import whyus
from apps.views import testimonial, SavatchaView, UserCreateView, UserLogoutView, UserSigninView, ShoppingCartCreateView, contactview
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='homepage'),
    path('about/', about, name='about'),
    path('products/', products, name='products'),
    path('whyus/', whyus, name='whyus'),
    path('testimonial/',testimonial, name='testimonial'),
    path('api/admin',homepage),
    path('savat/', SavatchaView.as_view(), name='savatcha'),
    path('signup/', UserCreateView.as_view(), name='user_create'),
    path('singin/', UserSigninView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('like/<int:pk>/', ShoppingCartCreateView.as_view(), name='like'),
    path('contact/', contactview, name='contact'),
   

]



urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
