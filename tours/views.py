from django.views.generic import ListView, DetailView
from .models import Tour, Agent

class TourListView(ListView):
    model = Tour
    template_name = "tours/tourlist.html"

class TourView(DetailView):
    template_name = "tours/tour.html"

class AgentListView(ListView):
    model = Agent
    template_name = "tours/tourlist.html"

class AgentView(DetailView):
    template_name = "tours/tour.html"
