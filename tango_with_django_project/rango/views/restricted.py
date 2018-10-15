from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


@login_required
def restricted(request):
    return HttpResponse("Página restrita. Como você está autenticado, consegue ver esse texto!")