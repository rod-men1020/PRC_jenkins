from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "¡Hola desde Docker! - Rodrigo Mendoza - 20001083"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)