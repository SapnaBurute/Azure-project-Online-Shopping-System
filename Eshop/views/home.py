from django.shortcuts import render,redirect
from django.contrib.auth import hashers 
from django.views import View 

from item_card.models import *

class HomePage(View):
    def get(self,request):
        data = None
        category_id = None
        if request.method == 'GET':
            category_id = request.GET.get('category_id')
            if category_id != None:
                data = Item_card.objects.all().filter(img_category=category_id)
                category_id = int(category_id)
            else: 
                data = Item_card.objects.all()

        fields = Category.objects.all()
        print(request.session.get('customer_id'))
        print(request.session.get('customer_email'))
        
        return render(request, 'home_page.html', {'data':data,'category_id':category_id ,'fields' : fields })

    def post(self,request):
        increment = request.POST.get('increment_cart')
        decrement = request.POST.get('decrement_cart')
        print(increment)
        print(decrement)

        if request.POST.get('poduct'):
            return redirect('homePage')

        cart = None
        cart = request.session.get('cart')
        # Decrementing number of product in cart
        remove = request.POST.get('remove')
        product = request.POST.get('product_id')
        print(product)
        if increment:
            product = increment
        
        if cart:
            if product in cart.keys():
                if decrement:
                    cart[str(product)] = cart.get(product) - 1
                if increment :
                    cart[product] = 1 + cart.get(product)
            else:
                cart[product] = 1
        
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        print('-'*40)
        return redirect('homePage')




