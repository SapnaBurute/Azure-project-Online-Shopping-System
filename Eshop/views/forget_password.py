from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth import hashers 
from django.views import View 
import random
from .signup import isValid_password
from item_card.models import *
from django.core.mail import send_mail

class ForgetPassword(View):

    def get(self,request):
        return render(request, 'forget_password/forget_password.html')

    def post(self,request):
        self.email = request.POST.get('email')
        try: 
            self.customer = Customer.objects.get(email=self.email)
        except: 
            self.customer = None

        if self.customer :
           request.session['user_email'] = self.email
           self.OTP = random.randint(100000, 999999)
           print(self.OTP)
           request.session['OTP'] = self.OTP
           # Sending OTP to mail
           send_mail('A2Z shop',
                     f' Forget Password OTP: \n your OTP is {self.OTP} \n please do not share any one',
                     'av321241',
                     [self.email,])

           return redirect('OTP_Verify')
        else:
            error_massege = 'Email Does not exists'
            context = {'error_massege':error_massege}
            return render(request, 'forget_password/forget_password.html',context)
        



class OTPVerify(View):
    def get(self,request):
        print('get')
        return render(request, 'forget_password/OTP_Verify.html')

    def post(self,request):
        error_massege = None

        user_OTP = request.POST.get('OTP')
        server_OTP = str(request.session.get('OTP'))
        # verifing OTP 
        if user_OTP == server_OTP:
            print('otp verified')
            request.session['OTP'] = None
            return redirect('new_password')

        else:
            error_massege = "OTP is Not Correct"

        context = {
            'error_massege' : error_massege
        }    
        return render(request, 'forget_password/OTP_Verify.html', context)




class NewPassword(View):

    def get(self,request):
        if request.session.get('user_email') == None:
            return redirect('login_page')
        return render(request, 'forget_password/new_password.html')


    def post(self,request):
        error_massege = None
        ispasswordUpdated = None

        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        customer_email = request.session.get('user_email')

        #if session is Empty then Redirect to Login page   
        if customer_email == None:
           return redirect('login_page')

        if new_password == confirm_password:
            if isValid_password(new_password):
                customer = Customer.objects.get(email=customer_email)
                customer.password = hashers.make_password(new_password)
                customer.save()
                error_massege = "Password Successfully Updated redirection Login Page"
                ispasswordUpdated = True
                request.session.clear()

                send_mail('Eshop Password Updated',
                     f'your Password is {new_password} \n please do not share any one',
                     'av321241',
                     [customer_email,])

            else:
                error_massege = 'Password must contains 8 charecter number,capital & small letters'
        else:
            error_massege = "Password does not matched."
        context = {
            'error_massege':error_massege,
            'ispasswordUpdated' :ispasswordUpdated
        }
        return render(request, 'forget_password/new_password.html', context )




