from django.urls import path
from api import views

urlpatterns = [
    path('branches/autocomplete', views.BranchesAutocompleteView.as_view(), name='bank-details'),
    path('branches', views.BranchesView.as_view(), name='bank-details'),
]