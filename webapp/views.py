from django.shortcuts import render,redirect
from myapp.models import categoryDb,productDb,ContactDb
from webapp.models import RegistrationDb,CartDb,CheckoutDb
from django.contrib import messages

# Create your views here.
def home_page(req):
    data = categoryDb.objects.all()
    return render(req,"Home.html",{'data':data})

def about_page(req):
    return render(req,"about.html")

def contact_page(req):
    return render(req,"contact.html")
def product_page(req,cat_name):
    data=categoryDb.objects.all()
    pro=productDb.objects.filter(Category=cat_name)

    return render(req,"product.html",{'data':data, 'pro':pro})
def single_pro(req,dataid):
    data = categoryDb.objects.all()

    pro_sing=productDb.objects.get(id=dataid)
    pro=productDb.objects.all()

    return render(req,"Singleproduct.html",{'pro_sing':pro_sing, 'pro':pro,'data':data})

def sign_page(req):
    return render(req,"registrationsignup.html")

def registration_page(request):
    if request.method=="POST":
        RegName=request.POST.get('regname')
        Rprofile=request.FILES['regim']
        Rmail=request.POST.get('regmail')
        Rpswrd=request.POST.get('regpas')

        obj=RegistrationDb(RegName=RegName,Rprofileim=Rprofile,REmail=Rmail,Rpassword=Rpswrd)
        obj.save()
        return redirect(sign_page)
def login_page(request):
    if request.method=="POST":
        RegName = request.POST.get('regname')
        Rpswrd = request.POST.get('regpas')
        request.session['RegName']=RegName
        request.session['Rpassword']=Rpswrd
        messages.success(request,"login succussfully")

        if RegistrationDb.objects.filter(RegName=RegName,Rpassword=Rpswrd).exists():
            return redirect(home_page)
        else:
            messages.error(request, "invalid username or password")
            return redirect(sign_page)
    else:
        messages.error(request, "invalid username or password")
        return redirect(sign_page)
def UserLogout(request):
    del request.session['RegName']
    del request.session['Rpassword']
    return redirect(sign_page)

def Contact_page(req):
    return render(req,"contact.html")

def Contact_save(req):
    if req.method=="POST":
        na=req.POST.get('name')
        em=req.POST.get('email')
        pn=req.POST.get('phone')
        sb=req.POST.get('subject')
        ms=req.POST.get('message')
        obj=ContactDb(ConName=na,ConEmail=em,ConPhone=pn,Subject=sb,Message=ms)
        obj.save()
        return redirect(Contact_page)
def card_page(req):
    data = categoryDb.objects.all()
    cdata=CartDb.objects.filter(UseName=req.session['RegName'])
    return render(req,"Card.html",{'data':data,'cdata':cdata})
def savecart_page(req):
    if req.method=="POST":
        usName=req.POST.get('usname')
        proName=req.POST.get('proname')
        prodis=req.POST.get('dis')
        prototal=req.POST.get('totalprice')
        proqty=req.POST.get('qtyy')
        obj=CartDb(UseName=usName,ProName=proName,ProDis=prodis,ProTotal=prototal,ProQuantity=proqty)
        obj.save()
        return redirect(card_page)
def delete_cart(req,cartid):
    cart=CartDb.objects.filter(id=cartid)
    cart.delete()

    return redirect(card_page)

def checkout_page(req):
    data = categoryDb.objects.all()

    return render(req,"checkout_pro.html",{'data':data})
def save_checkout(req):
    if req.method=="POST":
        na=req.POST.get('name')
        em=req.POST.get('email')
        add=req.POST.get('address')
        phon=req.POST.get('phone')
        bi=req.POST.get('bill')
        obj=CheckoutDb(CheckName=na,Checkemail=em,CheckAddress=add,CheckPhone=phon,CheckSubject=bi)
        obj.save()
        messages.success(req,"Your order is placed successfully..")

        return redirect(home_page)