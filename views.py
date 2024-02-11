from django.shortcuts import render ,redirect
from .models import Product 
from .models import Contact
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def product(request,pk):
    products = Product.objects.get(id=pk)
    return render(request, 'product.html' , {'product': product})

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html' , {'products': products})

def faq(request):
    return render(request, 'faq.html' , {})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username , password=password)
        if user is not None:
            login(request,user)
            messages.success(request, ("YOu Have Been logged In!"))
            return redirect('home')
        else:
            messages.success(request, ("There was an error, Please try again"))
            return redirect('login')
    else:
        return render(request, 'login.html', {})
    

def logout_user(request):
        logout(request)
        messages.success(request , ("You have been logged out..."))
        return redirect('login')


def contact(request):
    if request.method == "POST":
        contact=Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact.name = name
        contact.email = email
        contact.message = message
        contact.save()
        send_mail(
            'New Contact Form Submission',
            f'A new contact form submission has been received from {name} ({email}). Message: {message}',
            'hina.zailai97@gmail.com',['zamin2212@gmail.com', 'hina.zailai97@gmail.com'], fail_silently=False)
        return render(request, 'contact.html',{'name' : name})
    else:
        return render(request, 'contact.html',{})

