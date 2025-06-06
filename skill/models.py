from django.db import models
from django.db.models import F
from multiselectfield import MultiSelectField

def validate_skill(value):
    if value > 5 or value < 1:
        return False
    return True

class SkillMode(models.TextChoices):
    SOFT = "SOFT", "SOFT"
    HARD = 'HARD', "HARD"

class Skill(models.Model):

    title = models.CharField(
        max_length=100,
        verbose_name="Title", help_text="SKill Title", blank=False, null=False)
    display_title = models.BooleanField(
        default=False,
        verbose_name="Display Title", help_text="Should we display the skill title ?",
    )

    mode = models.CharField(
        max_length=64,
        verbose_name="Skill Mode", help_text="Is the Skill a hard skill or a soft skill", 
        blank=False, null=False, choices=SkillMode, default=SkillMode.HARD)
    
    description = models.TextField(
        max_length=4096,
        verbose_name="Header", help_text="Skill Header", blank=True, null=False)
    tips = models.TextField(
        max_length=4096,
        verbose_name="Tips", help_text="Skill Tips", blank=True, null=False)
    example = models.TextField(
        max_length=4096,
        verbose_name="Example", help_text="Skill Example", blank=True, null=False)

    color= models.CharField(
        max_length=6,
        verbose_name="Color", help_text="Skill Color for Banner", blank=True, null=False)


    level = models.SmallIntegerField(verbose_name="Level", help_text="SKill Level", default=1, validators=[validate_skill])
    icon = models.FileField(upload_to="skill_icon", verbose_name="Icon", help_text="Icon of the skill", null=True)
    banner = models.FileField(upload_to="skill_banner", verbose_name="Banner", help_text="Banner Image of the skill", null=True)

    def experiences(self):
        from experience.models import ExperienceSkill
        return ExperienceSkill.objects.filter(skill__id=self.id).select_related('experience').values(
            experience_ref=F('experience__id'), 
            job_title=F('experience__job_title'),
            contract_type=F('experience__contract_type'),
            company_name=F('experience__company_name'),
            start_date=F('experience__start_date'),
            )

    def skill__id(self):
        return self.pk
    
    def skill__icon(self):
        return str(self.icon)

    def __str__ (self):
        return "Skill - [{}]".format(self.title)
        
class SkillSection(models.Model):

    text = models.CharField(
        max_length=8192,
        verbose_name="Text", help_text="Skill Section Text", blank=False, null=False)
    
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, verbose_name="Skill", help_text="The Skill associated with the section")

    def __str__ (self):
        return "Section[{}] - {}".format(self.id, str(self.skill))