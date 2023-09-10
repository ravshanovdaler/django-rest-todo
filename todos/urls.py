from django.urls import path
from .views import ListCreatePlan,DetailPlan


urlpatterns = [
    path('', ListCreatePlan.as_view()),
    path('<int:pk>/', DetailPlan.as_view())
]
