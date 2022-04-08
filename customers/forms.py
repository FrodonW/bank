from django import forms

from customers.models import Profile, Loan, LoanAccept


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    email = forms.EmailField()

    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']


def form_validation_error(form):
    msg = ""
    for field in form:
        for error in field.errors:
            msg += "%s: %s \\n" % (field.label if hasattr(field, 'label') else 'Error', error)
    return msg


class LoanForm(forms.ModelForm):

    class Meta:
        model = Loan
        fields = '__all__'
        exclude = ['loaner']
        widgets = {
            'business_type': forms.Select(attrs={'class': 'custom-select md-form'}),
        }


class LoanAcceptForm(forms.ModelForm):
    class Meta:
        model = LoanAccept
        fields = '__all__'
        exclude = ['loan']


