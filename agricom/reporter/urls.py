from django.urls import path
from reporter.views import HomePageView, county_datasets, incidences_points

urlpatterns = [
    path('index/', HomePageView.as_view(), name = 'home'),
    path('county_data/', county_datasets, name = 'county'),
    path('incidences_data/', incidences_points, name = 'incidences'),
] 