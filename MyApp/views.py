from django.shortcuts import render,redirect
from .models import *

# Create your views here.


def home(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        number = request.POST.get('number')
        password = request.POST.get('password')
        try:
            data = Register.objects.get(Number = number, Password = password)
            return redirect('userhome', user = data.Number)
        except Register.DoesNotExist:
            return redirect('register')
        
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        mail = request.POST.get('mail')
        number = request.POST.get('number')
        password = request.POST.get('password')
        address = request.POST.get('address')
        pinCode = request.POST.get('pincode')

        obj = Register(
            Name = name,
            Mail = mail,
            Number = number,
            Password = password,
            Address = address,
            PinCode = pinCode,
        )
        obj.save()
        return redirect('login')
    
    return render(request, 'register.html')

def userhome(request, user):
    userData = Register.objects.get(Number = user)
    return render(request, 'userhome.html',  {'userData' : userData})

def userprofile(request, user):
    userData = Register.objects.get(Number = user)
    return render(request, 'profile.html',  {'userData' : userData})

def trainbooking(request,user):
    userData = Register.objects.get(Number = user)
    if request.method == 'POST':
        name = request.POST.get('name')
        booking = request.POST.get('booking')
        number = request.POST.get('number')
        date = request.POST.get('date')
        bookNumber = request.POST.get('hidden')

        obj = Booking(
            Name = name,
            Booking = booking,
            Number = number,
            Date = date,
            BookingNumber = bookNumber,
        )
        obj.save()
        return redirect('userhome', user = userData.Number)
    
    return render(request, 'trainbooking.html', {'userData' : userData})

def busbooking(request,user):
    userData = Register.objects.get(Number = user)
    if request.method == 'POST':
        name = request.POST.get('name')
        booking = request.POST.get('booking')
        number = request.POST.get('number')
        date = request.POST.get('date')
        bookNumber = request.POST.get('hidden')

        obj = Booking(
            Name = name,
            Booking = booking,
            Number = number,
            Date = date,
            BookingNumber = bookNumber,
        )
        obj.save()
        return redirect('userhome', user = userData.Number)
    
    return render(request, 'busbooking.html', {'userData' : userData})

def hotelbooking(request,user):
    userData = Register.objects.get(Number = user)
    if request.method == 'POST':
        name = request.POST.get('name')
        booking = request.POST.get('booking')
        number = request.POST.get('number')
        date = request.POST.get('date')
        bookNumber = request.POST.get('hidden')

        obj = Booking(
            Name = name,
            Booking = booking,
            Number = number,
            Date = date,
            BookingNumber = bookNumber,
        )
        obj.save()
        return redirect('userhome', user = userData.Number)
    
    return render(request, 'hotelbooking.html', {'userData' : userData})

def bookingspage(request,user):
    userdata = Register.objects.get(Number = user)
    bookings = Booking.objects.all()
    return render(request, 'bookingspage.html', {'userdata' : userdata, 'bookings': bookings})