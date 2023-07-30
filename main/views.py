from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from hitcount.views import HitCountDetailView
from hitcount.utils import get_hitcount_model
from hitcount.views import HitCountMixin
# Create your views here.
from .models import *
from .EmailBackEnd import EmailBackEnd
from .forms import Sending
from .models import Contact, Send
import smtplib
from . import models

def index(request):
    blog = Blog.objects.all()
    about = About.objects.all()
    hujjatlar = Hujjatlar.objects.all()
    karusel1 = Karusel1.objects.all()
    karusel2 = KaruselLoop.objects.all()
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact = Contact(
            name=name,
            email=email,
            phone=phone,
            message=message
        )
        contact.save()
        messages.success(request, 'Sizning xabaringiz muvaffaqiyatli yuborildi!')
        return redirect('index')

    ctx = {
        'blog':blog,
        'about':about,
        'hujjatlar':hujjatlar,
        'karusel1':karusel1,
        'karusel2':karusel2,
    }
    return render(request,'index.html',ctx)

@login_required(login_url='/')
def post(request):
    email = Contact.objects.all()
    send = Send.objects.all()
    module = Send()
    form = Sending(request.POST, instance=module)
    print(request.POST)
    if form.is_valid():
        form.save()
        messages.error(request, f"{form.instance.sending} || {form.instance.message} xabari jo'natildi")
        res = f"{form.instance.sending}"
        sender = "nargizsarvar.xk@gmail.com"
        pas = "mcjmpckqzxrswfng"
        m = form.instance.message
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender, pas)
        print("login kirildi")
        server.sendmail(sender, f"{form.instance.sending}", f"{form.instance.message}")
        print(f"jonattim {res} ga")

        return redirect("post")

    ctx = {
        "form": form,
        'email':email,
        'send':send
    }

    return render(request, "email/jonat.html", ctx)

@login_required(login_url="/")
def delete(request, id):
    send = Send.objects.get(id=id)
    send.delete()
    messages.success(request, 'UCHIRILDI')
    return redirect('post')\

@login_required(login_url="/")
def delete_cont(request, id):
    send = Contact.objects.get(id=id)
    send.delete()
    messages.success(request, 'UCHIRILDI')
    return redirect('post')

def doLogin(request):
        if request.method == "POST":
            user = EmailBackEnd.authenticate(request, username=request.POST.get('username'),
                                             password=request.POST.get('password'))
            if user != None:
                login(request, user)
                messages.error(request, 'EMAILGA XABAR YUBORISH GA KIRDINGIZ')
                return redirect('post')
            else:
                messages.error(request, 'Email and  Password Are Invalid !')
                return redirect('login')
        return None


def llogout(request):
    logout(request)
    return redirect('index')


def LOGIN(request):
    return render(request, 'login.html')

def qr_all(r):
    qrcode = Hujjatlar.objects.all()

    ctx = {
        'qrcode':qrcode
    }

    return render(r,'qr_code.html',ctx)
