from django.shortcuts import render, redirect
from  django.http import HttpResponse
from .models import *
from .forms import CreateUserForm, OrderForm, ContactForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users,admin_only
from django.contrib.auth.models import Group
from django.http import JsonResponse
import json
from django.forms import inlineformset_factory
from .filters import ProductFilter

from django.core.mail import EmailMessage
from django.conf import settings



@unauthenticated_user
def registerPage(request):
	
	form=CreateUserForm()
	if request.method == "POST":
		form=CreateUserForm(request.POST)
		if form.is_valid():
			user=form.save()
			username= form.cleaned_data.get('username')
			email=form.cleaned_data.get('email')
			phone=form.cleaned_data.get('phone')
			country=form.cleaned_data.get('country')
			city=form.cleaned_data.get('city')
			street=form.cleaned_data.get('street')

			group = Group.objects.get(name='customer')
			user.groups.add(group)
			Customer.objects.create(
				user=user,
				name=user.username,
				phone=phone,
				country=country,
				email=email,
				city=city,
				street=street
				)

			messages.success(request,"Account Was Created For "+ username)

			email=EmailMessage(
			"Welcome "+username ,
			"You are successfully registered to SHOOT. If you havent resistered and it is a unauthenticated_user  "+
			"vist http://127.0.0.1:8000/login/?next=/ and reset your password.",
			settings.EMAIL_HOST_USER,
			[email]
			)
			email.fail_silently=False
			email.send()
			return redirect('login')




	context={'form':form}
	return render(request,'shoes/register.html',context)

@unauthenticated_user
def loginPage(request):

	if request.method== "POST":
		username=request.POST.get('username')
		password=request.POST.get('password')
		user =authenticate(request,username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request,"Username/Password Incorrect")

	context={}
	return render(request,'shoes/login.html',context)

def logoutUser(request):
	logout(request)
	return redirect('login')



def home(request):
	product=Product.objects.all()
	contact=Contact.objects.filter(positive=True)
	
	context={'product': product,'contact':contact}
	return render(request,'shoes/home.html',context)

def products(request):
	product=Product.objects.all()
	myFilter= ProductFilter(request.GET, queryset=product)
	product=myFilter.qs
	
	context={'product': product,'myFilter':myFilter}
	return render(request,'shoes/products.html',context)

def about(request):
	return render(request,'shoes/AboutUs.html')
def contact(request):
	form=ContactForm()

	if request.method=="POST":
		print("hello")
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
		else:
			print("invalide")

	context={'form':form}
	return render(request,'shoes/contact.html',context)

@allowed_users(allowed_roles=['admin'])
def customer(request,pk):
	customer = Customer.objects.get(id=pk)
	orders = customer.order_set.all()
	Products=Product.objects.all()
	order_count = orders.count()
	context={
		'Products':Products,
		'customer':customer ,
		'orders':orders,
		'order_count':order_count
	}

	return render(request,'shoes/customer.html',context)

@allowed_users(allowed_roles=['admin'])
def ourmessages(request):
	messages=Contact.objects.all()
	context={'messages':messages}
	return render(request,'shoes/messages.html',context)



@allowed_users(allowed_roles=['admin'])
@login_required(login_url='login')
def details(request):
	orders=Order.objects.filter(complete=True)
	orderItem=OrderItem.objects.filter(order__in=orders)
	
	customers=Customer.objects.all()
	product=Product.objects.all()
	total_orders = orders.count()
	delivered = orders.filter(status='Delivered').count()
	pending = orders.filter(status='Pending').count()

	context = {'orders':orders, 'customers':customers,
	'total_orders':total_orders,'delivered':delivered,
	'pending':pending ,'orderItem':orderItem,'product':product}
	return render(request,'shoes/details.html',context)


def product_details(request,pk):
	items=Product.objects.all()
	current_product=Product.objects.get(id=pk)
	img1=current_product.product_img1
	img2=current_product.product_img2
	img3=current_product.product_img3
	img4=current_product.product_img4
	company=current_product.company
	name=current_product.name
	price=current_product.price
	description=current_product.description
	

		
	context={'current_product': current_product,
		'img1':img1,
		'img2':img2,
		'img3':img3,
		'img4':img4,
		'name':name,
		'price':price,
		'description':description,
		'company':company,
		'items':items,
	
		}
	if request.method=='post':
		orderItem=OrderItem.objects.create(product=product)
		orderItem.save()
	return render(request,'shoes/product-details.html',context)




@allowed_users(allowed_roles=['admin'])
def updateOrder(request, pk):
	order=Order.objects.get(id=pk)
	orderitem=OrderItem.objects.get(order=order)
	form=OrderForm(instance=orderitem)
	if request.method=="POST":
		form = OrderForm(request.POST, instance=orderitem)
		if form.is_valid():
			form.save()
			return redirect('/details/')
	context={'form':form}
	return render(request,'shoes/order_form.html',context)

@allowed_users(allowed_roles=['admin'])
def deleteOrder(request,pk):
	order=Order.objects.get(id=pk)
	if request.method =="POST":
		order.delete()
		return redirect('/details')
	context={'item': order}
	return render(request,'shoes/delete.html', context)


@allowed_users(allowed_roles=['admin'])
def customerOrder(request,pk):

	customer = Customer.objects.get(id=pk)
	
	form = OrderForm(initial={'customer':customer})
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = OrderForm(request.POST)
		
		if form.is_valid():
			form.save()
			return redirect('/details/')

	context={'form':form}
	return render(request,'shoes/order_form.html',context)

	
def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	quant=data['quant']
	quant=int(quant)
	size=data['size']
	print('size:',size)
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)
	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product,size=size)
	if action == 'add':
		print('working')
		orderItem.quantity = (orderItem.quantity + quant)
		print('added')
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)
	orderItem.save()
	
	if orderItem.quantity <= 0:
		orderItem.delete()
	return JsonResponse('Item was added', safe=False) 


def remove(request,pk):
	orderItem=OrderItem.objects.get(id=pk)
	if request.method =="POST":
		orderItem.delete()

		return redirect('/Mycart/')
	context={'item': orderItem}
	return render(request,'shoes/remove.html', context)

def cart(request):
	if request.user.is_authenticated:
		customer=request.user.customer
		order,created=Order.objects.get_or_create(customer=customer, complete=False)
		items=order.orderitem_set.all()
		email=customer.email
		username=customer.name
		
		if request.method== "POST":
			order=Order.objects.get(customer=customer, complete=False)
			order.complete=True
			order.save()
			# email=EmailMessage(
			# "Dear "+username ,
			# "Your order is successfully placed. You might reseive the product with in a week.For more information feel free to contact us. "+
			# "vist http://127.0.0.1:8000/contactus/ ",
			# settings.EMAIL_HOST_USER,
			# [email]
			# )
			# email.fail_silently=False
			# email.send()
			return redirect('home')


	else:

		items=[]
		order={'get_cart_total':0,'get_cart_total_with_Tax':0,'get_cart_Tax':0}


	context={'items':items,'order':order}
	return render(request,'shoes/cart.html',context)


