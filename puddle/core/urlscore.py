from django.urls import path
from core  import views
#tambahan untuk mengimport gambar
from django.conf import settings
from django.conf.urls.static import static
#tambahkan ini untuk membuat login (dengan rename views menjadi auth_views agaaar tidak crash)
from django.contrib.auth import views as auth_views
from .forms import LoginForm



urlpatterns =[
    path('',views.index,name="index"),
    path('contact/',views.contact,name="contact"),
    path('signup/',views.signup,name='signup'),
    path('login/',auth_views.LoginView.as_view(template_name='core/login.html',authentication_form=LoginForm),name='login')
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
