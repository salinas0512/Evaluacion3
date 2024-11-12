from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def home(): return render_template('index.html')


# Ejercicio 1
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    resultado = None
    # Inicializar valores
    nota1 = request.form.get('nota1', '')
    nota2 = request.form.get('nota2', '')
    nota3 = request.form.get('nota3', '')
    asistencia = request.form.get('asistencia', '')

    if request.method == 'POST':
        # Campos del formulario
        dato1 = int(request.form['nota1'])
        dato2 = int(request.form['nota2'])
        dato3 = int(request.form['nota3'])
        dato4 = int(request.form['asistencia'])
        # Promedio de notas
        promedio = (dato1 + dato2 + dato3) / 3
        asistencia = dato4
        if promedio >= 40 and asistencia >= 75:
            resultado = f"Su promedio de notas es: {int(promedio)} <br><br>APROBADO"
        else:
            resultado = f"Su promedio de notas es: {int(promedio)} <br><br>REPROBADO"
    return render_template('ejercicio1.html',
                           resultado=resultado, nota1=nota1, nota2=nota2, nota3=nota3, asistencia=asistencia)


# Ejercicio 2
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    resultado = None
    nombre1 = request.form.get('nombre1', '')
    nombre2 = request.form.get('nombre2', '')
    nombre3 = request.form.get('nombre3', '')
    if request.method == 'POST':
        # Campos del formulario
        nombre1 = (request.form['nombre1'])
        nombre2 = (request.form['nombre2'])
        nombre3 = (request.form['nombre3'])
        nombre_mas_largo = max(nombre1, nombre2, nombre3, key=len)
        if len(nombre1) == len(nombre2) == len(nombre3):
            # Si tienen la misma longitud, devolver todos los nombres
            resultado = (f"Los tres nombres tienen la misma cantidad de caracteres ({len(nombre1)})"
                         f":{nombre1}, "
                         f"{nombre2}, "
                         f"{nombre3}.")
        else:
            resultado = (f"El nombre con mayor cantidad de carácteres es: {nombre_mas_largo}<br><br>"
                         f" El nombre contiene: {len(nombre_mas_largo)} caracteres.")
    return render_template('ejercicio2.html', resultado=resultado, nombre1=nombre1,
                           nombre2=nombre2,
                           nombre3=nombre3)


if __name__ == '__main__':
    app.run(debug=True)
