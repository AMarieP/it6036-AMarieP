from django.db import models
from django.urls import reverse
from django.conf import settings #imports my custom user model

class Agent(models.Model):
  agent = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='agent')

  def __str__(self):  
      return self.agent.username

  def get_absolute_url(self):
        return reverse("agent_detail", kwargs={'pk': self.pk})

class Tour(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    author = models.ForeignKey(
      Agent,
      on_delete=models.PROTECT,
      related_name='author'
    )

    def __str__(self):  
        return self.name

    def get_absolute_url(self):
        return reverse("tour_detail", kwargs={'pk': self.pk})

