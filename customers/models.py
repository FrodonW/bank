from itertools import count
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum, Count, Max, DateField, CharField
from django.db.models.functions import TruncMonth, ExtractMonth
from django.templatetags.static import static
from django.utils.translation import gettext as _


class Profile(models.Model):
    GENDER_MALE = 1
    GENDER_FEMALE = 2
    GENDER_CHOICES = [
        (GENDER_MALE, _("Male")),
        (GENDER_FEMALE, _("Female")),
    ]

    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="customers/profiles/avatars/", null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICES, null=True, blank=True)
    phone = models.CharField(max_length=32, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')

    @property
    def get_avatar(self):
        return self.avatar.url if self.avatar else static('assets/img/team/default-profile-picture.png')

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

    @classmethod
    def get_profile(cls):
        return cls.objects.filter(birthday__isnull=False). \
            values('id', "user__first_name", "user__last_name", "birthday", "gender",
                   "phone", "address", "city").order_by('created_at')


class Loan(models.Model):
    BUSINESS_TYPES = (
        ('', 'Choose...'),
        ('FT', 'Food Truck'),
        ('CON', 'Construction'),
        ('OTH', 'Other')
    )
    loaner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    amount_required = models.IntegerField(null=True)  # label = 'Amount required'
    business_type = models.CharField(max_length=50, choices=BUSINESS_TYPES, null=True)
    years_in_business = models.IntegerField(null=True)  # label='Years in business'
    other = models.CharField(max_length=64, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super(Loan, self).save(*args, **kwargs)
        self.save_to_loan_accept()

    def save_to_loan_accept(self):
        staff_accept, _ = LoanAccept.objects.update_or_create(
            loan=self
        )

    def __str__(self):
        return str(self.loaner)

    @staticmethod
    def get_loan(pk):
        return Loan.objects.filter(loaner=pk).values('amount_required', 'business_type',
                                                     'years_in_business', 'other', 'created_at')

    @staticmethod
    def total_infor(pk):
        return Loan.objects.filter(loaner=pk).aggregate(total_amount_required=Sum('amount_required'),
                                                        loan_count=Count('id'))


class LoanAccept(models.Model):
    loan = models.OneToOneField(Loan, null=True, on_delete=models.CASCADE)
    accept = models.BooleanField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.loan)

    @staticmethod
    def total(boolean):
        obj = LoanAccept.objects.filter(accept=boolean).aggregate(count=Count('id'))

        return obj['count']

    @classmethod
    def total_by_month(cls):
        return cls.objects.annotate(month=TruncMonth('created_at')).values('month').annotate(count=Count('id')).values(
            'month', 'count').order_by()
