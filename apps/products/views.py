from django.shortcuts import render,redirect
from apps.settings.models import Setting
from apps.products.models import Product,ProductLike,Currency
from django.db.models import Q

# Create your views here.
def product_detail(request,id):
  setting = Setting.objects.latest('id')
  product = Product.objects.get(id = id)
  random_products = Product.objects.all().order_by('?')
  if request.method == "POST":
    try:
      like = ProductLike.objects.get(user = request.user,product = product)
      like.delete()
    except:
      ProductLike.objects.create(user = request.user, product = product)
  context = {
      'setting' : setting,
      'product' : product,
      'random_products' : random_products,
  }
  return render(request, 'single-product.html', context)

def product_index(request):
  setting = Setting.objects.latest('id')
  products = Product.objects.all()
  
  context = {
    'setting' : setting,
    'products' : products,
  }
  return render(request, 'shop.html', context)

def product_create(request):
  setting = Setting.objects.latest('id')
  currency = Currency.objects.all()

  if request.method == "POST":
    title = request.POST.get('title')
    description = request.POST.get('description')
    image = request.FILES.get('image')
    price = request.POST.get('price')
    currency = request.POST.get('currency')
    product = Product.objects.create(user = request.user, title = title,description = description, image = image, price = price,currency_id=currency)
    return redirect('product_detail', product.id)
  context={
    'setting' : setting,
    'currency' : currency,
  }
  return render(request,'product_create.html',context)

def product_search(request):
  product = Product.objects.all()
  setting = Setting.objects.latest('id')
  search_key = request.GET.get('key')
  if search_key:
    product = Product.objects.filter(Q(title__icontains = search_key) | Q (description__icontains = search_key ))
  context = {
    'setting' : setting,
    'product' : product,
  }
  return render (request, 'search.html', context)