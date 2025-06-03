from django.db import models

# Create your models here.
class Hobby(models.Model):

    title = models.CharField(
        max_length=100,
        verbose_name="Title", help_text="Title", blank=False, null=False)
    
    description = models.TextField(
        max_length=4096,
        verbose_name="Description", help_text="Description", blank=False, null=False)
    
    banner = models.FileField(upload_to="hobby_banner", verbose_name="Banner", help_text="Banner Image of the hobby", null=True)

    def images(self):
        return HobbyImage.objects.filter(hobby__id=self.pk).values('title', 'file')
    
    def __str__ (self):
        return "Hobby - [{}]".format(self.title)
    


        
class HobbyImage(models.Model):

    title = models.CharField(
        max_length=100,
        verbose_name="Titre", help_text="Le titre de l'image", blank=False, null=False)
    file = models.FileField(upload_to="hobby_image", verbose_name="Image liée a mon hobby", help_text="Une Image Associée à mon hobby", null=True)
    hobby = models.ForeignKey(Hobby, on_delete=models.CASCADE, verbose_name="Hobby", help_text="Le hobby associé à l'image")

    def __str__ (self):
        return self.hobby.title + " - " + self.title