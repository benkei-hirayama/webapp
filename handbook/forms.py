from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from .models import SubjectRecords, ContentsRecords, Promise

class SubjectRecordForm(forms.ModelForm):
	class Meta:
		model = SubjectRecords
		fields = ('comp_date', 'signature')
		widgets = {
			'comp_date': AdminDateWidget(),
		}

class ContentsRecordForm(forms.ModelForm):
	class Meta:
		model = ContentsRecords
		fields = ('comp_date', 'signature')
		widgets = {
			'comp_date': AdminDateWidget(),
		}

class PromiseForm(forms.ModelForm):
	class Meta:
		model = Promise
		fields = ('promise_date',)
		widgets = {
			'promise_date': AdminDateWidget(),
		}

