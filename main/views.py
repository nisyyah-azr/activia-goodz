from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
import json
from django.contrib.auth.models import User
import re

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    context = {
        'npm': '2406495823',
        'name': request.user.username,
        'class': 'PBP A',
        'last_login': request.COOKIES.get('last_login', 'Never'),
    }
    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit = False)
        product_entry.user = request.user
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.increment_views()

    context = {
        'product': product
    }

    return render(request, "product_detail.html", context)

def show_xml(request):
    products_list = Product.objects.all()
    xml_data = serializers.serialize("xml", products_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    user_filter = request.GET.get('filter')
    category_filter = request.GET.get('category')
    
    if user_filter == 'my_products':
        products_list = Product.objects.filter(user=request.user)
    else:
        products_list = Product.objects.all()
    
    if category_filter:
        products_list = products_list.filter(category=category_filter)
    
    data = [
        {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'product_views': product.product_views,
            'created_at': product.created_at.isoformat() if product.created_at else None,
            'is_featured': product.is_featured,
            'user_id': product.user_id,
        }
        for product in products_list
    ]
    
    return JsonResponse(data, safe=False)

def show_xml_by_id(request, product_id):
   try:
       product_item = Product.objects.filter(pk=product_id)
       xml_data = serializers.serialize("xml", product_item)
       return HttpResponse(xml_data, content_type="application/xml")
   except Product.DoesNotExist:
       return HttpResponse(status=404)

def show_json_by_id(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
        product.increment_views()
        
        data = {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'product_views': product.product_views,
            'created_at': product.created_at.isoformat() if product.created_at else None,
            'is_featured': product.is_featured,
            'user_id': product.user_id,
            'user_username': product.user.username if product.user_id else None,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {'form': form }

    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
@require_POST
def add_product_ajax(request):
    name = strip_tags(request.POST.get("name"))
    price = request.POST.get("price")
    description = strip_tags(request.POST.get("description"))
    category = request.POST.get("category")
    thumbnail = request.POST.get("thumbnail")
    is_featured = request.POST.get("is_featured") == 'on'
    user = request.user
    
    new_product = Product(
        name=name,
        price=price,
        description=description,
        category=category,
        thumbnail=thumbnail,
        is_featured=is_featured,
        user=user
    )
    new_product.save()
    
    return HttpResponse(b"CREATED", status=201)

@csrf_exempt
def update_product_ajax(request, id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=id, user=request.user)
        
        product.name = strip_tags(request.POST.get("name"))
        product.price = request.POST.get("price")
        product.description = strip_tags(request.POST.get("description"))
        product.category = request.POST.get("category")
        product.thumbnail = request.POST.get("thumbnail")
        product.is_featured = request.POST.get("is_featured") == 'on'
        
        product.save()
        return HttpResponse(b"UPDATED", status=200)
    
    return HttpResponse(b"METHOD_NOT_ALLOWED", status=405)

@csrf_exempt
@require_POST
def delete_product_ajax(request, id):
    product = get_object_or_404(Product, pk=id, user=request.user)
    product.delete()
    return HttpResponse(b"DELETED", status=200)

@require_POST
def login_ajax(request):
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({
            'status': 'error', 
            'message': 'Invalid JSON format'
        }, status=400)

    # Sanitize dan validasi input
    username = strip_tags(data.get('username', '')).strip()
    password = strip_tags(data.get('password', '')).strip()

    # Validasi input tidak kosong
    if not username or not password:
        return JsonResponse({
            'status': 'error', 
            'message': 'Username and password are required'
        }, status=400)

    # Batasi panjang input untuk mencegah abuse
    if len(username) > 150:
        return JsonResponse({
            'status': 'error', 
            'message': 'Username is too long'
        }, status=400)
    
    if len(password) > 128:
        return JsonResponse({
            'status': 'error', 
            'message': 'Password is too long'
        }, status=400)

    # Validasi karakter username (hanya huruf, angka, underscore)
    if not re.match(r'^[\w]+$', username):
        return JsonResponse({
            'status': 'error', 
            'message': 'Username can only contain letters, numbers, and underscores'
        }, status=400)

    # Autentikasi user
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        response_data = {
            'status': 'success',
            'message': 'Login successful',
            'redirect_url': reverse('main:show_main'),
            'username': user.username
        }
        response = JsonResponse(response_data)
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
    else:
        return JsonResponse({
            'status': 'error',
            'message': 'Invalid username or password'
        }, status=401)


@require_POST
def register_ajax(request):
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({
            'status': 'error', 
            'message': 'Invalid JSON format'
        }, status=400)

    # Sanitize semua input
    username = strip_tags(data.get('username', '')).strip()
    password1 = strip_tags(data.get('password1', '')).strip()
    password2 = strip_tags(data.get('password2', '')).strip()

    # Validasi input tidak kosong
    if not username or not password1 or not password2:
        return JsonResponse({
            'status': 'error', 
            'message': 'All fields are required'
        }, status=400)

    # Validasi panjang username
    if len(username) < 3:
        return JsonResponse({
            'status': 'error', 
            'message': 'Username must be at least 3 characters long'
        }, status=400)
    
    if len(username) > 150:
        return JsonResponse({
            'status': 'error', 
            'message': 'Username is too long (max 150 characters)'
        }, status=400)

    # Validasi karakter username (hanya huruf, angka, underscore)
    if not re.match(r'^[\w]+$', username):
        return JsonResponse({
            'status': 'error', 
            'message': 'Username can only contain letters, numbers, and underscores'
        }, status=400)

    # Validasi password cocok
    if password1 != password2:
        return JsonResponse({
            'status': 'error', 
            'message': 'Passwords do not match'
        }, status=400)

    # Validasi panjang password minimal
    if len(password1) < 8:
        return JsonResponse({
            'status': 'error', 
            'message': 'Password must be at least 8 characters long'
        }, status=400)
    
    if not re.search(r'[A-Za-z]', password1) or not re.search(r'[0-9]', password1):
        return JsonResponse({
            'status': 'error', 
            'message': 'Password must contain both letters and numbers'
        }, status=400)

    # Cek apakah username sudah ada
    if User.objects.filter(username=username).exists():
        return JsonResponse({
            'status': 'error', 
            'message': 'Username already exists'
        }, status=400)

    try:
        # Buat user baru
        user = User.objects.create_user(username=username, password=password1)
        user.save()

        return JsonResponse({
            'status': 'success',
            'message': 'Registration successful',
            'redirect_url': reverse('main:login'),
            'username': username
        })
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': 'Failed to create account. Please try again.'
        }, status=500)