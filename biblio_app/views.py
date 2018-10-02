from django.http import HttpResponse
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
    def post(self, request, category_id, subcategory_id):
        form = Less3AuthorsForm(request.POST)
        if form.is_valid():
            author1_name = form.cleaned_data['author1_name']
            author1_last_name = form.cleaned_data['author1_last_name']
            author2_name = form.cleaned_data['author2_name']
            author2_last_name = form.cleaned_data['author2_last_name']
            author3_name = form.cleaned_data['author3_name']
            author3_last_name = form.cleaned_data['author3_last_name']
            title = form.cleaned_data['title']
            translator_name = form.cleaned_data['translator_name']
            translator_last_name = form.cleaned_data['translator_last_name']
            city = form.cleaned_data['city']
            year = form.cleaned_data['year']
            volume = form.cleaned_data['volume']
            page = form.cleaned_data['page']
            ctx = {'author1_name': author1_name,
                   'author1_last_name': author1_last_name,
                   'author2_name':author2_name,
                   'author2_last_name':author2_last_name,
                   'author3_name':author3_name,
                   'author3_last_name':author3_last_name,
                   'title':title,
                   'translator_name':translator_name,
                   'translator_last_name':translator_last_name,
                   'city':city,
                   'year':year,
                   'volume':volume,
                   'page':page}
        return render(request, 'less3authors-template.html', ctx)