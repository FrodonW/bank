from django.urls import path
from customers import views
from dashboard.views import dashboard, chart, table, customer_dashboard, customer_table

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('chart', chart, name='chart'),
    path('table', table, name='table'),

    path('<int:pk>', customer_dashboard, name='c_dashboard'),
    path('<int:pk>/c_table', customer_table, name='c_table'),
]
