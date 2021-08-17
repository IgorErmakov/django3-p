from django.shortcuts import render
from .models import Project

# class Home:
    # def as_view():
        # return HttpResponse('yesss')

def home(request):

    projects = Project.objects.all()

    return render(
        request,
        'portfolio/home.html',
        {'projects': projects}
    )
