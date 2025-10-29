from pydoc import html
from flask import Flask, jsonify, render_template_string, request, redirect, url_for

app = Flask(__name__)

# Lista para almacenar los dispositivos
dispositivos_registrados = []


@app.route('/formulario', methods=['GET', 'POST'])
def agregar():
    return render_template_string('''
   <html>
   <center>
    <body style="background-color:lightblue;">
        <h1>Registrar Dispositivos</h1>
        <form method="POST" action="/formulario">
             Id : <input type="text" name="id"><br>
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






















@app.route('/formulario')
def formulario():
    print("mensaje ")
    dispositivos_registrados.append("leandro calderon") #añadir un nuevo elemento
    
    n1=10
    n2=100
    n3=100
    #html="<h6>"+dispositivos_registrados[0]+"</h6>"#mostrar lo que esta en esa lista en esa posicuion
    html="<h6>"+str((n1+n2)/n3)+"</h6>"
    html += "<br>"
    html += "<div style='background-color:green; color:white; height:300 px '>"+dispositivos_registrados[0]+"</div>"
    
    return html
    #str(dispositivos_registrados[0])#retornar en string 
  

if __name__ == '__main__':
    app.run(debug=True)