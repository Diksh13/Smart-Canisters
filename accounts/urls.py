from django.urls import path
# from dashboard import *
from accounts import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('login-success', views.LoginPage.as_view()),
    path('login',views.RegisterPage.as_view()),
    # path('dashboard/)
    # path('display',views.displayempPage.as_view()),

]
