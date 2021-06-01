from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from dashboard import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^(?P<pk>\d+)/$',views.AddressPage.as_view(),name='user_dashboard'),
    url(r'^EditAddress/(?P<pk>\d+)/$',views.EditAddressPage.as_view(),name='dashboard_edit_address'),
    url(r'^user/(?P<pk>\d+)/$',views.UpdateAddress.as_view(),name='update_address'),
    url(r'^customer-details/(?P<pk>\d+)/$',views.AssociatedUsers.as_view(),name='customer-details'),
    url(r'^canister-details/(?P<pk>\d+)/$',views.AssociatedCanisters.as_view(),name='canister-details'),
    url(r'^grocery-details/(?P<pk>\d+)/$',views.Grocery.as_view(),name='grocery-details'),
    url(r'^profile/(?P<pk>\d+)/$',views.Profile.as_view(),name='profile'),
    url(r'^user-profile/(?P<pk>\d+)/$',views.UpdateProfile.as_view(),name='update_profile'),
    url(r'^vendor-details/(?P<pk>\d+)/$',views.VendorProfile.as_view(),name='vendor-details'),
    # url(r'^(?P<pk>\d+)/$',views.DashboardPage.as_view(),name='menu-dashboard'),
    url(r'^(?P<pk>\d+)/$',views.DashboardPage.as_view(),name='dashboard'),
    

    
    
    # path('display',views.displayempPage.as_view()),

]
