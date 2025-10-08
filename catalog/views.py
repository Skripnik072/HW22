from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, ProductModeratorForm
from catalog.models import Product, Category
from catalog.services import get_products_from_cache
from config.settings import CACHE_ENABLED
from catalog.services import ProductsService


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        if CACHE_ENABLED:
            return get_products_from_cache()
        else:
            return Product.objects.filter(views_counter__gt=-1)


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    queryset = Product.objects.all()

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def get_success_url(self):
        return reverse('catalog:product_detail', args=[self.kwargs.get('pk')])

    def get_form_class(self):
        user = self.request.user
        if user == self.request.user:
            return ProductForm
        if user.has_perm("catalog.can_unpublish_product"):
            return ProductModeratorForm
        raise PermissionDenied

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')

    def get_form_class(self):
        user = self.request.user
        if user == self.request.user:
            return ProductForm
        if user.has_perm("can_delete_product"):
            return ProductModeratorForm
        raise PermissionDenied

def home(request):
    return render(request, 'home.html')


def contacts(request):
    return render(request, 'contacts.html')

class ProductsCategoryView(LoginRequiredMixin, ListView):
    model = Product
    template_name = "catalog/products_by_category.html"
    context_object_name = "prodcat"

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        return ProductsService.get_products_by_category(category_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs.get('category_id')
        context["category_id"] = category_id
        return context

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     categories = Product.objects.values_list('categor', flat=True).distinct()
    #     context['categories'] = categories
    #     return context
