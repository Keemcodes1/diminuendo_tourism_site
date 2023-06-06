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



def portfolio(requests):
    
    return render(requests,'portfolio.html')


def home(requests):
    return render(requests,'home.html')



#def SignUp(requests):
    #return render(requests,'main.html')


#creating a view for product_detail
def product_details(requests,product_id):
    product = Product.objects.get(id = product_id)
    return render(requests,'product_details.html',{'product':product})

     
#this handles receipt
def bookings(requests):
    sales = Sale.objects.all().order_by('-id')
    return render(requests, 'bookings.html', {'sales':sales})


#receipt details

def receipt_detail(requests, receipt_id):
    receipt = Sale.objects.get(id = receipt_id)
    return render(requests, 'receipt_detail.html',{'receipt':receipt})

def book_now(requests,):
    
    return render(requests,'book_now.html')

def services(requests,):
    
    return render(requests,'services.html')  
def contactus(requests):
    return render(requests,'contactus.html')  
                                                                
                                



    

