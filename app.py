from flask import Flask, request, render_template
from lexer import lex
from parser_1 import parse

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    tokens = []
    syntax_result = ""
    if request.method == 'POST':
        code = request.form['code']
        tokens = lex(code)
        syntax_result = parse(tokens)
    
    return render_template('index.html', tokens=tokens, syntax_result=syntax_result)

if __name__ == '__main__':
    app.run(debug=True)
