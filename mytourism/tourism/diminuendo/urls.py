from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('index/',views.index, name = 'index'),
    path('home/',views.home, name = 'home'),
    path('about/',views.about_us, name = 'about_us'),
    path('', auth_views.LoginView.as_view(template_name = 'login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'logout.html'), name='logout'),
    #this route is for buying items
    path('index/<int:product_id>', views.product_details, name='product_details'),
    #handling the receipt after a successful sale
    path('bookings/',views.bookings, name='bookings'),
    path('receipt/<int:receipt_id>',views.receipt_detail,name= 'receipt_detail'),

]