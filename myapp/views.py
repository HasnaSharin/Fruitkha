from django.shortcuts import render,redirect
from myapp.models import categoryDb,productDb,ContactDb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages


# Create your views here.
def new_page(req):
    return render(req,"index.html")
def phone_register(req):
    return render(req,"phonepage.html")
def add_page(req):
    if req.method == "POST":
        na=req.POST.get('cname')
        img=req.FILES['image']
        dis=req.POST.get('dscrptn')
        obj=categoryDb(Name=na,Image=img,Description=dis)
        obj.save()
        messages.success(req,"Category saved successfully..!")
        return redirect(phone_register)
def display_page(req):
    data=categoryDb.objects.all()
    return render(req,"Displaycategory.html",{'data':data})

def cat_edit(req,dataid):
    data=categoryDb.objects.get(id=dataid)
    return render(req,"Editcategory.html",{'data':data})
def update_dtls(req,dataid):
    if req.method == "POST":
        na=req.POST.get('cname')
        dis = req.POST.get('dscrptn')
        try:
            img = req.FILES['image']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=categoryDb.objects.get(id=dataid).Image
        categoryDb.objects.filter(id=dataid).update(Name=na,Description=dis,Image=file)
        return redirect(display_page)
def delt_cat(req,dataid):
    data=categoryDb.objects.filter(id=dataid)
    data.delete()
    return redirect(display_page)


def Add_prdct(req):
    data=categoryDb.objects.all()
    return render(req,"Addproduct.html",{'data':data})


def save_product(req):
    if req.method=="POST":
        catgr=req.POST.get('category')
        pn=req.POST.get('pname')
        pr=req.POST.get('price')
        discr=req.POST.get('description')
        brn=req.POST.get('brand')
        imgg=req.FILES['pimage']
        obj=productDb(Category=catgr,PrdctName=pn,Price=pr,Description=discr,Brand=brn,Productimage=imgg)
        obj.save()
        return redirect(Add_prdct)


def disp_product(req):
    product=productDb.objects.all()
    return render(req,"Displayproduct.html",{'product':product})


def edit_product(req,productid):
    data=categoryDb.objects.all()
    product=productDb.objects.get(id=productid)
    return render(req,"Editproduct.html",{'product':product,'data':data})
def update_product(req,productid):
    if req.method=="POST":
        catgr = req.POST.get('category')
        pn = req.POST.get('pname')
        pr = req.POST.get('price')
        discr = req.POST.get('description')
        brn = req.POST.get('brand')
        try:
            imgg = req.FILES['pimage']
            fs=FileSystemStorage()
            file=fs.save(imgg.name,imgg)
        except MultiValueDictKeyError:
            file=productDb.objects.get(id=productid).Productimage
        productDb.objects.filter(id=productid).update(Category=catgr,PrdctName=pn,Price=pr,Description=discr,Brand=brn,Productimage=file)
        return redirect(disp_product)
def delete_product(req,productid):
    product=productDb.objects.filter(id=productid)
    product.delete()
    return redirect(disp_product)



def Admin_login(request):
    return render(request,"Adminlogin.html")

def admin_loginpage(request):
    if request.method=="POST":
        uname=request.POST.get('username')
        pname=request.POST.get('password')
        if User.objects.filter(username__contains=uname).exists():
            user=authenticate(username=uname,password=pname)

            if user is not None:
                login(request,user)

                request.session['username']=uname
                request.session['password'] = pname
                messages.success(request, "Login Successfully")
                return redirect(new_page)
            else:
                messages.error(request,"invalid username or password")
                return redirect(Admin_login)
        else:
            messages.error(request, "invalid username or password")
            return redirect(Admin_login)


def disp_contact(req):
    contact=ContactDb.objects.all()
    return render(req,"DisplayContact.html",{'contact':contact})
def delete_page(req,contactid):
    contact=ContactDb.objects.filter(id=contactid)
    contact.delete()
    return redirect(disp_contact)



