from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth import hashers 
from django.views import View 

from item_card.models import *

class Login(View):
    request_url = None
    def get(self,request):
        Login.request_url = request.GET.get('request_url')
        print(Login.request_url)
        return render(request, 'login.html')

    def post(self,request):
        error_massege = None
        
        email = request.POST.get('email')
        password = request.POST.get('password')
        # login form validation 
        
        if not email:
            error_massege = "Put Email"
        elif not password:
            error_massege = "Input Password"
        else:
            customer = Customer.get_Customor_date_by_email(email)
            
        # Cheking Database Email is correct or not    
            if customer:
                customer = customer[0]
                customer_password = customer.password
                
                if hashers.check_password(password, customer_password):
                    #login successfull
                    request.session['customer_id'] = customer.id
                    request.session['customer_email'] = customer.email
                    if Login.request_url:
                        return HttpResponseRedirect(Login.request_url)
                    else:
                        return redirect('homePage')
                else:
                    error_massege = "Invailid Email or Password"
            else:
                error_massege = "Invailid Email or Password"
            
        return render(request, 'login.html',{'error_massege' : error_massege})


def logOut(request):
    request.session.clear()
    return redirect('homePage')




