from django.shortcuts import render,redirect
from django.views import View
from item_card.models import Customer
from django.contrib.auth.hashers import check_password,make_password
from .signup import isValid_password



class UserProfile(View):

    
    def get(self, request):
        customer_id = request.session.get('customer_id')
        self.customer = Customer.objects.filter(id=customer_id)[0]
        edit_profile = request.GET.get('edit_profile')
        return render(request, 'user_profile.html', {'customer':self.customer,'edit_profile':edit_profile})

    def post(self,request):
        self.customer = Customer.objects.filter(id=request.session.get('customer_id'))
        if request.POST.get('image'):
            print('**---'*8)
            print(request.FILES)
            if not request.FILES.get('upload_image'):
              return render(request, 'user_profile.html')  
            image = request.FILES.get('upload_image')  
            customer_obj = self.customer[0]
            customer_obj.image = image
            customer_obj.save()
            return redirect('user_profile')
        
        if request.POST.get('update_profile'):
            print('-'*40)
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            phone_number = request.POST.get('phone_number')
            address = request.POST.get('address')
            password = request.POST.get('password')
            if not check_password(password, self.customer[0].password):
                massage = 'You have Entered Wrong Password \n try again '
                return redirect('user_profile')
            else:
                Customer.objects.filter(id=request.session.get('customer_id')).update(
                     first_name=first_name,
                    last_name = last_name,
                    phone_num=phone_number,
                    address=address,
                   
                )
                return redirect('user_profile')
        if request.POST.get('edit_profile'):
            print('*'*8)
            edit_profile = request.POST.get('edit_profile')
            return render(request, 'user_profile.html', {'edit_profile':edit_profile} )




class Change_password(View):
    def get(self, request):
         return render(request,'change_password.html')



    def post(self,request):
        error_massage = None
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        conferm_password = request.POST.get('conferm_password')
        customer_id = request.session.get('customer_id')
        print('-'*30)
        print(customer_id)
        customer = Customer.objects.filter(id=customer_id)
        print(customer)
        
        #cheking old password
        if check_password(old_password,(customer[0].password)) :
            if isValid_password(new_password):
                customer.filter(id=customer_id)
                if new_password == conferm_password :
                    encoded_password = make_password(new_password)
                    customer.update(password=encoded_password)
                else:
                    error_massage = 'Your password Did not match'
            else:
                error_massage = 'Please Enter atleast 8 charater, containing upper ,lower and number'
        else:
            error_massage = 'Your entered, Old password in Wrong'
        return render(request,'change_password.html',{'error_massage':error_massage})

