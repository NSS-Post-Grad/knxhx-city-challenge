from django.db import models
from django.db.models import F
from django.urls import reverse
from .neighborhood_org import Neighborhood_org

class Resident(models.Model):

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    organization_position = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.IntegerField()
    zip_code = models.IntegerField()
    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255, null=True, blank=True, default=None)
    city_state = models.CharField(max_length=255, null=True, blank=True, default=None)
    is_subscribed = models.BooleanField()
    neighborhood_org_id = models.ForeignKey(Neighborhood_org, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Resident")
        verbose_name_plural = ("Residents")

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse("success", kwargs={"pk": self.pk})