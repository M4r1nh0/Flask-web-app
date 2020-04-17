
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "Minha_chave_criptografada"

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/tipoget')
def ir_get():
    return render_template('get.html')

@app.route('/tipopost')
def ir_post():
    return render_template('post.html')

@app.route('/receber/', methods=['GET','POST'])
def receber():
    if request.method == "POST":
        return u'Estou no tipo POST! <br> nome={} <br> idade={}'.format(request.form["Nome"],request.form["Idade"])
    elif request.method == "GET":
        return u'Estou no tipo GET! <br> nome={} <br> idade={}'.format(request.args.get("Nome"),request.args.get("Idade"))

@app.route('/Sessao/')
def ir_sessao():
    return render_template('sessao.html')

@app.route('/validacao/', methods=['POST'])
def validacao_sessao():
    if request.method == "POST":
        session['usuario'] = request.form['usuario']
        return redirect(url_for('restrito'))

    return redirect(url_for('ir_sessao'))

@app.route('/restrito/')
def restrito():
    if ( session['usuario'] ):
        return u"Estou na area de acesso restrito {}".format(session['usuario'])

    return redirect(url_for('ir_sessao'))
#app.route('/informacao/')
#@app.route('/informacao/<nome>')
#@app.route('/informacao/<nome>/<idade>')
#def info(nome = None,idade = None):
 #   return u'nome:{}, idade:{}'.format(nome,idade)
