from django.contrib import admin
from .models import Post,Question,Choice


# Register your models here.


class Posta(admin.ModelAdmin):

	admin.site.site_header = "Djangocombo Project"
	list_display = ('author','title','created_date')
	list_filter = ('title', )
	search_fields = ['published_date ']

admin.site.register(Post, Posta)



class Choicea(admin.TabularInline):
	
	model = Choice
	extra = 3


class QuestionAdmin(admin.ModelAdmin):
	 

	 fieldsets = [
	 	(None,				{'fields': ['question_text']}),
	 	('Date information',{'fields': ['pub_date'], 'classes':['collapse']}),
	 ]
	 inlines = [Choicea]
	 list_display = ('question_text', 'pub_date', 'was_published_recently')
	 list_filter = ['pub_date']
	 search_fields = ['question_text']

admin.site.register(Question,QuestionAdmin)