from django.db import models


class CategoryModel(models.Model):
    class Meta:
        db_table = "my_category"

    name = models.CharField(max_length=20, null=False)
    menu = models.CharField(max_length=20, null=False)


class DrinkModel(models.Model):
    class Meta:
        db_table = "my_drink"

    name = models.CharField(max_length=20, null=False)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    nutrition = models.CharField(max_length=256, default='')
    allergy = models.DateTimeField(auto_now_add=True)



