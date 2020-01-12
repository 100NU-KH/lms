from django.db import models
from utility.models import TimeStamp
from utility.choices import (EmploymentStatus,
							 MaritalStatus,
							 Gender,
							 EducationBackground,
							 IncomeMode,
							 AbominationStatus,
							 ApplicationStatus,)
from phone_field import PhoneField


class Application(TimeStamp):

	first_name = models.CharField(max_length=225, null=False, blank=False)
	last_name = models.CharField(max_length=225, null=False, blank=False)
	email = models.EmailField(max_length=255, unique=True)
	address = models.TextField(default='',blank=False, null=False)
	pan_card = models.CharField(max_length=10, null=False, blank=False)
	income = models.FloatField(help_text='Mention salary if employed or the ROI id self-employed')
	expected_loan_amount = models.FloatField()
	phone_num = PhoneField(max_length = 14, blank=False,null=False, unique=True, help_text='Contact phone number', default="")

	employment_status = models.CharField(max_length=50,
										choices=EmploymentStatus.CHOICES,
										null=False,
										blank=False)

	marital_status = models.CharField(max_length=50,
										choices=MaritalStatus.CHOICES,
										null=False,
										blank=False)

	gender = models.CharField(max_length=50,
										choices=Gender.CHOICES,
										null=False,
										blank=False)

	income_mode = models.CharField(max_length=50,
										choices=IncomeMode.CHOICES,
										null=False,
										blank=False)


	educational_background = models.CharField(max_length=50,
										choices=EducationBackground.CHOICES,
										null=False,
										blank=False)

	country = models.CharField(max_length=225,
										null=False,
										blank=False)

	state = models.CharField(max_length=225,
										null=False,
										blank=False)	

	pincode = models.CharField(max_length=225,
										null=False,
										blank=False)

	total_work_experience = models.CharField(max_length=225,
										null=False,
										blank=False,)

	total_monthly_emi = models.CharField(max_length=225,
										null=False,
										blank=False,)

	abomination_status = models.CharField(max_length=225,
										choices=AbominationStatus.CHOICES,
										null=False,
										blank=False,)

	duration_of_stay = models.CharField(max_length=225,
										null=False,
										blank=False,
										help_text="Duration of stay at current address(in years)")

	status = models.CharField(max_length=225,
										choices=ApplicationStatus.CHOICES,
										null=False,
										blank=False,
										default="under-process")

	class Meta:
		ordering = ('-created_at',)

	def __str__(self):
		return "Application: %(first_name)s (%(loan_amount)s)" % {"first_name" : self.first_name,
																"loan_amount" : self.expected_loan_amount, }





