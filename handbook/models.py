from django.db import models
from django.contrib.auth import get_user_model

class Section(models.Model):
	section_name = models.CharField(max_length=255,unique=True, verbose_name='部門')
	def __str__(self):
		return self.section_name
	class Meta:
		db_table = "promotion_section"
		verbose_name = '部門'
		verbose_name_plural = '部門'

class Category(models.Model):
	category_name = models.CharField(max_length=255,unique=True, verbose_name='種別')
	def __str__(self):
		return self.category_name
	class Meta:
		db_table = "promotion_category"
		verbose_name = 'カテゴリ'
		verbose_name_plural = 'カテゴリ'

class Subject(models.Model):
	section_from = models.IntegerField(verbose_name='部門from')
	section_to = models.IntegerField(verbose_name='部門to')
	category = models.ForeignKey(Category, on_delete = models.CASCADE, verbose_name='種別')
	subject_name  = models.CharField(max_length=255, verbose_name='名前')
	subject_image = models.ImageField(upload_to='static/handbook/img/', blank=True, null=True, verbose_name='画像')
	contents_count = models.IntegerField(verbose_name='細目数')
	def __str__(self):
		return self.subject_name
	class Meta:
		db_table = "promotion_subject"
		verbose_name = '課目'
		verbose_name_plural = '課目'

class SubjectRecords(models.Model):
	user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='ユーザ')
	subject = models.ForeignKey(Subject, on_delete = models.PROTECT, verbose_name='修得課目', related_name='subject_record')
	comp_date = models.DateField(verbose_name='修了日')
	signature = models.CharField(max_length=255, verbose_name='サイン')
	def __str__(self):
		return self.signature
	class Meta:
		db_table = "promotion_subject_records"
		verbose_name = '課目記録'
		verbose_name_plural = '課目記録'
		constraints = [
			models.UniqueConstraint(
				fields=["user","subject"],
				name="subject_records_unique"
			),
		]

class Contents(models.Model):
	subject = models.ForeignKey(Subject, on_delete = models.CASCADE, verbose_name='名前')
	chapter = models.IntegerField(verbose_name='章')
	chapter_title = models.CharField(max_length=255, blank=True, null=True, verbose_name='章タイトル')
	clause = models.IntegerField(verbose_name='節')
	clause_title = models.CharField(max_length=255, blank=True, null=True, verbose_name='節タイトル')
	sections = models.IntegerField(verbose_name='項')
	document = models.TextField(verbose_name='内容')
	def __str__(self):
		return self.document
	class Meta:
		db_table = "promotion_contents"
		verbose_name = '細目'
		verbose_name_plural = '細目'

class ContentsRecords(models.Model):
	user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='ユーザ')
	contents = models.ForeignKey(Contents, on_delete = models.PROTECT, verbose_name='細目', related_name='contents_record')
	comp_date = models.DateField(verbose_name='修了日')
	signature = models.CharField(max_length=255, verbose_name='サイン')
	def __str__(self):
		return self.signature
	class Meta:
		db_table = "promotion_contents_records"
		verbose_name = '細目記録'
		verbose_name_plural = '細目記録'
		constraints = [
			models.UniqueConstraint(
				fields=["user","contents"],
				name="contents_records_unique"
			),
		]

class Promise(models.Model):
	user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='名前')
	chapter = models.IntegerField(verbose_name='種別')
	promise_date = models.DateField(verbose_name='約束した日')
	def __str__(self):
		return self.user.email
	class Meta:
		db_table = "promotion_promise"
		verbose_name = '約束'
		verbose_name_plural = '約束'
		constraints = [
			models.UniqueConstraint(
				fields=["user","chapter"],
				name="promise_unique"
			),
		]

