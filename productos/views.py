from crudbuilder.views import ViewBuilder
from productos.cruds import CategoriaCrud,ProductoCrud
from django.db.utils import OperationalError
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER,TA_LEFT
from productos.models import Producto
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, cm
from django.http import HttpResponse
from datetime import datetime

try:
    builder = ViewBuilder('productos', 'producto', ProductoCrud)
    builder.generate_crud()
    builder = ViewBuilder('productos', 'categoria', CategoriaCrud)
    builder.generate_crud()
except OperationalError:
    pass # happens when db doesn't exist yet, views.py should be
         # importable without this side effect


def report(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=reporte_productos.pdf'

    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)

    x = datetime.now()
# Header
    c.setLineWidth(.3)
    c.setFont('Helvetica', 22)
    c.drawString(30, 780, 'Reporte')
    c.setFont('Helvetica', 22)
    c.drawString(45, 750, 'Productos')
    c.setFont('Helvetica-Bold', 12)
    c.drawString(200, 750, 'Fecha: ' + str(x.day) + '/' + str(x.month) + '/' + str(x.year))
    c.line(200, 747,747, 747)
    # drawImage(archivo, x, y, width=None, height=None)
    c.drawImage("https://www.lomejordelbarrio.com/images/sized/images/imagenes/acdelicutcakes-talleresreposteria-santander-logo-800x533.jpg", 400,600,width=200, height=200)

    # TableHeader
    styles = getSampleStyleSheet()
    styleBH = styles["Normal"]
    styleBH.alignment = TA_LEFT
    styleBH.fontSize = 11
    producto = Paragraph('producto', styleBH)
    precio = Paragraph('precio', styleBH)
    data = [[producto, precio]]

    #productosTable
    #productos = [Producto.nombre_producto, Producto.descripcion, Producto.precio]
    productos = map(lambda x: [x.nombre_producto, x.precio], Producto.objects.all())
    styles = getSampleStyleSheet()
    styleN = styles["BodyText"]

    styleN.fontSize = 10

    width, height = A4
    high = 600
    for producto in productos:
        data.append(producto)


    # tablesize
    table = Table(data, colWidths=[10 * cm,  1.5 * cm])
    table.setStyle(TableStyle([
        ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.blueviolet),
        ('BOX', (0, 0), (-1, -1), 0.25, colors.black), ]))

    # pdfsize
    table.wrapOn(c, width, height)
    table.drawOn(c, 30, high)
    c.showPage()

    c.save()
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response