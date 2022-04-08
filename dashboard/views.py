from django.contrib.auth.models import User
from django.db.models import Sum
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from customers.models import LoanAccept, Loan


def dashboard(request):
    customers = User.objects.filter(is_superuser=0, is_staff=0, is_active=1)
    customers_count = customers.count()

    loan_accept = Loan.objects.filter(loanaccept__accept=True)
    loan_accept_total = loan_accept.aggregate(Sum('amount_required'))['amount_required__sum'] or 0.00

    loan__count = LoanAccept.objects.all().count()
    loan_count_accept = LoanAccept.objects.filter(accept=True).count()
    loan_count_reject = LoanAccept.objects.filter(accept=False).count()
    loan_percen_accept = ((loan_count_accept / loan__count) * 100)
    loan_percen_reject = ((loan_count_reject / loan__count) * 100)
    loan_percen_inprogress = 100 - (loan_percen_reject + loan_percen_accept)
    context = {
        'customers_count': customers_count,

        'loan_accept_total': loan_accept_total,

        'loan_percen_accept': loan_percen_accept,
        'loan_percen_reject': loan_percen_reject,
        'loan_percen_inprogress': loan_percen_inprogress,
        'loan__count': loan__count,
    }
    return render(request, 'dashboard.html', context)

