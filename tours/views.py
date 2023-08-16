from django.views.generic import ListView, DetailView
from .models import Tour

class TourListView(ListView):
    model = Tour
    template_name = "tours/tourlist.html"

class TourView(DetailView):
    template_name = "tours/tour.html"
