
from django.template import loader
from django.http import HttpResponse

def members(request):
    # members = Member.objects.all()
    template = loader.get_template('home.html')
    return HttpResponse(template.render())
    

def details(request):
    template = loader.get_template('detail.html')
    return HttpResponse(template.render())
    

def add_member(request):
    if request.method == 'POST':
        pass


def del_member(request):
    if request.method == 'DELETE':
        pass


def modify_member(request):
    if request.method == 'PATCH':
        pass

