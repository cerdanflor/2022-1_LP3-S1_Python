from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Articulo

# Create your views here.
layout = """
    <h1> Proyecto Web (LP3) | Flor Cerdán </h1>
    <hr/>
    <ul>
        <li>
            <a href="/inicio"> Inicio</a>
        </li>
        <li>
            <a href="/saludo"> Mensaje de saludo</a>
        </li>
        <li>
            <a href="/rango"> Mostrar Números [a,b]</a>
        </li>
        <li>
            <a href="/rango2/10/15"> Mostrar Números [10,15]</a>
        </li>
    </ul>
    <hr/>

"""
def index(request):
    estudiantes = ['Luis Serna',
                   'Antony Ccaccya',
                   'Miguel Yauricasa',
                   'Carlos Granados']
 
    return render(request,'index.html', {
        'titulo':'Inicio',
        'mensaje':'Proyecto Web con DJango',
        'estudiantes': estudiantes
    })

def saludo(request):
    return render(request,'saludo.html',{
         'titulo': 'Saludo',
         'autor_saludo':'Mg. Flor Elizabeth Cerdán León'
    })
       
def rango(request):
    a = 10
    b = 20
    rango_numeros = range(a, b+1)
    return render(request,'rango.html', {
        'titulo':'Rango',
        'a':a,
        'b':b,
        'rango_numeros': rango_numeros
    })
    resultado = f"""
        <h2> Numéros de [{a},{b}] </h2>
        Resultado: <br>
        <ul>
    """
    while a<=b:
        resultado+= f"<li> {a} </li>"
        a+=1
    resultado += "</ul>"
    return HttpResponse(layout + resultado)

def rango2(request,a=0,b=100):
    if a>b:
        return redirect('rango2', a=b, b=a)
    resultado = f"""
        <h2> Números de [{a}, {b}]</h2>
    
    """
    while a<=b:
        resultado += f"<li> {a} </li>"
        a+=1
    resultado += "</ul"
    return HttpResponse(layout + resultado)
def crear_articulo(request):
    articulo = Articulo(
        titulo = "Tendencias Covid con Power BI",
        contenido = "El articulo muestra información de....",
        publicado = True
    )
    articulo.save()
    return HttpResponse(f"Articulo Creado: {articulo.titulo} - {articulo.contenido}")
