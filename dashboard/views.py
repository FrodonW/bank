import datetime

from django.contrib.auth.models import User
from django.db.models import Sum
from django.db.models.functions import ExtractMonth
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import json

# Create your views here.
from django.template import loader, Context
from django.views.generic import TemplateView

from customers.models import LoanAccept, Loan, Profile


def dashboard(request):
    template_name = loader.get_template('dashboard.html')

    total_loan = LoanAccept.total('')
    loan_percen_accept = (total_loan and (LoanAccept.total(True) / total_loan * 100)) or 0
    loan_percen_reject = (total_loan and (LoanAccept.total(False) / total_loan * 100)) or 0

    customers_count = User.objects.filter(is_superuser=0, is_staff=0, is_active=1).count()

    context = {
        'customers_count': customers_count,
        'loan_percen_accept': loan_percen_accept,
        'loan_percen_reject': loan_percen_reject,
        'loan_percen_inprogress': 100 - loan_percen_reject - loan_percen_accept,

    }

    return HttpResponse(template_name.render(context, request))


def chart(request):
    # labels = ['thang 1']
    data1 = []
    total = LoanAccept.total_by_month()
    labels = [i['month'] for i in total]
    data = [i['count'] for i in total]
    context = {
        'labels': labels,
        'data': data,
    }
    return JsonResponse(context)


def table(request):
    data = Profile.get_profile()
    return JsonResponse({'data': data})