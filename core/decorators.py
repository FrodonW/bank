from customers.models import Profile
from django.core.exceptions import PermissionDenied
from functools import wraps


# check_form = LoginForm(request.POST)
# email = check_form.cleaned_data['email']
# customer_profile = Profile.objects.filter(email=email)
# if customer_profile.DoesNotExist:
#     messages.error(request, 'complete your profile before submit a loan')
#     return render(request, 'customers/profile.html')

# def profile_require(function):
#     @wraps(function)
#     def wrap(request, *args, **kwargs):
#         profile = request.profile
#         if profile.DoesNotExist:
#             return

