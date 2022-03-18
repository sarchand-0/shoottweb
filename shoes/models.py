from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	country = models.CharField(max_length=200, null=True)
	city = models.CharField(max_length=200, null=True)
	street = models.CharField(max_length=200, null=True)
	def __str__(self):
		return self.name

class Product(models.Model):

	name = models.CharField(max_length=200, null=True)
	id=models.IntegerField(primary_key=True)
	product_img1 = models.ImageField(default="product.png", null=True, blank=True)
	product_img2 = models.ImageField(default="product.png", null=True, blank=True)
	product_img3 = models.ImageField(default="product.png", null=True, blank=True)
	product_img4 = models.ImageField(default="product.png", null=True, blank=True)
	company=models.CharField(max_length=200, blank=True , null=True)
	price = models.FloatField(null=True)
	description = models.CharField(max_length=200, null=True, blank=True ,default="Fresh")
	feedback= models.CharField(max_length=200, null=True, blank=True )

	def __str__(self):
		return self.name
	@property
	def imageURL(self):
		try:
			url = self.product_img1.url
		except:
			url = ''
		return url

class Order(models.Model):
	STATUS = (
			('Pending', 'Pending'),
			('Out for delivery', 'Out for delivery'),
			('Delivered', 'Delivered'),
			)
	
	customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS, default= 'Pending')
	complete=models.BooleanField(default=False)

	def __str__(self):
		return str(self.id)

	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total
	@property
	def get_cart_total_with_Tax(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		total+=total*0.13
		return total 
	@property
	def get_cart_Tax(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		total =total*0.13
		return total 

	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total 

class OrderItem(models.Model):
	SIZE = (
			('US7', 'US7'),
			('US7.5', 'US7.5'),
			('US8', 'US8'),
			('US8.5', 'US8.5'),
			('US9', 'US9'),
			('US9.5', 'US9.5'),
			('US10', 'US10'),
			('US10.5', 'US10.5'),
			) 
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	product = models.ForeignKey(Product, null=True, on_delete= models.SET_NULL)
	quantity=models.IntegerField(default=0)
	size = models.CharField(max_length=200, default='US8',choices=SIZE)

	def __str__(self):
		return self.product.name

	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total

class Contact(models.Model):
	
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	message = models.CharField(max_length=200, null=True)
	positive=models.BooleanField(default=False)
	def __str__(self):
		return self.name

