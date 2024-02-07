from django.urls import path
from myapp import views

urlpatterns=[
    path('new_page/',views.new_page,name="new_page"),
    path('phone_register/',views.phone_register,name="phone_register"),
    path('add_page/',views.add_page,name="add_page"),
    path('display_page/',views.display_page,name="display_page"),
    path('cat_edit/<int:dataid>/',views.cat_edit,name="cat_edit"),
    path('update_dtls/<int:dataid>/',views.update_dtls,name="update_dtls"),
    path('delt_cat/<int:dataid>/',views.delt_cat,name="delt_cat"),



    path('Add_prdct/',views.Add_prdct,name="Add_prdct"),
    path('save_product/',views.save_product,name="save_product"),
    path('disp_product/',views.disp_product,name="disp_product"),
    path('edit_product/<int:productid>/',views.edit_product,name="edit_product"),
    path('update_product/<int:productid>/',views.update_product,name="update_product"),
    path('delete_product/<int:productid>/',views.delete_product,name="delete_product"),
    path('',views.Admin_login,name="Admin_login"),
    path('admin_loginpage/',views.admin_loginpage,name="admin_loginpage"),


    path('disp_contact/',views.disp_contact,name="disp_contact"),
    path('delete_page/<int:contactid>/',views.delete_page,name="delete_page"),
]