from flask import Flask, request as req, render_template
import service

app = Flask(__name__)

@app.route('/')
def home():
    return 'HELLO! ESTÁ É A HOME!'

@app.route('/resultado/')
def resultado():
    nota1 = req.args.get('nota1')
    nota2 = req.args.get('nota2')

    resultado = service.check_aprovacao(nota1, nota2)
    return render_template('index.html', resultado = resultado)

if __name__=='__main__':
    app.run(port=3000, debug=True)
