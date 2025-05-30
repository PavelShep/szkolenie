from django.db import models

class Category(models.Model):
    publish = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Course(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    publish = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    hours = models.IntegerField()
    code = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title
