from django.shortcuts import render,redirect
from DeliveryBoy.models import *
from Guest.models import*
from User.models import*

# Create your views here.

def deliveryhome(request):
    return render(request,'DeliveryBoy/Deliveryhome.html')

def logout(request):
     del request.session["deid"]
     return redirect('Guest:index')

def myprofile(request):
    if 'deid' in request.session:
         delivery=tbl_delivery.objects.get(id=request.session['deid'])
         return render(request, 'DeliveryBoy/Myprofile.html',{ 'delivery':delivery})
    else:
          return redirect('Guest:Login')



def editprofile(request):
    if 'deid' in request.session:
        delivery = tbl_delivery.objects.get(id=request.session['deid'])
        if request.method == "POST":
            delivery.delivery_name = request.POST.get("txtname")
            delivery.delivery_email = request.POST.get("txtemail")
            delivery.delivery_contact = request.POST.get("txtcontact")
            delivery.delivery_address = request.POST.get("address")
            
            if 'txtphoto' in request.FILES:
                delivery.delivery_photo = request.FILES['txtphoto']
            
            delivery.save()
            return redirect("DeliveryBoy:myprofile")
        else:
            return render(request, 'DeliveryBoy/EditProfile.html', {'delivery': delivery})
    else:
        return redirect('Guest:Login')

     
def changepassword(request):
     if 'deid' in request.session:
           npassword=request.POST.get('txtpass')
           rpassword=request.POST.get('txtpassword')
           opassword=request.POST.get('txtpwd')
           delivery=tbl_delivery.objects.get(id=request.session['deid'])
           if request.method=="POST":
               if delivery.delivery_password == opassword:
                    if npassword==rpassword:
                         delivery.delivery_password=request.POST.get("txtpass")
                         delivery.save()
                         return redirect("DeliveryBoy:myprofile ")
                    else:
                         return render(request,'DeliveryBoy/ChangePassword.html',{"msg":"Error in Confirm password"})
               else:
                    return render(request,'DeliveryBoy/ChangePassword.html',{"msg":"Error in Old password"})
           else:
                    return render(request,'DeliveryBoy/ChangePassword.html')
     else:
          return redirect('Guest:Login') 

def complaint(request):
     if 'deid' in request.session:
          complaint=tbl_complaint.objects.filter(delivery=request.session['deid'])
          if request.method=="POST":
               tbl_complaint.objects.create(delivery=tbl_delivery.objects.get(id=request.session['deid']),
                                       complaint_title=request.POST.get("titile"),
                                       complaint_description=request.POST.get("content"))
               return redirect("DeliveryBoy:complaint") 
          else:
               return render(request,'DeliveryBoy/Complaint.html',{"complaint":complaint}) 
     else:
          return redirect('Guest:Login')   
     
def delcomplaint(request,id):
     tbl_complaint.objects.get(id=id).delete()
     return redirect("DeliveryBoy:complaint") 

def viewbooking(request):
     delivery = tbl_delivery.objects.get(id=request.session["deid"])
     book = tbl_booking.objects.filter(booking_status=2,tbl_cart__cart_status=4,user__place=delivery.place.id)
     return render(request,"DeliveryBoy/ViewBooking.html",{"book":book})

def bookingstatus(request,id,sts):
     cart=tbl_cart.objects.get(id=id)
     book = tbl_booking.objects.get(id=cart.booking.id)
     if book.deliveryboy == None:
          book.deliveryboy = tbl_delivery.objects.get(id=request.session["deid"])
          book.save()
     cart.cart_status=sts
     cart.save()
     return redirect("DeliveryBoy:deliveryhome")

def myorders(request):
     delivery = tbl_delivery.objects.get(id=request.session["deid"])
     book = tbl_booking.objects.filter(booking_status=2,tbl_cart__cart_status__gt=4,user__place=delivery.place.id,deliveryboy=request.session["deid"])
     return render(request,"DeliveryBoy/Myorder.html",{"book":book})