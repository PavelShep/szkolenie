from django.db import models
from oferta_panel.models import Course

class Registration(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    rodo_agreement = models.BooleanField()
    status = models.CharField(max_length=50)
    registration_date = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
