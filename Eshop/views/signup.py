from django.shortcuts import render,redirect
from django.contrib.auth import hashers 
from django.views import View 
from item_card.models import Customer
from django.core.mail import send_mail

# Chek sign Up page is valid or not
def isValid_password(password):
    return (len(password)>=8 and (not password.isupper()) and (not password.islower()) and not password.isnumeric() and not password.isalpha())


def isValid(first_name,last_name,phone_num,email,password):
        error_massege = None
        if not first_name:
            error_massege = 'Input first Name required'
        elif not last_name:
            error_massege = 'Input Last Name required'
        elif not phone_num:
            error_massege = 'Input Phone Number required'
        elif not email:
            error_massege = 'input email required'
        elif not password:
            error_massege = 'Enter Your passWord required'
        elif not isValid_password(password) :
                error_massege = 'Please Enter strong at least 8 character must contains upper,lower case and number'
        return error_massege

class SignUp(View):
    def get(self,request):
        return render(request, 'signUp.html')
    
    error_massege = ''
    def post(self,request):
        form_data = request.POST
        first_name = form_data.get('first_name')
        last_name = form_data.get('last_name')
        phone_num = form_data.get('phone_number')
        email = form_data.get('email')
        password = form_data.get('password')
        
        error_massege = isValid(first_name, last_name, phone_num, email, password)
        if error_massege :
            error_massege = error_massege   
        else:    
            if Customer.objects.filter(email=email):
                error_massege = 'Emai already exists, Use another email'
            else:
                password_encod = hashers.make_password(password)
                cus_exist = Customer.objects.get_or_create(first_name=first_name,last_name=last_name,phone_num=phone_num,email=email,password=password_encod)
                customer = Customer.objects.filter(email=email)[0] 
                request.session['customer_id'] = customer.id
                request.session['email'] = customer.email
                #sending mail
                send_mail( 'Eshop Sign up',
                            f'You have created new acc on Eshop portal.\n Email = {customer.email} \n password = {password}', 
                            'work.swapnaliburute@gmail.com', 
                            [email,])

                return redirect('homePage')

        return render(request, 'signUp.html',{'error_massege':error_massege})

