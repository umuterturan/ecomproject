from django.shortcuts import render
from .models import Product, Category
from .forms import ContactForm
from django.views.generic.edit import FormView
from django.core.mail import send_mail

class ContactView(FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = "/thankyou" 

    def form_valid(self, form):
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        sender_email = form.cleaned_data['sender_email']
        to_email = 'umut.erturan1@gmail.com'

        send_mail(subject, message, sender_email, [to_email])

        return super().form_valid(form)
    

def search_results(request):
    query = request.GET.get('q')
    results = Product.objects.all()

    if query:
        results = results.filter(name__icontains=query) | results.filter(description__icontains=query)

    return render(request, 'search_results.html', {'results': results, 'query': query})


def sale(request):
    products = Product.objects.filter(is_sale=True)
    return render(request, 'sale.html', {
        'products': products
    })

def thankyou(request):
    return render(request, 'thankyou.html')

def category(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    return render(request, 'category.html', {
        'category': category,
    })

def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product.html', {
        'product' : product
    })

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {
        'products' : products
    })

def about(request):
    return render(request, 'about.html')