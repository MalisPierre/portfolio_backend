from django.db import models

class Skill(models.Model):

    title = models.CharField(
        max_length=100,
        verbose_name="Title", help_text="SKill Title", blank=False, null=False)
    
    header = models.TextField(
        max_length=4096,
        verbose_name="Header", help_text="Skill Header", blank=False, null=False)
    
    def __str__ (self):
        return "Skill - [{}]".format(self.title)
        
class SkillSection(models.Model):

    text = models.CharField(
        max_length=8192,
        verbose_name="Text", help_text="Skill Section Text", blank=False, null=False)
    
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, verbose_name="Skill", help_text="The Skill associated with the section")

    def __str__ (self):
        return "Section[{}] - {}".format(self.id, str(self.skill))