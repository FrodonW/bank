from django.urls import path
from customers import views
from dashboard.views import dashboard, chart

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('chart', chart, name='chart'),


]
