from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, letter
import os
def generatePDF(path, font):
    ancho, alto=A4        # ancho y alto de la pagina, en dinA4, es una tupla en puntos (un punto=1/72 pulgadas)
    c=canvas.Canvas(path, pagesize=A4)  # genera el archivo pdf vacio, con tamaño dinA4
    #c.setFillColorRGB(0, 0, 0)
    c.setStrokeColorRGB(0.7, 0.7, 0.7)
    c.setFont("{}-Bold".format(font), 24)
    #c.roundRect(240, alto - 55, 200, 20, 10)
    c.drawString(150, alto-50, "Pipelines Project Ironhack")    # escribe con margen de 50 puntos
    c.setFont(font, 12)
    c.drawString(ancho -145, alto-80, "Data Bootcamp 06/19")
    c.drawString(ancho -100, alto-90, "Javier Molins")
    c.setFont("{}-Bold".format(font), 20)
    c.drawString(250, alto-80, "Suicides")
    c.drawImage("../presentacion/logo-ironhack-madrid.jpg", 0, alto-100, width=100, height=100)
    x=0
    y=alto-100
    c.setLineWidth(3)
    c.setStrokeGray(0)
    c.line(x, y, ancho, y)
    c.drawImage("../presentacion/SuicidesGenerationSex.png", 0, alto - 450, width=550, height=300)
    c.showPage()             # fin o cambio de pagina (se pierden los estilos)
    c.setStrokeColorRGB(0.7, 0.7, 0.7)
    c.setFont("{}-Bold".format(font), 24)
    c.drawString(150, alto-50, "Pipelines Project Ironhack")    # escribe con margen de 50 puntos
    c.setFont(font, 12)
    c.drawString(ancho -145, alto-80, "Data Bootcamp 06/19")
    c.drawString(ancho -100, alto-90, "Javier Molins")
    c.setFont("{}-Bold".format(font), 20)
    c.drawString(250, alto-80, "Suicides")
    c.drawImage("../presentacion/logo-ironhack-madrid.jpg", 0, alto-100, width=100, height=100)
    x=0
    y=alto-100
    c.setLineWidth(3)
    c.setStrokeGray(0)
    c.line(x, y, ancho, y)
    c.showPage()
    c.save()
    return path