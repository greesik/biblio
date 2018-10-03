from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from biblio_app.forms import Less3AuthorsForm, CompositeWorkForm, DailyMagazineForm, More3AuthorsForm, \
    PeriodicalMagazineForm, FilmForm, WebArticleForm, WebPageForm, FotoForm
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


class FormsView(View):

    def get(self, request, category_id, subcategory_id):
        if subcategory_id == '1':
            form = Less3AuthorsForm()
            return render(request, 'certain-subcategory.html', {'form': form, 'button': 'Generuj przypis!'})
        elif subcategory_id == '2':
            form = More3AuthorsForm()
            return render(request, 'certain-subcategory.html', {'form': form, 'button': 'Generuj przypis!'})
        elif subcategory_id == '3':
            form = CompositeWorkForm()
            return render(request, 'certain-subcategory.html', {'form': form, 'button': 'Generuj przypis!'})
        elif subcategory_id == '4':
            form = DailyMagazineForm()
            return render(request, 'certain-subcategory.html', {'form': form, 'button': 'Generuj przypis!'})
        elif subcategory_id == '5':
            form = PeriodicalMagazineForm()
            return render(request, 'certain-subcategory.html', {'form': form, 'button': 'Generuj przypis!'})
        elif subcategory_id == '6':
            form = WebArticleForm()
            return render(request, 'certain-subcategory.html', {'form': form, 'button': 'Generuj przypis!'})
        elif subcategory_id == '7':
            form = WebPageForm()
            return render(request, 'certain-subcategory.html', {'form': form, 'button': 'Generuj przypis!'})
        elif subcategory_id == '8':
            form = FilmForm()
            return render(request, 'certain-subcategory.html', {'form': form, 'button': 'Generuj przypis!'})
        elif subcategory_id == '9':
            form = FotoForm()
            return render(request, 'certain-subcategory.html', {'form': form, 'button': 'Generuj przypis!'})

    def post(self, request, category_id, subcategory_id):
        if subcategory_id == '1':
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
                       'author2_name': author2_name,
                       'author2_last_name': author2_last_name,
                       'author3_name': author3_name,
                       'author3_last_name': author3_last_name,
                       'title': title,
                       'translator_name': translator_name,
                       'translator_last_name': translator_last_name,
                       'city': city,
                       'year': year,
                       'volume': volume,
                       'page': page}
                return render(request, 'less3authors-template.html', ctx)
        if subcategory_id == '2':
            form = More3AuthorsForm(request.POST)
            if form.is_valid():
                editor1_name = form.cleaned_data['editor1_name']
                editor1_last_name = form.cleaned_data['editor1_last_name']
                editor2_name = form.cleaned_data['editor2_name']
                editor2_last_name = form.cleaned_data['editor2_last_name']
                title = form.cleaned_data['title']
                translator_name = form.cleaned_data['translator_name']
                translator_last_name = form.cleaned_data['translator_last_name']
                city = form.cleaned_data['city']
                year = form.cleaned_data['year']
                volume = form.cleaned_data['volume']
                page = form.cleaned_data['page']
                ctx = {'editor1_name': editor1_name,
                       'editor1_last_name': editor1_last_name,
                       'editor2_name': editor2_name,
                       'editor2_last_name': editor2_last_name,
                       'title': title,
                       'translator_name': translator_name,
                       'translator_last_name': translator_last_name,
                       'city': city,
                       'year': year,
                       'volume': volume,
                       'page': page}
                return render(request, 'more3authors-template.html', ctx)
        if subcategory_id == '3':
            form = CompositeWorkForm(request.POST)
            if form.is_valid():
                author_name = form.cleaned_data['author_name']
                author_last_name = form.cleaned_data['author_last_name']
                text_title = form.cleaned_data['text_title']
                editor_name = form.cleaned_data['editor_name']
                editor_last_name = form.cleaned_data['editor_last_name']
                book_title = form.cleaned_data['book_title']
                translator_name = form.cleaned_data['translator_name']
                translator_last_name = form.cleaned_data['translator_last_name']
                city = form.cleaned_data['city']
                year = form.cleaned_data['year']
                page = form.cleaned_data['page']
                ctx = {
                    'author_name': author_name,
                    'author_last_name': author_last_name,
                    'text_title': text_title,
                    'editor_name': editor_name,
                    'editor_last_name': editor_last_name,
                    'book_title': book_title,
                    'translator_name': translator_name,
                    'translator_last_name': translator_last_name,
                    'city': city,
                    'year': year,
                    'page': page}
                return render(request, 'composite-work-template.html', ctx)
        if subcategory_id == '4':
            form = DailyMagazineForm(request.POST)
            if form.is_valid():
                author_name = form.cleaned_data['author_name']
                author_last_name = form.cleaned_data['author_last_name']
                text_title = form.cleaned_data['text_title']
                magazine_title = form.cleaned_data['magazine_title']
                year = form.cleaned_data['year']
                magazine_number = form.cleaned_data['magazine_number']
                page = form.cleaned_data['page']
                ctx = {
                    'author_name': author_name,
                    'author_last_name': author_last_name,
                    'text_title': text_title,
                    'magazine_title': magazine_title,
                    'year': year,
                    'magazine_number': magazine_number,
                    'page': page}
                return render(request, 'daily-magazine-template.html', ctx)
        if subcategory_id == '5':
            form = PeriodicalMagazineForm(request.POST)
            if form.is_valid():
                author_name = form.cleaned_data['author_name']
                author_last_name = form.cleaned_data['author_last_name']
                text_title = form.cleaned_data['text_title']
                magazine_title = form.cleaned_data['magazine_title']
                year = form.cleaned_data['year']
                magazine_number = form.cleaned_data['magazine_number']
                page = form.cleaned_data['page']
                ctx = {
                    'author_name': author_name,
                    'author_last_name': author_last_name,
                    'text_title': text_title,
                    'magazine_title': magazine_title,
                    'year': year,
                    'magazine_number': magazine_number,
                    'page': page}
                return render(request, 'periodical-magazine-template.html', ctx)
        if subcategory_id == '6':
            form = WebArticleForm(request.POST)
            if form.is_valid():
                author_name = form.cleaned_data['author_name']
                author_last_name = form.cleaned_data['author_last_name']
                text_title = form.cleaned_data['text_title']
                web_page_name = form.cleaned_data['web_page_name']
                year = form.cleaned_data['year']
                number = form.cleaned_data['number']
                url = form.cleaned_data['url']
                access = form.cleaned_data['access']
                ctx = {
                    'author_name': author_name,
                    'author_last_name': author_last_name,
                    'text_title': text_title,
                    'web_page_name': web_page_name,
                    'year': year,
                    'number': number,
                    'url': url,
                    'access': access}
                return render(request, 'web-article-template.html', ctx)
        if subcategory_id == '7':
            form = WebPageForm(request.POST)
            if form.is_valid():
                web_page_name = form.cleaned_data['web_page_name']
                url = form.cleaned_data['url']
                access = form.cleaned_data['access']
                ctx = {
                    'web_page_name': web_page_name,
                    'url': url,
                    'access': access}
                return render(request, 'web-page-template.html', ctx)
        if subcategory_id == '8':
            form = FilmForm(request.POST)
            if form.is_valid():
                director_name = form.cleaned_data['director_name']
                film_title = form.cleaned_data['film_title']
                year = form.cleaned_data['year']
                dop_name = form.cleaned_data['dop_name']
                country = form.cleaned_data['country']
                ctx = {
                    'director_name': director_name,
                    'film_title': film_title,
                    'year': year,
                    'dop_name': dop_name,
                    'country': country}
                return render(request, 'film-template.html', ctx)
        if subcategory_id == '9':
            form = FotoForm(request.POST)
            if form.is_valid():
                foto_number = form.cleaned_data['foto_number']
                foto_description = form.cleaned_data['foto_description']
                foto_source = form.cleaned_data['foto_source']
                ctx = {
                    'foto_number': foto_number,
                    'foto_description': foto_description,
                    'foto_source': foto_source}
                return render(request, 'foto-template.html', ctx)