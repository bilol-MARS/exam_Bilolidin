from django.shortcuts import render, redirect
from .models import Product, User, WishList, Saqlovchi
from .form import ProductForm
from django.views.generic import TemplateView, CreateView, FormView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .forms import UserCreateForm, UserLoginForm
from .mixins import NotLoginRequired
from httpx import get
BOT_TOKEN = '7445052239:AAFY-RIVGfZmqVpUaIIWuPKKseCBwWHLe8g'

from django.contrib.auth import login, logout
# Create your views here.


class ContactView(ListView):
    model = Product
    context_object_name = 'contact'
    template_name = 'about.html'   


def send_message(chat_id, message) :
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    params = {
        'chat_id': chat_id,
        'text': message
    }
    response = get(url, params=params)
   
    # print(response.text, response.status_code)


def contactview(request):
    if request.method == 'POST':
        data = request.POST
        message = data.get('text')
        text = f"""
Foydalanuvchidan habar: {message}

"""
        data = Saqlovchi.objects.create(
            message = message,
        )
        data.save()
        send_message(2041375313, text)
    return render(request, 'about.html')


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
    




class SavatchaView(ListView):
    template_name = 'savatcha.html'
    model = WishList
    context_object_name = 'mahsulotlar'

    def get_queryset(self):
        return WishList.objects.filter(user=self.request.user)




class ShoppingCartCreateView(LoginRequiredMixin, View): 
# model = ShoppingCart
# template_name = 'shop.html'
    login_url = 'login'

    def get(self, *args, **kwargs):
        user = self.request.user
        pk = self.kwargs.get('pk')
        product = Product.objects.filter(pk=pk).first()
        print(user)
        print(pk)
        print(product)
        
        if user and pk:
            if not WishList.objects.filter(product=product, user=user).exists():
                WishList.objects.create(
                    user=user,
                    product=product
                )
            else:
                wishlist = WishList.objects.filter(product=product).first()
                wishlist.delete()
        return redirect('products')


class UserCreateView(CreateView):
    model = User
    form_class = UserCreateForm
    template_name = 'register.html'
    success_url = '/'


class UserSigninView(FormView):
    form_class = UserLoginForm
    template_name = 'login.html'
    success_url = '/'


    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = User.objects.filter(username=username).first()
        if user and user.check_password(password):
            login(self.request, user)
            return redirect('/') 
        return super().form_valid(form)
    

class UserLogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('/')
    
