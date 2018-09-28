from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import View

from ..forms import PageForm

# def add_category(request):
#     form = CategoryForm()
#
#     if request.method == 'POST':
#         form = CategoryForm(request.POST)
#         if form.is_valid():
#             form.save(commit=True)
#             return HttpResponseRedirect(reverse('index'))
#
#     return render(request, 'rango/add_category.html', {'form': form})
#     # print(form)
#     # return HttpResponse('Adcionar Categoria <br/> %s' %form)

class Add_Category(View):
    form_class = PageForm
    initial = {}
    template_name = 'rango/add_category.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(reverse('index'))

        return render(request, self.template_name, {'form': form})