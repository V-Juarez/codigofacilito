from flask import Flask, render_template


app = Flask(__name__)

"""
@app.route('/')
def index():
  return "CodigoFacilito"
"""

def index():
  # return render_template('index.html', titulo='Index')
  data={
    'titulo':'Index',
    'encabezado':'Bienvenidos(a)'
  }
  return render_template('index.html', data=data)
  #return "Bienvenidos a CodigoFacilito"

@app.route('/contacto')
def contacto():
  data={
    'titulo':'Contacto',
    'encabezado':'Bienvenidos(a)'
  }
  return render_template('contacto.html', data=data)

@app.route('/holaMundo')
def hola_mundo():
  return "Hola Mundo! Desde codigofacilito"

if __name__ == '__main__':
  app.add_url_rule('/',view_func=index)
  app.run(debug=True, port=5005)

