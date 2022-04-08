from django.urls import path
from customers import views
from customers.views import post_loan, StaffView

urlpatterns = [
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('staff/',  StaffView.as_view(), name='staff'),
    path('loan', post_loan, name='loan'),
]
