from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt



urlpatterns = [
    path('', views.home, name='home'),
    path('faq/', views.faq, name='faq'),
    path('contact/', views.contact,  name='contact'),
    # path('contact_form/', views.contact_form),
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)