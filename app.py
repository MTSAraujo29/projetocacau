from flask import Flask, render_template

app = Flask(__name__)

import os

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/galeria')
def galeria():
    # Caminho completo para a pasta static/img
    caminho_imagens = os.path.join(app.static_folder, 'img')
    
    # Lista de todos os arquivos na pasta img
    imagens = [img for img in os.listdir(caminho_imagens) if img.endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    
    return render_template('galeria.html', imagens=imagens)


@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')


if __name__ == '__main__':
    app.run(debug=True)
