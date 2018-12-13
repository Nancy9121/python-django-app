from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('register/',views.user_register,name="register"),
    path('user_details/',views.user_details,name="user_details"),
    path('user_edit/<pk>',views.user_edit,name="user_edit"),
   	path('user_delete/<pk>',views.user_delete,name="user_delete"),
    path('crop_register/',views.crop_register,name="crop_register"),
	path('crop_details/',views.crop_details,name="crop_details"),   
	path('crop_edit/<pk>',views.crop_edit,name="crop_edit"),
	path('crop_delete/<pk>',views.crop_delete,name="crop_delete"),
	path('crop_calculator/',views.crop_calculator,name="crop_calculator"),
    path('crop_search/',views.crop_search,name="crop_search"),
    path('change_password/<pk>',views.change_password,name="change_password"),
    path('forgot_password',views.forgot_password,name="forgot_password"),
]