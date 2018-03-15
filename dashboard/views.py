from django.shortcuts import render

from api.models import Salary

# Create your views here.
def index(request):
    all_salary_list = Salary.objects.all()
    context = {'all_salary_list': all_salary_list}
    return render(request, 'dashboard/index.html', context)

def detail(request, year):
    return HttpResponse("You're looking at dashboard %s." % year)
