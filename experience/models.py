from django.db import models
from multiselectfield import MultiSelectField
from django.db.models import F

class ContractType(models.TextChoices):
    CDI = "CDI", "CDI"
    INTERNSHIP = 'INTERNSHIP', "Stage"

class Experience(models.Model):

    job_title = models.CharField(
        max_length=100,
        verbose_name="Job Title", help_text="Job Title", blank=False, null=False)
    
    contract_type = models.CharField(
        choices= ContractType, max_length=20,
        verbose_name="Contract Type", help_text="The Type of the Contract signed", blank=False, null=False, default=ContractType.CDI)
    
    company_name = models.CharField(
        max_length=100,
        verbose_name="Company Name", help_text="Company Name", blank=False, null=False)

    localisation = models.CharField(
        max_length=100,
        verbose_name="Company Localisation", help_text="Company Localisation", blank=False, null=False, default="France")
    
    description = models.TextField(
        max_length=2048,
        verbose_name="Description", help_text="Description", blank=False, null=False)
    
    start_date = models.DateField(verbose_name="Start Date", help_text="Start Date")
    end_date = models.DateField(verbose_name="End Date", help_text="End Date")

    banner = models.FileField(upload_to="experience_banner", verbose_name="Banner", help_text="Banner Image of the experience", null=True)

    def skills(self):   
        return ExperienceSkill.objects.filter(experience__id=self.id).select_related('skill').values(skill__id=F('skill__id'), title=F('skill__title'), icon=F('skill__icon'), level=F('skill__level'))

    def tasks(self):
        return ExperienceTask.objects.filter(experience__id=self.pk).values('id', 'description', 'tooltip').order_by('-importance')
    
    def __str__ (self):
        return "Experience - [{}] - [{}]".format(self.job_title, self.company_name)

    
class ExperienceSkill(models.Model):
    from skill.models import Skill

    experience = models.ForeignKey(Experience, on_delete=models.CASCADE, verbose_name="Experience", help_text="Experience")
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, verbose_name="Skill", help_text="Skill")

    def __str__ (self):
        return self.experience.company_name + " - " + self.skill.title

class ExperienceTask(models.Model):
    from skill.models import Skill

    description = models.TextField(
        max_length=124,
        verbose_name="Description", help_text="Experience Description", blank=False, null=False)
    
    tooltip = models.TextField(
        max_length=512,
        verbose_name="Tooltip HelpText", help_text="Tooltip HelpText", blank=False, null=False)
    
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE, 
        verbose_name="Experience", help_text="Experience")
    
    skills = models.ManyToManyField(Skill, 
        verbose_name="Skills", help_text="Skills")

    importance = models.IntegerField(
        default=0,
        verbose_name="Level of Importance", help_text="How important was this task and should it be displayed on top or bottom of the list ?",
    )

    def __str__ (self):
        return self.description