from django.shortcuts import render
from .models import Blocks 
from django.core.paginator import Paginator, EmptyPage
# импорт модели Artists

def BlocksView(request):
    database = Blocks.objects.all()

    p = Paginator(database, 50)

    page_num = request.GET.get('page', 1)

    try:
    	blocks = p.page(page_num)
    except EmptyPage:
    	blocks = p.page(1)
    return render(request, "blocks.html", locals())


def BlockView(request, height):
	block = Blocks.objects.get(height=height)
	return render(request, "block.html", locals())