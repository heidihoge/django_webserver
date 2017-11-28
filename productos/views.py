from crudbuilder.views import ViewBuilder
from productos.cruds import CategoriaCrud,ProductoCrud

from django.http import HttpResponse
from django.db.utils import OperationalError
from reportlab.pdfgen import canvas

try:
    builder = ViewBuilder('productos', 'producto', ProductoCrud)
    builder.generate_crud()
    builder = ViewBuilder('productos', 'categoria', CategoriaCrud)
    builder.generate_crud()
except OperationalError:
    pass # happens when db doesn't exist yet, views.py should be
         # importable without this side effect



def report(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reporte_productos.pdf"'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Reporte productos")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response