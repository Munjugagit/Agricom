from django.urls import path
from reporter.views import HomePageView

urlpatterns = [
    path('index/', HomePageView.as_view()),
]