from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Exercício 1 & 2
    nome = "Carlos"
    idade = 17
    
    # Exercício 3
    usuario = {
        "nome": "Ana",
        "email": "ana@email.com"
    }
    
    # Exercício 4
    alunos = ["Ana", "Bruno", "Gabriel", "Mariana", "Beatriz"]
    
    # Exercício 5
    nota = 8.5
    
    return render_template(
        'index.html', 
        nome=nome, 
        idade=idade, 
        usuario=usuario, 
        alunos=alunos, 
        nota=nota
    )

if __name__ == '__main__':
    app.run(debug=True)
