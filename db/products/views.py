from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Product, ProductSubCategory
from .forms import ProductForm, ProductSubCategoryForm

def product_list(request):
    products = Product.objects.all()
    query = request.GET.get('q')
    if query:
        products = products.filter(product_name__icontains=query)
    return render(request, 'product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    subcategories = ProductSubCategory.objects.filter(product=product)
    return render(request, 'product_detail.html', {'product': product, 'subcategories': subcategories})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'product_form.html', {'form': form})

def add_subcategory(request):
    if request.method == 'POST':
        form = ProductSubCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductSubCategoryForm()
    return render(request, 'subcategory_form.html', {'form': form})

def update_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'product_form.html', {'form': form})

def update_subcategory(request, pk):
    subcategory = get_object_or_404(ProductSubCategory, pk=pk)
    if request.method == 'POST':
        form = ProductSubCategoryForm(request.POST, request.FILES, instance=subcategory)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductSubCategoryForm(instance=subcategory)
    return render(request, 'subcategory_form.html', {'form': form})

def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('product_list')

def delete_subcategory(request, pk):
    subcategory = get_object_or_404(ProductSubCategory, pk=pk)
    subcategory.delete()
    return redirect('product_list')
