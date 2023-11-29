from django.shortcuts import render, redirect

from photographyapp.models import Customer
from photographyapp.forms import CustomerForm


# Create your views here.

def home(request):
    return render(request, 'index.html')

def gallery(request):
    return render(request, 'gallery.html')

def aboutus(request):
    return render(request, 'about.html')

def contacts(request):
    return render(request, 'contacts.html')

def appointment(request):
    if request.method == 'POST':
        customer =Customer(firstname=request.POST['firstname'], lastname=request.POST['lastname'],
                            address=request.POST['address'],
                            phonenumber=request.POST['phonenumber'], email=request.POST['email'], service=request.POST['service'])

        customer.save()
        return redirect("/customers/")
    else:
        return render(request, 'appointments.html')

    form = CustomerForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect("/customers/")

    else:
        form = CustomerForm()
        return render(request, 'appointments.html', {'form': form})





def inner(request):
    return render(request,'innerpage.html')

def services(request):
    return render(request,' services.html')

def customer(request):
    customers = Customer.objects.all()
    return render(request, 'customers.html', {'customers': customers})

def delete(request, id):
    customer = Customer.objects.get(id=id)
    customer.delete()
    return redirect('/customers')

def edit(request, id):
    customer = Customer.objects.get(id=id)
    return render(request, 'edit.html', {'customer':customer})

def update(request, id):
    customer = Customer.objects.get(id=id)
    form = CustomerForm(request.POST, instance=customer)
    if form.is_valid():
        form.save()
        return redirect('/customers')
    else:
        return render(request, 'edit.html', {'customer':customer})



