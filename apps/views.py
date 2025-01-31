from django.shortcuts import render
from .models import Product 
from .form import ProductForm

# Create your views here.

def homepage(request):
    mahsulotlar = Product.objects.all()
    context = {
        'mahsulotlar': mahsulotlar
    }

    if request.method == 'POST':
        search_query = request.POST.get('search_query')
        results = Product.objects.filter(name__icontains=search_query)
        return render(request, 'index.html', {'mahsulotlar': results})  
    return render(request, 'index.html', context=context)



def about(request):
    return render(request, 'about.html')





def products(request):
    mahsulotlar = Product.objects.all()
    context = {
        'mahsulotlar': mahsulotlar
    }
    
    return render(request, 'products.html', context=context)

    
def whyus(request):
    return render(request, 'whyus.html')
    
def testimonial(request):
    return render(request, 'testimonial.html')
    