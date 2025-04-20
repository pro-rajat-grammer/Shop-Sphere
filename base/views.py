from django.shortcuts import render,redirect
from .models import products,Contactmodel,Cart
from django.db.models import Q
from .forms import Contact
from django.contrib.auth.decorators import login_required
# Create your views here.
global all


def home(request):
    links=[]
    for i in products.objects.all():
        if i.category not in links:
            links+=[i.category]
    all=[]
    if 'cat' in request.GET:
        cat=request.GET['cat']
        all=products.objects.filter(category=cat)
    elif 'q' in request.GET :
        q=request.GET['q']
        all=products.objects.filter(Q(category__icontains=q)|Q(name__icontains=q)|Q(desc__icontains=q))
    elif 'TRENDING' in request.GET:
        for i in products.objects.filter(trend=1):
            print(i)
            all+=[i]
    else:
        all=products.objects.all()


    if request.user.is_authenticated:
        about=False
    else:
        about=True

    # if len(all)==0:
    #     noproduct=True
    # else:
    #     noproduct=False

    noproduct = len(all) == 0
    

    # if request.user.is_authenticated:
    #     count=Cart.objects.filter(host=request.user).count()
    # else:
    #     count=None
    count = Cart.objects.filter(host=request.user).count() if request.user.is_authenticated else None

    context={'products':all,'links':links,'showtrend':True,'about':about,'noproduct':noproduct,'count':count}
    
    return render(request,'home.html',context )


def about(request):
    if request.user.is_authenticated:
        count=Cart.objects.filter(host=request.user).count()
    return render(request,'about.html',{'about':True,'count':count})


def contactus(request):
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']
        Contactmodel.objects.create(firstname=firstname,lastname=lastname,email=email,phone=phone,message=message)
        return render(request,'request.html')
    
    if request.user.is_authenticated:
        count=Cart.objects.filter(host=request.user).count()

    
    return render(request,'contactus.html',{'Contact':Contact,'about':True,'count':count})


@login_required (login_url='login_')
def addcart(request,id):
    a=products.objects.get(id=id)
    try:
        c=Cart.objects.get(name=a.name,host=request.user)
        c.quantity+=1
        c.totalprice+=a.price
        c.save()
    except:
        Cart.objects.create(category=a.category,name=a.name,desc=a.desc,price=a.price,totalprice=a.price,host=request.user)
    return redirect('home')


def profile(request):
    if request.user.is_authenticated:
        count=Cart.objects.filter(host=request.user).count()
    return render(request,'profile.html',{'about':True,'count':count})


def cart(request):
    a=Cart.objects.filter(host=request.user)
    finaltotal=Cart.objects.filter(host=request.user)
    final=0
    for i in finaltotal:
        final+=i.totalprice

    if request.user.is_authenticated:
        count=Cart.objects.filter(host=request.user).count()
    return render(request,'cart.html',{'a':a,'count':count,'final':final})

def cartitemrem(request,id):
    a=Cart.objects.get(id=id)
    a.delete()
    return redirect('cart')

def checkoutform(request):
    if request.method == 'POST':
        return redirect('placeorder')
    return render(request,'checkoutform.html')

def placeorder(request):
    return render(request,'placeorder.html')