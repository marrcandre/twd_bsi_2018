from django.shortcuts import render
from .models import Category

def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    # print('Categorias: ', len(category_list), ':', category_list)

    context_dict = {'categories':category_list}
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    context_dict = {'autor': 'Marco André Mendes'}
    return render(request, 'rango/about.html', context=context_dict)
