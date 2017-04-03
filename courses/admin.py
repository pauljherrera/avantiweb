from django.contrib import admin
from .models import Subject, Course, Module, Questions

# Register your models here.
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
	list_display = ['title', 'slug']
	prepopulated_fields = {'slug': ('title',)}


class ModuleInline(admin.StackedInline):
	model = Module


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
	list_display = ['title', 'subject', 'created']
	list_filter = ['created', 'subject']
	search_fields = ['title', 'overview']
	prepopulated_fields = {'slug': ('title',)}
	inlines = [ModuleInline]

@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
	list_display = ['owner', 'created', 'answered', 'question']
	list_filter = ['answered', 'created']