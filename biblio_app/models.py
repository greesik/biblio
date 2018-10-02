from django.db import models


class MainCategory(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=255)
    form_name = models.CharField(max_length=64)
    main_cat = models.ForeignKey(MainCategory, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s %s" % (self.name, self.form_name, self.main_cat)

