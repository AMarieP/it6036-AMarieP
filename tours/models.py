from django.db import models
from django.urls import reverse
from django.conf import settings #imports my custom user model

class Tour(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    author = models.ForeignKey(
      settings.AUTH_USER_MODEL,
      on_delete=models.CASCADE
    )

    def __str__(self):  
        return self.name

    def get_absolute_url(self):
        return reverse("tour_detail", kwargs={'pk': self.pk})