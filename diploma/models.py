from django.db import models

# Create your models here.
class Diploma(models.Model):

    title = models.CharField(
        max_length=100,
        verbose_name="Title", help_text="Title", blank=False, null=False)
    
    description = models.TextField(
        max_length=512,
        verbose_name="Description", help_text="Description", blank=False, null=False)
    
    date = models.DateField(verbose_name="Date", help_text="Date")

    def __str__ (self):
        return "Diploma - [{}]".format(self.title)