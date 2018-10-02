from django import forms


class Less3AuthorsForm(forms.Form):
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
    page = forms.IntegerField(label="Numer/numery stron", required=False)

