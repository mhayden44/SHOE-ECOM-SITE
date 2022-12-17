from django.urls import path
from . import views
from .views import SearchView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('shoes/', views.shoes, name='shoes'),
    path('shoes/mens/',views.shoes_mens,name='shoes_mens'),
    path('shoes/mens/athl',views.shoes_mens_athl,name='shoes_mens_athl'),
    path('shoes/mens/drss',views.shoes_mens_drss,name='shoes_mens_drss'),
    path('shoes/mens/work',views.shoes_mens_work,name='shoes_mens_work'),
    path('shoes/mens/casl',views.shoes_mens_casl,name='shoes_mens_casl'),
    path('shoes/womens/',views.shoes_womens,name='shoes_womens'),
    path('shoes/womens/athl',views.shoes_womens_athl,name='shoes_womens_athl'),
    path('shoes/womens/drss',views.shoes_womens_drss,name='shoes_womens_drss'),
    path('shoes/womens/work',views.shoes_womens_work,name='shoes_womens_work'),
    path('shoes/womens/casl',views.shoes_womens_casl,name='shoes_womens_casl'),
    path('home/',views.home,name='home'),
    path('',views.home,name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('cart/', views.cart, name = 'cart'),
    path('updatecart', views.updateCart, name = 'updatecart'),
    path('updatequantity', views.updateQuantity, name = 'updatequantity'),
    path('clearcart', views.clearCart, name = 'clearcart'),
    path('search/', SearchView.as_view(), name='search'),
]