from django.views import View
from django.shortcuts import render,redirect,HttpResponseRedirect
from item_card.models import Item_card,Order,Customer

class Cart(View):
    def get(self,request):
        cart = request.session.get('cart')
        products = []
        if cart:
            for id in cart:
                products.append(Item_card.objects.filter(id=id)[0])
        else:
            massage = 'No Products here...'
            return render(request, 'cart_page.html',{'products':products, 'massage':massage})

        return render(request, 'cart_page.html',{'products':products})

    def post(self,request):
        cart = request.session.get('cart')
        print(cart)
        product = request.POST.get('product')
        print(type(product))
        print(product)
        print(type(cart.get(product)))
        if request.POST.get('increment') == 'increment':
            cart[product] = cart.get(product) + 1
            print('@'*8)
        if request.POST.get('decrement') == 'decrement':
            cart[product] = cart.get(product) - 1
            print('#'*8)
        if request.POST.get('remove') == 'Remove':
            del cart[product]
            print('$'*8)
        request.session['cart'] = cart
        return redirect('cart_page')
 
# orders page coding
 
class Check_out(View):
    def get(self,request):
        return render(request, 'checkOut.html')

    def post(self,request):
        name = request.POST.get('Name')
        address = request.POST.get('Address')
        phone_nu = request.POST.get('phone_number')
        customer_id = request.session.get('customer_id')
        cart = request.session.get('cart')
        #fetching model objects
        customer = Customer.objects.all().filter(id=customer_id)[0]
        product = Item_card.objects.all()
        for i in cart.keys():
            # print(customer)
            # print(product.filter(id=i)[0])
            # print(product.filter(id=i)[0].price)
            # print(str(i))
            print('---'*4)
            obj = Order(customer=customer,
                  product=product.filter(id=i)[0],
                  product_price=product.filter(id=i)[0].price,
                  product_quantity=cart.get(str(i)),
            )
            obj.save()

        request.session['cart'] = {}
        return redirect('homePage')
