
from django.contrib import admin
from django.urls import path
from photographyapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='index'),
    path('appointment/', views.appointment, name='appointments'),
    path('contacts/', views.contacts, name='contacts'),
    path('inner/', views.inner, name='inner'),
    path('about/', views.aboutus, name='about'),
    path('gallery/', views.gallery, name='gallery'),
    path('services/', views.services, name='services'),
    path('customers/', views.customer, name='customers'),
    path('delete/<int:id>', views.delete),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),

]
