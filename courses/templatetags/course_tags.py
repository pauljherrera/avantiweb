from django import template

register = template.Library()

@register.filter
def model_name(obj):
	try:
		return obj._meta.model_name
	except AttributeError:
		return None

@register.filter
def filter_course_id(obj, filter_):
	return obj.filter(course_id=filter_)