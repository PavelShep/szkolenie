from django.db import models

class IssueReport(models.Model):
    report_date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)
    subject = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.subject
