from django.urls import path
from DeliveryBoy import views
app_name="DeliveryBoy"

urlpatterns = [
        path('deliveryhome/',views.deliveryhome,name='deliveryhome'),
        path('logout/',views.logout,name='logout'),
        path('editprofile/',views.editprofile,name='editprofile'),
        path('myprofile/',views.myprofile,name='myprofile'),
        path('changepassword/',views.changepassword,name='changepassword'),
         path('complaint/',views.complaint,name='complaint'),
       path('delcomplaint<int:id>/',views.delcomplaint,name='delcomplaint'),
       path('viewbooking/',views.viewbooking,name='viewbooking'),
         path("bookingstatus/<int:id>/<int:sts>", views.bookingstatus,name="bookingstatus"),
         path('myorders/',views.myorders,name='myorders'),

]


