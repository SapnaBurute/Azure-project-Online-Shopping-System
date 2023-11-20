from django.shortcuts import render
from django.views import View
from  item_card.models import Order



class Your_Order(View):
    def get(self, request):
        customer_id = request.session.get('customer_id')
        orders = Order.objects.filter(customer=customer_id)
        
        return render(request, 'orders_page.html', {'orders':orders})





