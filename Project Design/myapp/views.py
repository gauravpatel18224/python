from django.shortcuts import render,redirect
from .models import User,Product,Wishlist,Cart
import requests
import random

# Create your views here.
def index(request):
	try:
		user=User.objects.get(email=request.session['email'])
		if user.usertype=="buyer":
			return render(request,'index.html')
		else:
			return render(request,'seller-index.html')
	except:
		return render(request,'index.html')			

def seller_index(request):
	return render(request,'seller-index.html')	

def about(request):
	return render(request,'about.html')

def shop(request):
	products= Product.objects.all()
	return render(request,'shop.html',{'products':products})

def contact(request):
	return render(request,'contact.html')

def signup(request):
	if request.method=="POST":
		try:
			user=User.objects.get(email=request.POST['email'])
			msg="Email Already Registered"
			return render(request,'login.html',{'msg':msg})	
		except:
			if request.POST['password']==request.POST['cpassword']:
				User.objects.create(
						fname=request.POST['fname'],
						lname=request.POST['fname'],
						email=request.POST['email'],
						mobile=request.POST['mobile'],
						address=request.POST['address'],
						password=request.POST['password'],
						profile_picture=request.FILES['profile_picture'],
						usertype=request.POST['usertype'],	
						
				    )
				msg="User Signup Successfully"
				return render(request,'login.html',{'msg':msg})
			else:
				msg="Password & Confirm Password Dose Not Matched"
				return render(request,'login.html',{'msg':msg})
	else:
		return render(request,'signup.html')

def login(request):
	if request.method=="POST":
		try:
			user=User.objects.get(email=request.POST['email'])
			if user.password==request.POST['password']:
				request.session['email']=user.email
				request.session['fname']=user.fname
				request.session['profile_picture']=user.profile_picture.url
				wishlists=Wishlist.objects.filter(user=user)
				request.session['wishlist_count']=len(wishlists)
				carts=Cart.objects.filter(user=user)
				request.session['cart_count']=len(carts)
				if user.usertype=="buyer":
					return render(request,'index.html')
				else:
					return render(request,'seller-index.html')	
			else:
				msg="Incorrect Password"
				return render(request,'login.html',{'msg':msg})
		except:
			msg="Email Not Registered"
			return render(request,'signup.html',{'msg':msg})
	else:
		return render(request,'login.html')					
def logout(request):
	try:
		del request.session['fname']     	
		del request.session['email']
		del request.session['profile_picture']
		del request.session['wishlist_count']
		del request.session['cart_count']
		msg="User Logged Out Successfully"
		return render(request,'login.html',{'msg':msg})
	except:
		msg="User Logged Out Successfully"
		return render(request,'login.html',{'msg':msg})	
def change_password(request):
	user=User.objects.get(email=request.session['email'])
	if request.method=="POST":
		if user.password==request.POST['old_password']:
			if request.POST['new_password']==request.POST['cnew_password']:
				user.password=request.POST['new_password']
				user.save()
				msg="Password Changed Successfully"
				del request.session['email']
				del request.session['fname']
				del request.session['profile_picture']
				return render(request,'login.html',{'msg':msg})
			else:
				msg="New Password & Confirm New Password Dose Not Matched"
				if user.usertype=="buyer":
					return render(request,'change-password.html',{'msg':msg})
				else:
					return render(request,'seller-change-password.html',{'msg':msg})
		else:
			msg="Old Password Dose Not Matched"
			if user.usertype=="buyer":
				return render(request,'change-password.html',{'msg':msg})
			else:
				return render(request,'seller-change-password.html',{'msg':msg})
				
	else:
		if user.usertype=="buyer":
			return render(request,'change-password.html')
		else:
			return render(request,'seller-change-password.html')
				
def forgot_password(request):
	if request.method=="POST":
		try:
			user=User.objects.get(mobile=request.POST['mobile'])
			mobile=str(user.mobile)
			otp=str(random.randint(1000,9999))
			url = "https://www.fast2sms.com/dev/bulkV2"
			querystring = {"authorization":"vXy8Hb7BWQ1sNaqzOwg3dM0oenfT4tAPSpiLJkKlIhVjcURrx9G5OlaHDtAXMb8WQqNpPRKdjcB9TIwZ","variables_values":otp,"route":"otp","numbers":mobile}
			headers = {'cache-control': "no-cache"}
			response = requests.request("GET", url, headers=headers, params=querystring)
			print(response.text)
			request.session['mobile']=user.mobile
			request.session['otp']=otp
			
			return render(request,'otp.html')
		except:
			msg="Mobile Number Not Registered"
			return render(request,'forgot-password.html',{'msg':msg})	

	else:
		return render(request,'forgot-password.html')	

def verify_otp(request):
	otp1=int(request.session['otp'])
	otp2=int(request.POST['otp'])

	if otp1==otp2:
		del request.session['otp']
		return render(request,'new-password.html')
	else:
		msg="Invalid Otp"
		return render(request,'otp.html')	

def new_password(request):
	if request.POST['new_password']==request.POST['cnew_password']:
		user=User.objects.get(mobile=request.session['mobile'])
		user.password=request.POST['new_password']
		user.save()
		del request.session['mobile']
		msg="Password Update Successfully"
		return render(request,'login.html',{'msg':msg})
	else:
		msg="New Password & Confirm New Password Dose Not Matched"
		return render(request,'new-password.html',{'msg':msg})			
def profile(request):
	user=User.objects.get(email=request.session['email'])
	if request.method=="POST":
		user.fname=request.POST['fname']
		user.lname=request.POST['lname']
		user.mobile=request.POST['mobile']
		user.address=request.POST['address']
		try:
			user.profile_picture=request.FILES['profile_picture']
		except:
			pass
		user.save()
		msg="Profile Update Successfully"
		request.session['profile_picture']=user.profile_picture.url
		if user.usertype=="buyer":
			return render(request,'profile.html',{'user':user,'msg':msg})
		else:
			return render(request,'seller-profile.html',{'user':user,'msg':msg})
					
	else:
		if user.usertype=="buyer":
			return render(request,'profile.html',{'user':user})
		else:
			return render(request,'seller-profile.html',{'user':user})
def seller_add_product(request):
	if request.method=="POST":
		seller=User.objects.get(email=request.session['email'])
		Product.objects.create(	
				seller=seller,
				product_category=request.POST['product_category'],
				product_size=request.POST['product_size'],
				product_color=request.POST['product_color'],
				product_name=request.POST['product_name'],
				product_desc=request.POST['product_desc'],
				product_price=request.POST['product_price'],
				product_picture=request.FILES['product_picture'],
			)
		msg="Product Add Successfully"
		return render(request,'seller-add-product.html',{'msg':msg})

	else:
		return render(request,'seller-add-product.html')
def seller_view_product(request):
	seller=User.objects.get(email=request.session['email'])
	products=Product.objects.filter(seller=seller)
	return render(request,'seller-view-product.html',{'products':products})

def seller_product_detail(request,pk):
	wishlist_flag=False
	cart_flag=False
	product=Product.objects.get(pk=pk)
	user=User.objects.get(email=request.session['email'])
	if user.usertype=="buyer":
		try:
			Wishlist.objects.get(user=user,product=product)			
			wishlist_flag=True
		except:
			pass
		try:
			Cart.objects.get(user=user,product=product)			
			cart_flag=True
		except:
			pass		
		return render(request,'product-detail.html',{'product':product,'wishlist_flag':wishlist_flag,'cart_flag':cart_flag})
	else:
		return render(request,'seller-product-detail.html',{'product':product})
			

def seller_product_edit(request,pk):
	product=Product.objects.get(pk=pk)
	if request.method=='POST':
		product.product_name=request.POST['product_name']
		product.product_price=request.POST['product_price']
		product.product_desc=request.POST['product_desc']
		product.product_category=request.POST['product_category']
		product.product_size=request.POST['product_size']
		product.product_color=request.POST['product_color']
		try:
			product.product_picture=request.FILES['product_picture']
		except:
			pass
		product.save()
		msg="Product Update Successfully"
		return render(request,'seller-product-edit.html',{'product':product,'msg':msg})
	else:
		return render(request,'seller-product-edit.html',{'product':product})

def seller_product_delete(request,pk):

	product=Product.objects.get(pk=pk)
	product.delete()
	return redirect('seller-view-product')

def seller_view_product_specific(request,cat):
	user=User()
	products=[]
	if cat=="all":
		products=Product.objects.all()
	else:
		products=Product.objects.filter(product_category=cat)
	try:
		user=User.objects.get(email=request.session['email'])
	except:
		pass
	if user.usertype=="buyer":
		return render(request,'shop.html',{'products':products})
	elif user.usertype=="seller":
		return render(request,'seller-view-product.html',{'products':products})
	else:
		return render(request,'shop.html',{'products':products})

def add_to_wishlist(request,pk):
	product=Product.objects.get(pk=pk)
	user=User.objects.get(email=request.session['email'])
	Wishlist.objects.create(user=user,product=product)
	return redirect('mywishlist')

def mywishlist(request):
	user=User.objects.get(email=request.session['email'])
	wishlists=Wishlist.objects.filter(user=user)
	request.session['wishlist_count']=len(wishlists)
	return render(request,'mywishlist.html',{'wishlists':wishlists})

def remove_from_wishlist(request,pk):
	product=Product.objects.get(pk=pk)
	user=User.objects.get(email=request.session['email'])
	wishlist=Wishlist.objects.get(user=user,product=product)
	wishlist.delete()
	return redirect('mywishlist')

def add_to_cart(request,pk):
	product=Product.objects.get(pk=pk)
	user=User.objects.get(email=request.session['email'])
	Cart.objects.create(
		user=user,
		product=product,
		product_price=product.product_price,
		product_qty=1,
		total_price=product.product_price
	)
	return redirect('mycart')

def mycart(request):
	net_price=0
	user=User.objects.get(email=request.session['email'])
	carts=Cart.objects.filter(user=user)
	for i in carts:
		net_price=net_price+i.total_price
	request.session['cart_count']=len(carts)
	return render(request,'mycart.html',{'carts':carts,'net_price':net_price})

def remove_from_cart(request,pk):
	product=Product.objects.get(pk=pk)
	user=User.objects.get(email=request.session['email'])
	cart=Cart.objects.get(user=user,product=product)
	cart.delete()
	return redirect('mycart')	

def change_qty(request):
	product_qty=int(request.POST['product_qty'])
	pk=int(request.POST['pk'])
	cart=Cart.objects.get(pk=pk)
	cart.product_qty=product_qty
	cart.total_price=cart.product_price*product_qty
	cart.save()
	return redirect('mycart') 

