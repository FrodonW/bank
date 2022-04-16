from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import UpdateView
from django.utils.translation import gettext_lazy as _

from customers.forms import ProfileForm, form_validation_error, LoanForm, LoanAcceptForm
from customers.models import Profile, LoanAccept


@method_decorator(login_required(login_url='login'), name='dispatch')
class ProfileView(View):
    profile = None

    def dispatch(self, request, *args, **kwargs):
        self.profile, __ = Profile.objects.get_or_create(user=request.user)
        return super(ProfileView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        context = {'profile': self.profile, 'segment': 'profile'}
        return render(request, 'customers/profile.html', context)

    def post(self, request):
        form = ProfileForm(request.POST, request.FILES, instance=self.profile)

        if form.is_valid():
            profile = form.save()
            profile.user.first_name = form.cleaned_data.get('first_name')
            profile.user.last_name = form.cleaned_data.get('last_name')
            profile.user.email = form.cleaned_data.get('email')
            profile.user.save()

            messages.success(request, 'Profile saved successfully')
        else:
            messages.error(request, form_validation_error(form))
        return redirect('profile')


def post_loan(request):
    form = LoanForm(request.POST)
    loaner_profile = request.user.profile
    if not loaner_profile.user.first_name:
        messages.error(request, 'fill you profile')
        return render(request, 'customers/profile.html')
    else:
        if request.method == 'POST':
            if form.is_valid():
                loan = form.save()
                loan.loaner = loaner_profile
                loan.save()

                messages.success(request, ' success')
    return render(request, 'customers/loan.html')


@method_decorator(staff_member_required, name='dispatch')
@method_decorator(login_required(login_url='login'), name='post')
class StaffView(SuccessMessageMixin, UpdateView):
    model = LoanAccept
    form_class = LoanAcceptForm
    template_name = 'customers/loan_accept.html'
    success_message = _('Widget was successfully updated')
    success_url = '/customers/staff/'

    def get_object(self, queryset=None):
        loans = LoanAccept.objects.filter(accept__isnull=True).first()
        return loans
