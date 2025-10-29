from pydoc import html
from flask import Flask, jsonify, render_template_string, request, redirect, url_for

app = Flask(__name__)

dispositivos_registrados = []


@app.route('/formulario', methods=['GET', 'POST'])
def agregar():
    return render_template_string('''
   <html>
   <center>
    <body style="background-color:lightblue;">
        <h1>Registrar Dispositivos</h1>
        <form method="POST" action="/agregar">
             id : <input type="text" name="id"><br>
            Nombre del Dispositivo: <input type="text" name="nombre"><br>
            Descripcion: <input type="text" name="descripcion"><br>
            Ip: <input type="text" name="ip"><br>
            MAC: <input type="text" name="mac"><br>
            Ubicacion: <input type="text" name="ubicacion"><br>
            Tipo : <input type="text" name="tipo"><br>
             Otro : <input type="text" name="otro"><br><br>
            <input type="submit" value="Registrar">
        </form>
    </body>
    </center>

   </html> 
''')


@app.route('/agregar', methods=['GET'])
def agregar_dispositivo():
    data = {
        "id": request.form['id'],
        "nombre": request.form['nombre'],
        "descripcion": request.form['descripcion'],
        "ip": request.form['ip'],
        "mac": request.form['mac'],
        "ubicacion": request.form['ubicacion'],
        "tipo": request.form['tipo'],
    }
    dispositivos_registrados.append(data)
    return redirect(url_for('mostrar_dispositivos'))







if __name__ == '__main__':
    app.run(debug=True)