from django.urls import path
from customers import views
from dashboard.views import dashboard

urlpatterns = [
    path('', dashboard, name='dashboard'),
]
