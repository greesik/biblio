from django.shortcuts import render
from django.views import View

from biblio_app.forms import Less3AuthorsForm
from biblio_app.models import MainCategory, SubCategory


class MainCategoryView(View):
    def get(self, request):
        ctx = {"main_category": MainCategory.objects.all()}
        return render(request, 'main-category.html', ctx)


class SubCategoryView(View):
    def get(self, request, category_id):
        ctx = {"subcategory": SubCategory.objects.filter(main_cat=category_id),
               "id_category": category_id}
        return render(request, 'subcategory.html', ctx)


class CertainSubCategoryView(View):
    def get(self, request, category_id, subcategory_id):
        ctx = {"subcategory": SubCategory.objects.filter(main_cat=category_id),
               "certain_subcategory": SubCategory.objects.filter(id=subcategory_id)}
        return render(request, 'certain-subcategory.html', ctx)


class Less3AuthorsFormView(View):
    def get(self, request, category_id, subcategory_id):
        form = Less3AuthorsForm()
        return render(request, 'certain-subcategory.html', {'form':form, 'button': 'Generuj przypis!'})
