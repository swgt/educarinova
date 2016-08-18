from django import template
register = template.Library()

@register.filter(name='getObj')
def getObj(list, id):
    for obj in list:
    	if (str(obj['id']) == str(id)):
    		return obj

@register.filter		
def getValueTuitionFee(list, id):
	for obj in list:
		if (str(obj['id']) == str(id)):
			return obj['valueTuitionFee']

@register.filter		
def getVacancies(list, id):
	for obj in list:
		if (str(obj['id']) == str(id)):
			return obj['vacancies']

@register.filter		
def getMessage(list, id):
	for obj in list:
		if (str(obj['id']) == str(id)):
			return obj['message']