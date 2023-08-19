from django.shortcuts import render

from catalog.models import Product, Contact


def home(request):
    latest_products = Product.objects.order_by('-id')[:5]
    for product in latest_products:
        print(product)
    return render(request, 'catalog/home.html', {'latest_products': latest_products})


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, message=message)
        contact.save()
        print(f'Имя пользователя: {name}, Почта: {email}, Сообщение: {message}')
    all_contacts = Contact.objects.all()
    return render(request, 'catalog/contacts.html', {'all_contacts': all_contacts})
