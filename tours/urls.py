from django.urls import path
from .views import TourView, TourListView, AgentView, AgentListView

urlpatterns = [
    path("tours", TourListView.as_view(), name="tours"),
    path("tour/<int:pk>/", TourView.as_view(), name="tour_detail"),
    path("agents", AgentListView.as_view(), name="agents"),
    path("agent/<int:pk>/", AgentView.as_view(), name="agent_detail"),
]