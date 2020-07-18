from django.db import models
from django.db.models import F
from django.urls import reverse

class Neighborhood_org(models.Model):

    name = models.CharField(max_length=255)
    org_type = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    boundary = models.CharField(max_length=255)
    website = models.CharField(max_length=255, null=True, blank=True, default=None)
    facebook = models.CharField(max_length=255, null=True, blank=True, default=None)
    notes = models.CharField(max_length=255, null=True, blank=True, default=None)
    location = models.CharField(max_length=255, null=True, blank=True, default=None)
    time = models.CharField(max_length=255, null=True, blank=True, default=None)
    day = models.CharField(max_length=255, null=True, blank=True, default=None)
    week = models.CharField(max_length=255, null=True, blank=True, default=None)
    frequency = models.CharField(max_length=255, null=True, blank=True, default=None)
    last_updated = models.DateField(null=True, blank=True, default=None)
    is_active = models.BooleanField()
    district = models.IntegerField()

    class Meta:
        verbose_name = ("Neighborhood")
        verbose_name_plural = ("Neighborhoods")

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse("success", kwargs={"pk": self.pk})