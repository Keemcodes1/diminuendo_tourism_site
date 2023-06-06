from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('index/',views.index, name = 'index'),
    path('home/',views.home, name = 'home'),
    path('portfolio/',views.portfolio, name = 'portfolio'),
    path('index/<int:product_id>', views.product_details, name='product_details'),
    #handling the receipt after a successful sale
    path('bookings/',views.bookings, name='bookings'),
    path('receipt/<int:receipt_id>',views.receipt_detail,name= 'receipt_detail'),
    path('book/',views.book_now, name= 'book_now'),
    path('services/',views.services, name='services'),
    path('contactus/',views.contactus, name='contactus'),

]