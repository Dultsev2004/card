from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('service/', views.ServiceView.as_view(), name='service'),
    path('service/<int:pk>/', views.service_detail, name='service-detail'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('create_service/', views.create_service, name='create_service'),
    path('logged_out/', views.LogoutView.as_view(), name='logged_out'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegistrationView.as_view(), name='registration'),
    path('search_result/', views.search_view, name='search'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)