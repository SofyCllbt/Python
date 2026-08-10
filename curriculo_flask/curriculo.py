from flask import Flask
app = Flask(__name__)
@app.route('/')
def curriculo():
    return '''
<!DOCTYPE html>
<html lang="pt-BR">
<head>
 <meta charset="UTF-8">
 <title>Meu Currículo Online</title>
 <style>
 body { font-family: Arial, sans-serif; line-height: 1.6; margin: 40px; color: #333; }
 header { text-align: center; border-bottom: 2px solid #0056b3; padding-bottom: 10px; }
 h2 { color: #0056b3; border-bottom: 1px solid #ccc; margin-top: 20px; }
 ul { padding-left: 20px; }
 </style>
</head>
<body>
 <header>
 <h1>Nome: Sofia Garbazza Leite</h1>
 <p>Email: 12401234@aluno.cotemig.com.br | Telefone: (31)4002-8922</p>
 </header>

 <section>
 <h2>Experiência Profissional</h2>
 <h1>Estagio com foco em Planilhas</h1>
 </section>

 <section>
 <h2>Formação Acadêmica</h2>
 <h1>Cotemig/ 100% concluido</h1>
 </section>

 <section>
 <h2>Idiomas</h2>
 <p>Inglês: 100%</p>
 <p>Espanhol: 50%</p>
 </section>
</body>
</html>
'''

if __name__ == '__main__':
 app.run(debug=True)
