from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, letter
import os

def extendpdf (path,path2,path3,path4, font, yea):
    """ fgag gffgad"""
    ancho, alto=A4        # ancho y alto de la pagina, en dinA4, es una tupla en puntos (un punto=1/72 pulgadas)
    archivo='../presentacion/Pipeline Project {}-2014.pdf'.format(yea)
    c=canvas.Canvas('../presentacion/Pipeline Project {}-2014.pdf'.format(yea), pagesize=A4)  # genera el archivo pdf vacio, con tamaño dinA4
    c.setStrokeColorRGB(0.7, 0.7, 0.7)
    c.setStrokeColorRGB(0.7, 0.7, 0.7)
    c.setFont("{}-Bold".format(font), 24)
    c.drawString(150, alto-50, "Pipelines Project Ironhack")    # escribe con margen de 50 puntos
    c.setFont('{}-BoldOblique'.format(font), 10)
    c.drawString(20, 20, "Data Bootcamp 06/19")
    c.drawRightString(ancho-30, 20, "Javier Molins Jiménez")
    c.setFont("{}-Bold".format(font), 20)
    c.drawCentredString(round(ancho/2), alto-80, "Suicides between {}-2014".format(yea))
    c.drawImage("../presentacion/logo-ironhack-madrid.jpg", 0, alto-100, width=100, height=100)
    c.drawImage("../presentacion/descarga.png", ancho-100, alto-100, width=75, height=75)
    x=0
    y=alto-100
    c.setLineWidth(3)
    c.setStrokeGray(0)
    c.line(x, y, ancho, y)
    c.setFont('Times-Roman', 12)
    c.drawString(100, alto-155, " In the following graph you can observe the evolution of suicides versus the ")
    c.drawString(100, alto-168, " evolution of the GDP per capita:")
    c.drawImage(path3, 70, alto - 440, width=450, height=250)
    c.drawString(100, alto-480, " In the following graph you can observe the top 10 countries by suicide rate:")
    c.drawImage(path4, 70, alto - 750, width=450, height=250)
    c.setLineWidth(1)
    #c.line(0, 50, ancho, 50)
    c.setFont('{}-Bold'.format(font), 10)
    c.drawCentredString(round(ancho/2), 20, "1/2")
    c.showPage()

    c.setFont("{}-Bold".format(font), 24)
    c.drawCentredString(round(ancho/2), alto-50, "Pipelines Project Ironhack")    # escribe con margen de 50 puntos
    c.setFont('{}-BoldOblique'.format(font), 10)
    c.drawString(20, 20, "Data Bootcamp 06/19")
    c.drawRightString(ancho-30, 20, "Javier Molins Jiménez")
    c.setFont("{}-Bold".format(font), 20)
    c.drawCentredString(round(ancho/2), alto-80, "Suicides between {}-2014".format(yea))
    c.drawImage("../presentacion/logo-ironhack-madrid.jpg", 0, alto-100, width=100, height=100)
    c.drawImage("../presentacion/descarga.png", ancho-100, alto-100, width=75, height=75)
    x=0
    y=alto-100
    c.setLineWidth(3)
    c.setStrokeGray(0)
    c.line(x, y, ancho, y)
    c.setFont('Times-Roman', 12)
    c.drawString(100, alto-122, "Here are the birth years for each generation:")
    c.setFont('Times-Bold', 12)
    c.drawString(120, alto-135, " - Generation Z:")
    c.setFont('Times-Roman', 12)
    c.drawString(200, alto-135, " Born 1996 – TBD.")
    c.setFont('Times-Bold', 12)
    c.drawString(120, alto-148, " - Millennials:")
    c.setFont('Times-Roman', 12)
    c.drawString(191, alto-148, " Born 1977 – 1995.")
    c.setFont('Times-Bold', 12)
    c.drawString(120, alto-161, " - Generation X:")
    c.setFont('Times-Roman', 12)
    c.drawString(205, alto-161, " Born 1965 – 1976.")
    c.setFont('Times-Bold', 12)
    c.drawString(120, alto-174, " - Baby Boomers:")
    c.setFont('Times-Roman', 12)
    c.drawString(210, alto-174, " Born 1946 – 1964.")
    c.setFont('Times-Bold', 12)
    c.drawString(120, alto-187, " - Silent Generation:")
    c.setFont('Times-Roman', 12)
    c.drawString(225, alto-187, " Born 1945 and before.")
    c.drawString(100, alto-210, " In the following graph you can observe the suicides rate per generation:")
    c.drawImage(path, 0, alto - 500, width= 650, height=280)
    c.setFont('Times-Roman', 12)
    c.drawString(100, alto-500, " In the following graph you can observe the suicides rate per continent:")
    c.drawImage(path2, 0, alto - 810, width= 650, height=300)
    c.setLineWidth(1)
    #c.line(0, 50, ancho, 50)
    c.setFont('{}-Bold'.format(font), 10)
    c.drawCentredString(round(ancho/2), 20, "2/2")
    c.showPage()             # fin o cambio de pagina (se pierden los estilos)
    c.save()
    return archivo


def shortpdf (path,path2,path3,path4, font, yea):
    ancho, alto=A4        # ancho y alto de la pagina, en dinA4, es una tupla en puntos (un punto=1/72 pulgadas)
    archivo='../presentacion/Pipeline Project {}-2014.pdf'.format(yea)
    c=canvas.Canvas('../presentacion/Pipeline Project {}-2014.pdf'.format(yea), pagesize=A4)  # genera el archivo pdf vacio, con tamaño dinA4
    c.setStrokeColorRGB(0.7, 0.7, 0.7)
    c.setStrokeColorRGB(0.7, 0.7, 0.7)
    c.setFont("{}-Bold".format(font), 24)
    c.drawString(150, alto-50, "Pipelines Project Ironhack")    # escribe con margen de 50 puntos
    c.setFont('{}-BoldOblique'.format(font), 10)
    c.drawString(20, 20, "Data Bootcamp 06/19")
    c.drawRightString(ancho-30, 20, "Javier Molins Jiménez")
    c.setFont("{}-Bold".format(font), 20)
    c.drawCentredString(round(ancho/2), alto-80, "Suicides between {}-2014".format(yea))
    c.drawImage("../presentacion/logo-ironhack-madrid.jpg", 0, alto-100, width=100, height=100)
    c.drawImage("../presentacion/descarga.png", ancho-100, alto-100, width=75, height=75)
    x=0
    y=alto-100
    c.setLineWidth(3)
    c.setStrokeGray(0)
    c.line(x, y, ancho, y)
    c.setFont('Times-Roman', 12)
    c.drawString(100, alto-155, " In the following graph you can observe the evolution of suicides versus the ")
    c.drawString(100, alto-168, " evolution of the GDP per capita:")
    c.drawImage(path3, 70, alto - 440, width=450, height=250)
    c.drawString(100, alto-480, " In the following graph you can observe the top 10 countries by suicide rate:")
    c.drawImage(path4, 70, alto - 750, width=450, height=250)
    c.setLineWidth(1)
    #c.line(0, 50, ancho, 50)
    c.setFont('{}-Bold'.format(font), 10)
    c.drawCentredString(round(ancho/2), 20, "1/1")
    c.showPage()
    c.save()
    return archivo



def pdf(p,p2,p3,p4,f,y,t):
    if t=='s':
        archivo = shortpdf(p,p2,p3,p4,f,y)
    else:
        archivo= extendpdf(p,p2,p3,p4,f,y)
    return archivo

