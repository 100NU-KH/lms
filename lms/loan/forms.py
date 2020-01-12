from django import forms
from .models import Application

class ApplicationForm(forms.ModelForm):
	class Meta:
		model = Application
		fields = '__all__'
		exclude = ('status',)

	def __init__(self, *args, **kwargs):
		super(ApplicationForm, self).__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs.update({
				'id': field,
				'class' : 'form-control'
			})

class ApplicationEditForm(forms.ModelForm):
	class Meta:
		model = Application
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super(ApplicationEditForm, self).__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs.update({
				'id': field,
				'class' : 'form-control'
			})

class ApplicationSearchForm(forms.Form):
	country = forms.CharField(max_length=25, required=False, label='Country')
	email = forms.CharField(max_length=225, required=False, label='Email')
	status = forms.CharField(max_length=225, required=False, label='Status')

	def __init__(self, *args, **kwargs):
		super(ApplicationSearchForm, self).__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs.update({
				'id': field,
				'class' : 'form-control'
			})

	def clean(self):
		cleaned_data = super(ApplicationSearchForm, self).clean()
		cleaned_data['country'] = cleaned_data['country'].strip()
		cleaned_data['email'] = cleaned_data['email'].strip()
		cleaned_data['status'] = cleaned_data['status'].strip()
		return cleaned_data