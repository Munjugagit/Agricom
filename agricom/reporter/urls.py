from django.urls import path
from reporter.views import HomePageView, county_datasets

urlpatterns = [
    path('index/', HomePageView.as_view(), name = 'home'),
    path('county_data/', county_datasets, name = 'county'),
    path('incidence_data/', HomePageView.as_view(), name = 'home'),
] 