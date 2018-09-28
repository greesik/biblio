from django.db import models


class MainCategory(models.Model):
    name = models.CharField(max_length=128)


class SubCategory(models.Model):
    name = models.CharField(max_length=255)
    form_name = models.CharField(max_length=64)
    main_cat_id = models.ForeignKey(MainCategory, on_delete=models.CASCADE)