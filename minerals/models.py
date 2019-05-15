from django.db import models


class Mineral(models.Model):
    name = models.CharField(max_length=250, blank=True)
    image_filename = models.CharField(max_length=250, blank=True)
    image_caption = models.CharField(max_length=250, blank=True)
    category = models.CharField(max_length=250, blank=True)
    formula = models.CharField(max_length=250, blank=True)
    strunz_classification = models.CharField(max_length=250, blank=True)
    color = models.CharField(max_length=250, blank=True)
    crystal_system = models.CharField(max_length=250, blank=True)
    unit_cell = models.CharField(max_length=250, blank=True)
    crystal = models.CharField(max_length=250, blank=True)
    symmetry = models.CharField(max_length=250, blank=True)
    cleavage = models.CharField(max_length=250, blank=True)
    mohs_scale_hardness = models.CharField(max_length=250, blank=True)
    luster = models.CharField(max_length=250, blank=True)
    streak = models.CharField(max_length=250, blank=True)
    diaphaneity = models.CharField(max_length=250, blank=True)
    optical_properties = models.CharField(max_length=250, blank=True)
    refractive_index = models.CharField(max_length=250, blank=True)
    crystal_habit = models.CharField(max_length=250, blank=True)
    specific_gravity = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.name

