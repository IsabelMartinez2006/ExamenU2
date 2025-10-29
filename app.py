from flask import Flask, jsonify, render_template_string, request, redirect, url_for

app = Flask(__name__)

dispositivos_registrados = []


@app.route('/formulario', methods=['GET'])
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
            <input type="submit" value="agregar">
        </form>
    </body>
    </center>

   </html> 
''')


@app.route('/agregar', methods=['POST'])
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



@app.route('/dispositivos', methods=['GET'])
def mostrar_dispositivos():
    html = ""
    for d in dispositivos_registrados:
        html += f"""
        <div name="dispositivo" style="border:1px solid black; padding:10px; margin:10px; background-color:lightblue;">
            <strong>{d['id']}</strong><br>
            <b>Nombre:</b> {d['nombre']}<br>
            <b>IP:</b> {d['descripcion']}<br>
            <b>MAC:</b> {d['ip']}<br>
            <b>Ubicacion:</b> {d['mac']}<br>
            <b>Tipo:</b> {d['ubicacion']}<br>
            <b>Otro:</b> {d['tipo']}<br><br>

        </div>
        """

    return render_template_string(f"""
    <html>
    <head><title>Dispositivos</title></head>
    <body>
        <h1>Lista de Dispositivos</h1>
 
        {html}
    </body>
    </html>
    """)

@app.route('/actualizardisp', methods=['PUT'])
def actualizar_dispositivo():
    data = request.get_json()
    dispositivo_id = data.get('id')

    html = ""
    html += f"""
           <form method="POST" action="/agregar">
             id : <input type="text" name="id"><br>
            
        </form>
        """


    for dispositivo in dispositivos_registrados:
        if dispositivo['id'] == dispositivo_id:
            dispositivo.update(data)
            return jsonify({"message": "Dispositivo actualizado", "dispositivo": dispositivo}), 200

    return jsonify({"message": "Dispositivo no encontrado"})





if __name__ == '__main__':
    app.run(debug=True)