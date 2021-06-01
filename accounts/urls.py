from django.urls import path
from django.conf.urls import url
from accounts import views

urlpatterns = [
    path('', views.IndexPage.as_view(),name='logout'),
    url(r'^login/$',views.LoginPage.as_view(),name='login-success'),
    url(r'^login$',views.RegisterPage.as_view(),name='register-login'),
    

]
