from datetime import datetime
from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
from Designer.models import *
from User.models import *
from django.db.models import Q

from django.conf import settings
from django.core.mail import send_mail


# Create your views here.



     
def dhomepage(request):
     if 'did' in request.session:
       return render(request, 'Designer/HomePage.html')  
     else:
         return redirect('Guest:Login')

def dprofile(request):
    if 'did' in request.session:
     designer=tbl_designer.objects.get(id=request.session['did'])
     return render(request, 'Designer/DesignerProfile.html',{ 'designer':designer}) 
    else:
         return redirect('Guest:Login')

def designeredit(request):
     if 'did' in request.session:
          designer=tbl_designer.objects.get(id=request.session['did'])
          if request.method == "POST":
               designer.designer_name=request.POST.get("txtname")
               designer.designer_email=request.POST.get("txtemail")
               designer.designer_contact=request.POST.get("txtcontact")
               designer.designer_address=request.POST.get("address")
               designer.save()
               return redirect("Designer:designeredit")
          else:
               return render(request, 'Designer/DesignerEdit.html',{'designer':designer})
     else:
         return redirect('Guest:Login')
          
def changeDpassword(request):
     if 'did' in request.session:
          npassword=request.POST.get('txtpass')
          rpassword=request.POST.get('txtpassword')
          opassword=request.POST.get('txtpwd')
          designer=tbl_designer.objects.get(id=request.session['did'])
          if request.method=="POST":
               if designer.designer_password == opassword:
                    if npassword==rpassword:
                         designer.designer_password=request.POST.get("txtpass")
                         designer.save()
                         return redirect("Designer:dprofile")
                    else:
                         return render(request,'Designer/ChangeDesignerPasswrod.html',{"msg":"Error in Confirm password"})
               else:
                    return render(request,'Designer/ChangeDesignerPasswrod.html',{"msg":"Error in Old password"})
          else:
               return render(request,'Designer/ChangeDesignerPasswrod.html') 
     else:
          return redirect('Guest:Login')  
         

def addwork(request):
     if 'did' in request.session:     
          work = tbl_work.objects.all()
          if request.method=="POST":
               tbl_work.objects.create(work_name=request.POST.get("txtname"),
                                        work_details=request.POST.get("Details"),
                                        work_photo=request.FILES.get("txtphoto"),
                                        designer= tbl_designer.objects.get(id= request.session["did"]))
               return redirect("Designer:addwork")
          else:
               return render(request, 'Designer/Work.html',{"work":work})
     else:
          return redirect('Guest:Login')  
     
      
def delwork(request,id):
     tbl_work.objects.get(id=id).delete()
     return redirect('Designer:addwork')

def gallery(request,id):
     gallery=tbl_gallery.objects.filter(work=id)
     if request.method=="POST":
          tbl_gallery.objects.create(gallery_photo=request.FILES.get("txtphoto"),
                                     work = tbl_work.objects.get(id=id))
          return redirect('Designer:gallery',id)
     else:
          return render(request, 'Designer/Gallery.html',{"gallery":gallery})
     
def delgallery(request,id):
     tbl_gallery.objects.get(id=id).delete()
     return redirect('Designer:addwork')     
     
# def viwedesigner(request):
#     designer= tbl_designer.objects.all()
#     return render(request, 'Designer/ViewDesigner.html',{"designer":designer})  
 
# def viewwork(request,did):
#      work=tbl_work.objects.filter(id=did)
#      return render(request, 'Designer/ViewWork.html',{"work":work})

# def viewgallery(request,id):
#      gallery=tbl_gallery.objects.filter(work=id)
#      return render(request, 'Designer/ViewGallery.html',{"gallery":gallery})

def viewrequest(request):
     if 'did' in request.session:     
          viewrequest=tbl_designrequest.objects.all()
          work=tbl_work.objects.all()
          user=tbl_user.objects.all()
          return render(request,'Designer/viewRequest.html',{"request":viewrequest,"work":work,"user":user})
     else:
          return redirect('Guest:Login')  
     

def rejectrequest(request, id):
    # Fetch the design request from the database
    designrequest = tbl_designrequest.objects.get(id=id)
    
    # Update the status of the design request
    designrequest.designrequest_status = 2
    designrequest.save()
    
    # Prepare email content
    user_email = designrequest.user.user_email  # Assuming tbl_user has an email field
    subject = "Your Design Request Has Been Rejected"
    


    message = (
          f"Dear {designrequest.user.user_name},\n\n"  # Assuming tbl_user has a name field
          "We regret to inform you that your design request has been rejected. Below are the details of your request:\n\n"
          f"Request Date: {designrequest.designrequest_date}\n"
          f"Completion Date: {designrequest.designrequest_todate}\n"
          f"Amount: {designrequest.designrequest_amount}\n"
          f"Work Details: {designrequest.work.work_name}\n\n"
          "If you have any questions or need clarification, please feel free to contact us.\n\n"
          "We apologize for any inconvenience caused.\n\n"
          "Best regards,\n"
          "The Design Team"
     )
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [user_email]
    
    # Send the email
    send_mail(subject, message, from_email, recipient_list)
    
    # Redirect to the view request page
    return redirect("Designer:viewrequest")

def acceptrequest(request, id):
    designrequest = tbl_designrequest.objects.get(id=id)
    if request.method=="POST":
     designrequest.designrequest_status = 1
     designrequest.designrequest_amount=request.POST.get("txt_amount")
     designrequest.save()
     
     user_email = designrequest.user.user_email  # Assuming tbl_user has an email field
     subject = "Your Design Request Has Been Accepted"
     message = (
        f"Dear {designrequest.user.user_name},\n\n"  # Assuming tbl_user has a name field
        "We are pleased to inform you that your design request has been accepted. Below are the details of your request:\n\n"
        f"Request Date: {designrequest.designrequest_date}\n"
        f"Completion Date: {designrequest.designrequest_todate}\n"
        f"Amount: {designrequest.designrequest_amount}\n"
        f"Work Details: {designrequest.work.work_name}\n\n"
        "If you have any questions or require further assistance, please do not hesitate to contact us.\n\n"
        "Best regards,\n"
        "The Design Team"
    )
     
     from_email = settings.EMAIL_HOST_USER
     recipient_list = [user_email]
     
     # Send the email
     send_mail(subject, message, from_email, recipient_list)
     
     # Redirect to the view request page
     return redirect("Designer:viewrequest")  
    else:
         return render(request,"Designer/Amount.html")

def complaint(request):
     if 'did' in request.session:
          designercomplaint=tbl_complaint.objects.filter(desginer=request.session['did'])
          if request.method=="POST":
               tbl_complaint.objects.create(complaint_title=request.POST.get("titile"),
               complaint_description=request.POST.get("content"),
               desginer=tbl_designer.objects.get(id=request.session['did']))
               return redirect("Designer:complaint")
          else:
               return render(request,'Designer/Dcomplaint.html',{"designercomplaint":designercomplaint}) 
     else:
          return redirect('Guest:Login')  
        
          
def deldesignercomplaint(request,id):
     tbl_complaint.objects.get(id=id).delete()
     return redirect("Designer:complaint") 

def logout(request):
     del request.session["did"]
     return redirect('Guest:index')    



def chatpage(request,id):
    user  = tbl_user.objects.get(id=id)
    return render(request,"Designer/Chat.html",{"user":user})

def ajaxchat(request):
    from_designer = tbl_designer.objects.get(id=request.session["did"])
    to_user = tbl_user.objects.get(id=request.POST.get("tid"))
    
    tbl_chat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),designer_from=from_designer,user_to=to_user,chat_file=request.FILES.get("file"))
    return render(request,"Designer/Chat.html")

def ajaxchatview(request):
    tid = request.GET.get("tid")
    designer = tbl_designer.objects.get(id=request.session["did"])
    chat_data = tbl_chat.objects.filter((Q(designer_from=designer) | Q(designer_to=designer)) & (Q(user_from=tid) | Q(user_to=tid))).order_by('chat_time')
    return render(request,"Designer/ChatView.html",{"data":chat_data,"tid":int(tid)})

def clearchat(request):
    tbl_chat.objects.filter(Q(designer_from=request.session["did"]) | (Q(user_to=request.GET.get("tid")) )).delete()
    return render(request,"Designer/ClearChat.html",{"msg":"Chat Deleted Sucessfully...."})
