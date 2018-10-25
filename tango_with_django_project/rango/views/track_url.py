from django.core.urlresolvers import reverse
from django.shortcuts import redirect

from ..models import Page


def track_url(request):
    page_id = None
    url = reverse('index')
    if request.method == 'GET':
        if 'page_id' in request.GET:
            page_id = request.GET['page_id']
            try:
                page = Page.objects.get(id=page_id)
                print(page.url, page.views)
                page.views += 1
                page.save()
                url = page.url
            except Page.DoesNotExist:
                print("Não achou: %s" %page_id)

    return redirect(url)