from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from ..forms import CategoryForm

def add_category(request):
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(reverse('index'))

    return render(request, 'rango/add_category.html', {'form': form})
    # print(form)
    # return HttpResponse('Adcionar Categoria <br/> %s' %form)