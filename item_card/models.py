from django.db import models
import datetime

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Item_card(models.Model):
    img_title = models.CharField(max_length=100)
    img_desc = models.CharField(max_length=100)
    price = models.FloatField(null=True, default=200)
    img_category = models.ForeignKey(Category, on_delete= models.CASCADE, default=5)
    img_img = models.ImageField(upload_to='uploads/',null=True, default=None)

    def __str__(self):
        return self.img_title




class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_num = models.CharField(max_length=14)
    email     = models.EmailField()
    image  =  models.ImageField(upload_to='customers/' , null=True, default='')
    address = models.CharField(max_length=100,null=True , default='')
    password  = models.CharField(max_length=500)

    def __str__(self):
        value = str(self.first_name)+' '+str(self.last_name)               
        return value

    @staticmethod
    def get_Customor_date_by_email(email):
        return Customer.objects.filter(email=email)



 
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Item_card, on_delete=models.CASCADE)
    product_price = models.FloatField()
    product_quantity = models.IntegerField()
    date = models.DateField(default=datetime.datetime.today)
    # address = models.CharField(100)
    # phone_nu = models.CharField(15)





