from django.db import models

class Formularze(models.Model):
    form_name = models.CharField(max_length=255)
    attr_name = models.CharField(max_length=255)
    attr_value = models.CharField(max_length=255)
    position = models.IntegerField(default=0)

    class Meta:
        db_table = 'formularze'
        unique_together = ('form_name', 'attr_name')
        indexes = [
            models.Index(fields=['form_name', 'position']),
        ]

    def __str__(self):
        return f"{self.form_name} - {self.attr_name}"

class Szablony(models.Model):
    template_name = models.CharField(max_length=255, unique=True)
    template_text = models.TextField()

    class Meta:
        db_table = 'szablony'

    def __str__(self):
        return self.template_name