from flask import Flask

app = Flask(__name__)


@app.route("/decorator")
def explicar_decorator():
    texto_explicativo = """
 <h2>Conceito de Decorator em Python</h2>
 
 <b>1. O que é um decorator em Python?</b>
 Um decorator é uma função que recebe outra função como argumento e estende o seu 
 comportamento sem modificá-la explicitamente. É uma forma elegante de 'envelopar' 
 uma função.

 <b>2. Para que ele serve?</b>
 Serve para separar preocupações no código. Ele permite adicionar funcionalidades 
 extras (como logs, autenticação, cache ou medição de tempo) a várias funções 
 de forma reutilizável e limpa.

 <b>3. Como ele é utilizado no Flask?</b>
 No Flask, o decorator principal é o @app.route. Ele é usado para vincular uma 
 URL (rota) a uma função específica do Python. Quando o usuário acessa o caminho 
 definido, o Flask 'sabe' que deve executar a função que está logo abaixo do decorator.
 
 Exemplo:
 @app.route('/contato')
 def pagina_contato():
 return "Página de Contato"
 """
    return texto_explicativo


if __name__ == "__main__":
    app.run(debug=True)
