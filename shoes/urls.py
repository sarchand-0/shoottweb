from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns=[
	path('',views.home, name="home"),
	path('products/',views.products, name="products"),
	path('customer/<str:pk>/',views.customer, name="customer"),
	path('details/',views.details,name="details"),
	path('aboutus/',views.about,name="about"),
	path('contactus/',views.contact,name="contact"),
	path('messages/',views.ourmessages,name="messages"),

	path('product_details/<str:pk>/',views.product_details, name="product_details"),
	path('Mycart/', views.cart, name="cart"),


	
	path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
	path('delete/<str:pk>/', views.deleteOrder, name="delete_order"),
	path('create_order/<str:pk>', views.customerOrder, name="customer_order"),

	path('register/',views.registerPage, name="register"),
	path('login/',views.loginPage, name="login"),
	path('loginout/',views.logoutUser, name="logout"),

	path('update_item/',views.updateItem, name="update_item"),
	path('remove_item/<str:pk>/', views.remove, name="remove_item"),


	path('reset_password/',
    auth_views.PasswordResetView.as_view(template_name="shoes/password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="shoes/password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="shoes/password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="shoes/password_reset_done.html"), 
        name="password_reset_complete"),

]