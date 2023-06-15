from django.urls import path
from handbook import views

app_name = 'handbook'

urlpatterns = [
	path('subject/<int:category>/', views.SubjectList.as_view(), name='subject_list'),
	path('contents/<int:subject>/', views.ContentsList.as_view(), name='contents_list'),
	path('course/<int:userid>/', views.CourseList.as_view(), name='course_list'),
	path('course/<int:userid>/promise/<int:chapter>/create/', views.PromiseCreate.as_view(), name='promise_create'),
	path('course/<int:userid>/promise/<int:chapter>/delete/<int:pk>/', views.PromiseDelete.as_view(), name='promise_delete'),
	path('course/<int:userid>/subject/<int:subjectid>/', views.CourseDetail.as_view(), name='course_detail'),
	path('course/<int:userid>/subject/<int:subjectid>/create/', views.SubjectRecordCreate.as_view(), name='subject_create'),
	path('course/<int:userid>/subject/<int:subjectid>/delete/<int:pk>/', views.SubjectRecordDelete.as_view(), name='subject_delete'),
	path('course/<int:userid>/subject/<int:subjectid>/contents/<int:contentsid>/create/', views.ContentsRecordCreate.as_view(), name='contents_create'),
	path('course/<int:userid>/subject/<int:subjectid>/contents/<int:contentsid>/delete/<int:pk>/', views.ContentsRecordDelete.as_view(), name='contents_delete'),
]


