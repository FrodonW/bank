from django.urls import path
from customers import views
from dashboard.views import dashboard, chart, table, customer_dashboard

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('chart', chart, name='chart'),
    path('table', table, name='table'),

    path('<int:pk>', customer_dashboard, name='c_dashboard'),
]
