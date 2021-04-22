from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('user/', views.DashboardPage.as_view()),
    # path('display',views.displayempPage.as_view()),

]
