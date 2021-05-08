from flask import Flask, render_template, request


app = Flask(__name__)

@app.before_request
def before_request():
  print('Antes de la peticion...')


@app.after_request
def after_request(response):
  print('Despues de la peticion...')
  return response


"""
@app.route('/')
def index():
  return "CodigoFacilito"
"""

def index():
  print('Estamos accediendo a la peticion...')
  # return render_template('index.html', titulo='Index')
  data={
    'titulo':'Index',
    'encabezado':'Bienvenidos(a)'
  }
  return render_template('index.html', data=data)
  #return "Bienvenidos a CodigoFacilito"

@app.route('/saludo/<nombre>')
def saludo(nombre):
  # return 'Hola, Codi!!!'
  return 'Hola, {O}!'.format(nombre)

@app.route('/suma/<int:valor1>/<int:valor2>')
def suma(valor1,valor2):
  return 'La suma es: {0}'.format((valor1 + valor2))



@app.route('/lenguajes')
def lenguajes():
  data={
    'hay_lenguajes': True,
    'lenguajes':['PHP', 'Python', 'Kotlin', 'Rust', 'Java', 'C#', 'JavaScript']
  }
  return render_template('lenguajes.html', data=data)


@app.route('/contacto')
def contacto():
  data={
    'titulo':'Contacto',
    'encabezado':'Bienvenidos(a)'
  }
  return render_template('contacto.html', data=data)

@app.route('/datos')
def datos():
  print(request.args)
  # valor1=request.args.get('valor1')
  a = request.args.get('valor1')
  b = int(request.args.get('valor2'))
  return 'Estos son los datos: {0}, {1}'.format(a, (b+15))

@app.route('/holaMundo')
def hola_mundo():
  return "Hola Mundo! Desde codigofacilito"

if __name__ == '__main__':
  app.add_url_rule('/',view_func=index)
  app.run(debug=True, port=5005)

