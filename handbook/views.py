from django.template import loader
from django.views.generic import ListView, CreateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse
from handbook.models import Section, Category, Subject, SubjectRecords, Contents, ContentsRecords, Promise
from register.models import User
from itertools import chain
from .forms import SubjectRecordForm, ContentsRecordForm, PromiseForm

class LeaderMixin(UserPassesTestMixin):
	raise_exception = True

	def test_func(self):
		user = self.request.user
		return user.is_leader

class SubjectList(ListView):
	template_name = 'handbook/subject_list.html'
	model = Subject

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		cat_id = self.kwargs['category']
		user = self.request.user
		context['subject_list']=Subject.objects.filter(category_id=cat_id)
		if user.is_authenticated and not user.is_leader:
			context['records']=SubjectRecords.objects.filter(user_id=user.id).values_list('subject_id', flat=True)
		return context

class ContentsList(ListView):
	template_name = 'handbook/contents_list.html'
	model = Contents

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		sub_id = self.kwargs['subject']
		user = self.request.user
		context['contents_list']=Contents.objects.filter(subject_id=sub_id)
		if user.is_authenticated and not user.is_leader:
			context['complate']=SubjectRecords.objects.filter(user_id=user.id, subject_id=sub_id)
			context['records']=ContentsRecords.objects.filter(user_id=user.id)
		return context

class CourseList(LeaderMixin, ListView):
	template_name = 'handbook/course_list.html'
	model = Subject

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		userid = self.kwargs['userid']
		target = User.objects.filter(id=userid)
		if self.request.user.team_name != target[0].team_name:
			return HttpResponseForbiden()
		context['target']=target
		context['promise_1']=Promise.objects.filter(user__id=userid, chapter=1)
		context['promise_2']=Promise.objects.filter(user__id=userid, chapter=2)
		context['subject_list_1']=Subject.objects.filter(category_id=1)
		context['subject_list_2']=Subject.objects.filter(category_id=2)
		context['subject_list_3']=Subject.objects.filter(category_id=3)
		context['subject_list_4']=Subject.objects.filter(category_id=4)
		context['subject_list_5']=Subject.objects.filter(category_id=5)
		context['records']=SubjectRecords.objects.filter(user__id=userid).values_list('subject_id', flat=True)
		return context

class CourseDetail(LeaderMixin, ListView):
	template_name = 'handbook/course_detail.html'
	model = ContentsRecords

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		userid = self.kwargs['userid']
		target = User.objects.filter(id=userid)
		if self.request.user.team_name != target[0].team_name:
			return HttpResponseForbiden()
		sub_id = self.kwargs['subjectid']
		context['target']=target
		context['contents_list']=Contents.objects.filter(subject_id=sub_id)
		context['complate']=SubjectRecords.objects.filter(user__id=userid, subject_id=sub_id)
		context['records']=ContentsRecords.objects.filter(user__id=userid)
		context['reclist']=ContentsRecords.objects.filter(user__id=userid).values_list("contents", flat=True)
		return context

class SubjectRecordCreate(LeaderMixin, CreateView):
	template_name = 'handbook/subject_record_create.html'
	model = SubjectRecords
	form_class = SubjectRecordForm
	
	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.user = User.objects.get(id=self.kwargs['userid'])
		self.object.subject = Subject.objects.get(id=self.kwargs['subjectid'])
		self.object.save()
		return super().form_valid(form)

	def get_success_url(self):
		return reverse('handbook:course_detail', kwargs={'userid':self.kwargs['userid'], 'subjectid':self.kwargs['subjectid']})

class SubjectRecordDelete(LeaderMixin, DeleteView):
	model = SubjectRecords

	def get_success_url(self):
		return reverse('handbook:course_detail', kwargs={'userid':self.kwargs['userid'], 'subjectid':self.kwargs['subjectid']})

class ContentsRecordCreate(LeaderMixin, CreateView):
	template_name = 'handbook/contents_record_create.html'
	model = ContentsRecords
	form_class = ContentsRecordForm

	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.user = User.objects.get(id=self.kwargs['userid'])
		self.object.contents = Contents.objects.get(id=self.kwargs['contentsid'])
		self.object.save()
		return super().form_valid(form)

	def get_success_url(self):
		return reverse('handbook:course_detail', kwargs={'userid':self.kwargs['userid'], 'subjectid':self.kwargs['subjectid']})

class ContentsRecordDelete(LeaderMixin, DeleteView):
	model = ContentsRecords

	def get_success_url(self):
		return reverse('handbook:course_detail', kwargs={'userid':self.kwargs['userid'], 'subjectid':self.kwargs['subjectid']})

class PromiseCreate(LeaderMixin, CreateView):
	template_name = 'handbook/promise_create.html'
	model = Promise
	form_class = PromiseForm

	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.user = User.objects.get(id=self.kwargs['userid'])
		self.object.chapter = self.kwargs['chapter']
		self.object.save()
		return super().form_valid(form)

	def get_success_url(self):
		return reverse('handbook:course_list', kwargs={'userid':self.kwargs['userid']})

class PromiseDelete(LeaderMixin, DeleteView):
	model = Promise

	def get_success_url(self):
		return reverse('handbook:course_list', kwargs={'userid':self.kwargs['userid']})


