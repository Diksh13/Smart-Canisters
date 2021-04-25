from django.contrib import admin
from django.urls import path
from dashboard import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('user', views.AddressPage.as_view()),
    # path('display',views.displayempPage.as_view()),

]
