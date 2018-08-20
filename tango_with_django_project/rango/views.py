from django.http import HttpResponse

def index(request):

    texto = '''
    <h1> Rango </h1>
    Essa é a página principal do Rango
    
    <br/><a href='/rango/about/'>Sobre o rango</a>
    '''
    return HttpResponse(texto)


def about(request):
    texto = '''
    <h1> Sobre o Rango </h1>
    Essa é a página sobre o Rango.

    <br/><a href='/rango/'>Index</a>
    '''
    return HttpResponse(texto)

