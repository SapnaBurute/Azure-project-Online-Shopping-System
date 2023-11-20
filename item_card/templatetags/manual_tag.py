from django import template
from Eshop.views.cart import Cart
from item_card.models import Item_card,Customer

register = template.Library()


@register.filter(name='is_in_cart')
def is_in_cart(product , cart):
    if str(product) in cart.keys():
       return True
    return False



@register.filter(name='cart_quantity')
def cart_quantity(product , cart):
    if str(product) in cart.keys():
       return cart[str(product)]
    
    return None




@register.filter(name='cart_len')
def cart_len(cart):
      if cart != None:
         return len(cart)
      return False



@register.filter(name='get_cart')
def get_cart(id , cart):
   query = Item_card.objects.filter(id=id)
   return query[0]


@register.filter(name='total')
def total(product, cart):
   return product.price * cart_quantity(product.id, cart)


@register.filter(name='grand_total')
def grand_total(product,cart):
   sum = 0
   for product in product:
      sum = sum + total(product, cart)
   return sum


@register.filter(name='name_by_id')
def name_by_id(customer_id):
   costomer = Customer.objects.all().filter(id=customer_id)[0]
   return costomer.first_name +' '+ costomer.last_name



