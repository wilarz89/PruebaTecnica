from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from primera.models import Modelo
from primera.utils import mostCommon
import reportlab
from reportlab.pdfgen import canvas
from django.http import HttpResponse



def index(request):

    return render(request, 'primera/primera.html', )


@csrf_exempt
def persist(request):
            #persist input/output to  database
    entrada=request.POST.get('entrada',None)
    salida=str(mostCommon(entrada))
    Modelo(entrada=entrada,salida=salida).save()
    contexto = {
        'input':entrada, 'output':salida
    }
    return render(request,'primera/resultados.html',context=contexto)

def generate_pdf(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="pruebaTecnica2017.pdf"'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response

''' def ConsultarBaseDatos(request):
    modelos = []
    for modelos in Modelo.objects.all():
        modelos.append(modelos)
    context = {'modelos': modelos}
    return render(request, 'primera/resultados.html', context)'''