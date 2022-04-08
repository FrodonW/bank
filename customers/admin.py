from django.contrib import admin

from customers.models import Profile, Loan, LoanAccept

admin.site.register(Profile)
admin.site.register(Loan)
admin.site.register(LoanAccept)
