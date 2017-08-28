from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from primera.models import Modelo
from primera.utils import mostCommon



def index(request):

    return render(request, 'primera/primera.html', )


@csrf_exempt
def persist(request):
            #persist input/output to  database
    entrada=request.POST.get('entrada',None)
    salida=str(mostCommon(entrada))
    Modelo(entrada=entrada,salida=salida).save()
    return render(request,'primera/resultados.html')


def ConsultarBaseDatos(request):
    modelos = []
    for modelos in Modelo.objects.all():
        modelos.append(modelos)
    context = {'modelos': modelos}
    return render(request, 'primera/resultados.html', context)