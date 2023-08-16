from django.urls import path
from .views import TourView, TourListView

urlpatterns = [
    path("tours", TourListView.as_view(), name="tours"),
    path("tour/<int:pk>/", TourView.as_view(), name="tour_detail")
]