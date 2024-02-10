from django.shortcuts import render
from .models import Product 
from .models import Contact
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse


def home(request):
    products = Product.objects.all()
    return render(request, 'home.html' , {'products': products})

def faq(request):
    return render(request, 'faq.html' , {})


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

