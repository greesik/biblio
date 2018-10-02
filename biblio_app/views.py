from django.shortcuts import render
from django.views import View

from biblio_app.models import MainCategory, SubCategory


class MainCategoryView(View):
    def get(self, request):
        ctx = {"main_category": MainCategory.objects.all()}
        return render(request, 'main-category.html', ctx)


class SubCategoryView(View):
    def get(self, request, category_id):
        ctx = {"subcategory": SubCategory.objects.filter(main_cat=category_id)}
        return render(request, 'subcategory.html', ctx)
