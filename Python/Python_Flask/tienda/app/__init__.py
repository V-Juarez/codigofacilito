from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    # return 'Hola mundo!!! CodigoFacilito'
@app.route('/login')
def login():
    return render_template('auth/login.html')

@app.errorhandler(404)
def pagina_no_encontrada(error):
    return render_template('errores/404.html'), 404


def inicializar_app(config):
    app.config.from_object(config)
    app.register_error_handler(404, pagina_no_encontrada)
    return app

