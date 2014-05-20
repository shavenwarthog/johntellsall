from django.template.response import TemplateResponse


def allstuff(request):
    return TemplateResponse(request, 'allstuff.html')
