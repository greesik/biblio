from django import forms


class Less3AuthorsForm(forms.Form): #formularz do prac, które mają maksymalnie 3 autorów
    author1_name = forms.CharField(label="Imię autora", max_length=64, required=True)
    author1_last_name = forms.CharField(label="Nazwisko autora", max_length=64, required=True)
    author2_name = forms.CharField(label="Imię drugiego autora", max_length=64, required=False)
    author2_last_name = forms.CharField(label="Nazwisko drugiego autora", max_length=64, required=False)
    author3_name = forms.CharField(label="Imię trzeciego autora", max_length=64, required=False)
    author3_last_name = forms.CharField(label="Nazwisko trzeciego autora", max_length=64, required=False)
    title = forms.CharField(label="Tytuł", max_length=256, required=True)
    translator_name = forms.CharField(label="Imię tłumacza", max_length=64, required=False)
    translator_last_name = forms.CharField(label="Nazwisko tłumacza", max_length=64, required=False)
    city = forms.CharField(label="Miasto wydania", max_length=64, required=False)
    year = forms.IntegerField(label="Rok wydania", max_value=9999, required=False)
    volume = forms.IntegerField(label="Numer tomu", required=False)
    page = forms.CharField(label="Numer/numery stron", required=True)


class More3AuthorsForm(forms.Form): #formularz do prac, które mają ponad 3 autorów
    editor1_name = forms.CharField(label="Imię redaktora", max_length=64, required=True)
    editor1_last_name = forms.CharField(label="Nazwisko redaktora", max_length=64, required=True)
    editor2_name = forms.CharField(label="Imię drugiego redaktora", max_length=64, required=False)
    editor2_last_name = forms.CharField(label="Nazwisko drugiego redaktora", max_length=64, required=False)
    title = forms.CharField(label="Tytuł", max_length=256, required=True)
    translator_name = forms.CharField(label="Imię tłumacza", max_length=64, required=False)
    translator_last_name = forms.CharField(label="Nazwisko tłumacza", max_length=64, required=False)
    city = forms.CharField(label="Miasto wydania", max_length=64, required=False)
    year = forms.IntegerField(label="Rok wydania", max_value=9999, required=False)
    volume = forms.IntegerField(label="Numer tomu", required=False)
    page = forms.CharField(label="Numer/numery stron", required=True)


class CompositeWorkForm(forms.Form): # formularz do prac, które są opracowaniami złożonymi z prac różnych autorów
    author_name = forms.CharField(label="Imię autora", max_length=64, required=True)
    author_last_name = forms.CharField(label="Nazwisko autora", max_length=64, required=True)
    text_title = forms.CharField(label="Tytuł artykułu", max_length=256, required=True)
    editor_name = forms.CharField(label="Imię redaktora wydania", max_length=64, required=True)
    editor_last_name = forms.CharField(label="Nazwisko redaktora wydania", max_length=64, required=True)
    book_title = forms.CharField(label="Tytuł zbioru", max_length=256, required=True)
    translator_name = forms.CharField(label="Imię tłumacza", max_length=64, required=False)
    translator_last_name = forms.CharField(label="Nazwisko tłumacza", max_length=64, required=False)
    city = forms.CharField(label="Miasto wydania", max_length=64, required=False)
    year = forms.IntegerField(label="Rok wydania", max_value=9999, required=False)
    page = forms.CharField(label="Numer/numery stron", required=True)


class DailyMagazineForm(forms.Form): # formularz do czasopisma codziennego lub tygodnika
    author_name = forms.CharField(label="Imię autora", max_length=64, required=True)
    author_last_name = forms.CharField(label="Nazwisko autora", max_length=64, required=True)
    text_title = forms.CharField(label="Tytuł artykułu", max_length=256, required=True)
    magazine_title = forms.CharField(label="Tytuł czasopisma", max_length=256, required=True)
    year = forms.CharField(label="Dokładna data wydania", required=False, widget=forms.TextInput(
        attrs={'placeholder':'np. 21 grudnia 2012'}))
    magazine_number = forms.IntegerField(label="Numer wydania", required=False)
    page = forms.CharField(label="Numer/numery stron", required=True)


class PeriodicalMagazineForm(forms.Form): # formularz do periodyków
    author_name = forms.CharField(label="Imię autora", max_length=64, required=True)
    author_last_name = forms.CharField(label="Nazwisko autora", max_length=64, required=True)
    text_title = forms.CharField(label="Tytuł artykułu", max_length=256, required=True)
    magazine_title = forms.CharField(label="Tytuł czasopisma", max_length=256, required=True)
    year = forms.IntegerField(label="Rok wydania", max_value=9999, required=False)
    magazine_number = forms.IntegerField(label="Numer wydania", required=False)
    page = forms.CharField(label="Numer/numery stron", required=True)


class WebArticleForm(forms.Form):
    author_name = forms.CharField(label="Imię autora", max_length=64, required=True)
    author_last_name = forms.CharField(label="Nazwisko autora lub nick", max_length=64, required=True)
    text_title = forms.CharField(label="Tytuł artykułu", max_length=256, required=True)
    web_page_name = forms.CharField(label="Nazwa portalu", max_length=256, required=True)
    number = forms.IntegerField(label="Numer wydania", min_value=1, required=False)
    url = forms.URLField(label="Adres strony", required=True, initial="http://")
    access = forms.CharField(label="Data dostępu", max_length=64, required=True, widget=forms.TextInput(
        attrs={'placeholder':'Format dd.mm.rrrr'}))
    year = forms.IntegerField(label="Rok publikacji artykułu", min_value=1999, max_value=9999, required=True)


class WebPageForm(forms.Form):
    web_page_name = forms.CharField(label="Nazwa portalu", max_length=256, required=True)
    url = forms.URLField(label="Adres strony", required=True, initial="http://")
    access = forms.CharField(label="Data dostępu", max_length=64, required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Format dd.mm.rrrr'}))


class FilmForm(forms.Form):
    film_title = forms.CharField(label="Tytuł filmu", max_length=128, required=True)
    director_name = forms.CharField(label="Imię i nazwisko reżysera", max_length=128, required=True)
    dop_name = forms.CharField(label="Imię i nazwisko autora zdjęć", required=False)
    year = forms.IntegerField(label="Rok", min_value=1895, max_value=9999, required=False)
    country = forms.CharField(label="Kraj produkcji", max_length=64, required=False)


class FotoForm(forms.Form):
    foto_number = forms.IntegerField(label="Numer zdjęcia", min_value=1, required=True)
    foto_description = forms.CharField(label="Opis zdjęcia", max_length=128, required=True)
    foto_source = forms.CharField(label="Źródło zdjęcia", max_length=255, required=False)


