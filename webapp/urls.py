from django.urls import path
from webapp import views
urlpatterns=[
    path('home_page/',views.home_page,name="home_page"),
    path('about_page/',views.about_page,name="about_page"),
    path('contact_page/',views.contact_page,name="contact_page"),
    path('product_page/<cat_name>',views.product_page,name="product_page"),
    path('single_pro/<int:dataid>/',views.single_pro,name="single_pro"),


    path('sign_page/',views.sign_page,name="sign_page"),
    path('registration_page/',views.registration_page,name="registration_page"),
    path('login_page/',views.login_page,name="login_page"),
    path('UserLogout/',views.UserLogout,name="UserLogout"),


    path('Contact_page/',views.Contact_page,name="Contact_page"),
    path('Contact_save/',views.Contact_save,name="Contact_save"),
    path('card_page/',views.card_page,name="card_page"),
    path('savecart_page/',views.savecart_page,name="savecart_page"),
    path('delete_cart/<int:cartid>/',views.delete_cart,name="delete_cart"),
    path('checkout_page/',views.checkout_page,name="checkout_page"),
    path('save_checkout/',views.save_checkout,name="save_checkout"),








]