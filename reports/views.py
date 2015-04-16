from django.shortcuts import render
from extractor.processor import Processor
# Create your views here.


def index(request):
    processor = Processor()
    formatted_rows = processor.format()
    header = formatted_rows[0]
    formatted_rows = formatted_rows[1:]
    # context = {'latest_question_list': 'latest_question_list'}
    return render(request, 'reports/index.html', locals())
