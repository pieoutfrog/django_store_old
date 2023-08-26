from django.shortcuts import render
from catalog.models import Product, Contact, Category


def home(request):
    latest_products = Product.objects.order_by('-id')[:5]
    context = {'latest_products': latest_products,
               'title': 'Наши последние товары'}
    return render(request, 'catalog/home.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, message=message)
        contact.save()
        print(f'Имя пользователя: {name}, Почта: {email}, Сообщение: {message}')

    all_contacts = Contact.objects.all()
    context = {'all_contacts': all_contacts,
               'title': 'Контактные данные'}
    return render(request, 'catalog/contacts.html', context)


def product_details(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {'product': product}
    return render(request, 'catalog/product.html', context)


def products(request):
    products_list = Product.objects.all()
    context = {'products': products_list}
    return render(request, 'catalog/products.html', context)


def category_products(request, category_id):
    category = Category.objects.get(id=category_id)
    products_list = Product.objects.filter(category=category)
    context = {'category': category, 'products': products_list}
    return render(request, 'catalog/category_products.html', context)






