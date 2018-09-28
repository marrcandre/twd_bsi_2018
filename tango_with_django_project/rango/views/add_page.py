from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import View
from ..forms import PageForm
from ..models import Category

class Add_Page(View):
    form_class = PageForm
    initial = {}
    template_name = 'rango/add_page.html'

    def get(self, request, category_name_slug=None):
        try:
            category = Category.objects.get(slug=category_name_slug)
        except Category.DoesNotExist:
            category = None

        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form, 'category':category})

    def post(self, request,  category_name_slug=None):
        try:
            category = Category.objects.get(slug=category_name_slug)
        except Category.DoesNotExist:
            category = None

        form = self.form_class(request.POST)
        if form.is_valid():
            if category:
                page = form.save(commit=False)
                page.category = category
                page.views = 0
                page.save()
                return HttpResponseRedirect(reverse('show_category', args=(category_name_slug,)))

        return render(request, self.template_name, {'form': form, 'category':category})

# def add_page(request, category_name_slug):
#     try:
#         category = Category.objects.get(slug=category_name_slug)
#     except Category.DoesNotExist:
#         category = None
#
#     if request.method != 'POST':
#         form = PageForm()
#     else:
#         form = PageForm(request.POST)
#         if form.is_valid():
#             if category:
#                 page = form.save(commit=False)
#                 page.category = category
#                 page.views = 0
#                 page.save()
#                 return HttpResponseRedirect(reverse('show_category', args=(category_name_slug,)))
#                 # return show_category(request, category_name_slug)
#             else:
#                 print(form.errors)
#
#     context_dict = {'form': form, 'category': category}
#
#     return render(request, 'rango/add_page.html', context_dict)
