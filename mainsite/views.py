from django.db import models
from django.db.models import Prefetch
from django.shortcuts import render
from django.views import View

from mainsite.models import Student, Cat


# from mainsite.models import Student, Enrollment, Course, Lecture


# Create your views here.

class index(View):
    def get(self, request):
        thiscontext = {}
        thiscontext['students'] = Student.objects.all().order_by('firstname')
        numcats = Student.objects.annotate(num_cats=models.Count('cats'))
        thiscontext['numcats'] = numcats
        return render(request, 'mainsite/index.html',{'thiscontext':thiscontext})

class about(View):
    def get(self, request):
        context_dict = {}
        context_dict['cats'] = Cat.objects.all().order_by('cat_name')
        return render(request, 'mainsite/about.html', context=context_dict)