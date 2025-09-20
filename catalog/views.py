from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from catalog.models import Product


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product
    queryset = Product.objects.all()


class ProductCreateView(CreateView):
    model = Product
    fields = ("name", "description", "photo", "categor", "price")
    success_url = reverse_lazy('catalog:product_list')

def home(request):
    return render(request, 'home.html')


def contacts(request):
    return render(request, 'contacts.html')


