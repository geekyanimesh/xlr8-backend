from django.urls import path
from . import views

urlpatterns = [
    path('submit-lead/', views.submit_lead, name='submit_lead'),
]