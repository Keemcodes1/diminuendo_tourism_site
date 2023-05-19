from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Product,Sale
from .filters import Product_filters
#we now include our filters from the filters side
#we are going to first include the models to be used here
# Create your views here.
#including our models form created in the forms file
from .forms import AddForm,SaleForm
def index(requests):
    products = Product.objects.all().order_by('-id')
    product_filters = Product_filters(requests.GET,queryset= products)
    products = product_filters.qs
    return render(requests,'index.html',{'products': products,'product_filters': product_filters})


@login_required
def about_us(requests):
    return render(requests,'about_us.html')

@login_required
def LoginView(requests):
    return render(requests,'login.html')

def home(requests):
    return render(requests,'base.html')

def LogoutView(requests):
    return render(requests,'logout.html')

#def SignUp(requests):
    #return render(requests,'main.html')


#creating a view for product_detail
@login_required
def product_details(requests,product_id):
    product = Product.objects.get(id = product_id)
    return render(requests,'product_details.html',{'product':product})

     
#this handles receipt
@login_required
def bookings(requests):
    sales = Sale.objects.all().order_by('-id')
    return render(requests, 'bookings.html', {'sales':sales})


#receipt details
@login_required
def receipt_detail(requests, receipt_id):
    receipt = Sale.objects.get(id = receipt_id)
    return render(requests, 'receipt_detail.html',{'receipt':receipt})
                                                                
                                



    

