from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from dashboard import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^(?P<pk>\d+)/$',views.AddressPage.as_view(),name='user_dashboard'),
    url(r'^EditAddress/(?P<pk>\d+)/$',views.EditAddressPage.as_view(),name='dashboard_edit_address'),
    url(r'^user/(?P<pk>\d+)/$',views.UpdateAddress.as_view(),name='update_address'),
    url(r'^details/(?P<pk>\d+)/$',views.AssociatedUsers.as_view(),name='table-details'),
    
    
    # path('display',views.displayempPage.as_view()),

]
