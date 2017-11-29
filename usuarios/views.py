from crudbuilder.views import ViewBuilder
from usuarios.cruds import UsuarioCrud
from django.db.utils import OperationalError
from django.http import HttpResponse
from crudbuilder.views import ViewBuilder
from django.db.utils import OperationalError
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER,TA_LEFT
from usuarios.models import Usuarios
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, cm
from django.http import HttpResponse
from datetime import datetime
try:
    builder = ViewBuilder('usuarios', 'usuarios', UsuarioCrud)
    builder.generate_crud()
except OperationalError:
    pass # happens when db doesn't exist yet, views.py should be
         # importable without this side effect



def report(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=reporte_clientes.pdf'

    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)

    x = datetime.now()
# Header
    c.setLineWidth(.3)
    c.setFont('Helvetica', 22)
    c.drawString(30, 780, 'Reporte')
    c.setFont('Helvetica', 22)
    c.drawString(45, 750, 'Clientes')
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
    nombre_usuario = Paragraph('cliente', styleBH)
    correo_electronico = Paragraph('contacto', styleBH)
    data = [[nombre_usuario, correo_electronico]]

    #productosTable
    #productos = [Producto.nombre_producto, Producto.descripcion, Producto.precio]
    usuarios = map(lambda x: [x.nombre_usuario, x.correo_electronico], Usuarios.objects.all())
    styles = getSampleStyleSheet()
    styleN = styles["BodyText"]

    styleN.fontSize = 10

    width, height = A4
    high = 600
    for cliente in usuarios:
        data.append(cliente)


    # tablesize
    table = Table(data, colWidths=[8 * cm,  5 * cm])
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