from django.shortcuts import render

# Create your views here.


def index(request):
    context = {'latest_question_list': 'latest_question_list'}
    return render(request, 'reports/index.html', context)
