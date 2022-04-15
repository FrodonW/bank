import datetime

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core import serializers
from django.db.models import Sum
from django.db.models.functions import ExtractMonth
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import json

# Create your views here.
from django.template import loader, Context
from django.utils.decorators import method_decorator
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


@login_required()
@staff_member_required()
def chart(request):
    total = LoanAccept.total_by_month()
    labels = [i['month'] for i in total]
    data = [i['count'] for i in total]
    context = {
        'labels': labels,
        'data': data,
    }
    return JsonResponse(context)


@login_required()
@staff_member_required()
def table(request):
    data = Profile.get_profile()
    return JsonResponse({'data': list(data)})

# customer dashboard


def customer_dashboard(request, pk):
    template_name = loader.get_template('dashboard_customer.html')

    loan_count = Loan.total_infor(pk)['loan_count']
    total_amount_required = Loan.total_infor(pk)['total_amount_required']

    context = {
        'loan_count': loan_count,
        'total_amount_required': total_amount_required,
    }
    return HttpResponse(template_name.render(context, request))
