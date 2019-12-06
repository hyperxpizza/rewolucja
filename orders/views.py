from django.shortcuts import render
from .models import OrderItem
from .forms import OrderForm
from cart.cart import Cart
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.

def order_create(request):
    cart = Cart(request)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,product=item['product'],price=item['price'],quantity=item['quantity'])
            cart.clear()
            send_email(order)

            return render(request,'orders/order/created.html', {'order':order})
    else:
        form = OrderForm()
    return render(request, 'orders/order/create.html', {'form':form, 'cart':cart})

def send_email(order):
    subject = "Dziękujemy za zakupy na rewolucja.com.pl!"
    message = "Numer twojego zamówienia to: " + str(order.id) 
    send_mail(
        subject,
        message,
        'studio.rewolucja@gmail.com',
        [order.email]
    )
    print("Confirmation email send to: " + str(order.email))

    subject2 = "Nowe zamówienie" + str(order.id)
    message2 = "Imie: " + order.first_name + " " + order.last_name + "Email: " + order.email + "Telefon: " + str(order.phone) + "Adres: " + order.adress + " " + order.postal_code + " " + order.city

    send_mail(
        subject2,
        message2,
        'studio.rewolucja@gmail.com',
        ['studio.rewolucja@gmail.com']
    )

    print("Internal email send to studio.rewolucja@gmail.com")