from flask import Flask, render_template, request, jsonify, send_from_directory
import openai

app = Flask(__name__)

openai.api_key = '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'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/enviar_mensaje', methods=['POST'])
def enviar_mensaje():
    entrada_usuario = request.form['entrada_usuario']
    respuesta_asistente = ejecutar_comando(entrada_usuario)
    return jsonify({'respuesta': respuesta_asistente})

def ejecutar_comando(entrada_usuario):
    try:
        # Leer el historial desde el archivo
        historial = leer_historial()

        # Agregar el historial como contexto a la solicitud
        prompt = f"{historial}\nUsuario: {entrada_usuario}\nAsistente:"

        # Realizar la solicitud a GPT-3
        respuesta = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=150
        )

        return respuesta.choices[0].text.strip()
    except Exception as e:
        return f"Error al procesar la solicitud: {str(e)}"

def leer_historial():
    try:
        with open("historial_conversacion.txt", 'r') as historial_file:
            return historial_file.read()
    except FileNotFoundError:
        return ""

# Ruta estática para servir archivos en el directorio 'templates'
@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('templates', filename)

if __name__ == '__main__':
    app.run(debug=True, port=8000)