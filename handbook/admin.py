from django.contrib import admin
from handbook.models import Section, Category, Subject, Contents, SubjectRecords, ContentsRecords, Promise

class SectionAdmin(admin.ModelAdmin):
	list_display = ('id', 'section_name')
	list_display_links = ('id', 'section_name')


admin.site.register(Section, SectionAdmin)


class CategoryAdmin(admin.ModelAdmin):
	list_display = ('id', 'category_name')
	list_display_links = ('id', 'category_name')


admin.site.register(Category, CategoryAdmin)


class SubjectAdmin(admin.ModelAdmin):
	list_display = ('id', 'category', 'subject_name', 'contents_count')
	list_display_links = ('id', 'subject_name')


admin.site.register(Subject, SubjectAdmin)


class SubjectRecordsAdmin(admin.ModelAdmin):
	list_display = ('user', 'subject', 'comp_date', 'signature')
	list_display_links = ('user','subject')


admin.site.register(SubjectRecords, SubjectRecordsAdmin)


class ContentsAdmin(admin.ModelAdmin):
	list_display = ('id', 'subject','chapter', 'clause', 'sections', 'document')
	list_display_links = ('id','document')


admin.site.register(Contents, ContentsAdmin)


class ContentsRecordsAdmin(admin.ModelAdmin):
	list_display = ('user', 'contents', 'comp_date', 'signature')
	list_display_links = ('user','contents')


admin.site.register(ContentsRecords, ContentsRecordsAdmin)


class PromiseAdmin(admin.ModelAdmin):
	list_display = ('user', 'chapter', 'promise_date')
	list_display_linke = ('user', 'chapter')


admin.site.register(Promise, PromiseAdmin)


