import re

# Definición de los tipos de tokens
token_specification = [
    ('NUMBER',  r'\d+(\.\d*)?'),       # Números
    ('ID',      r'[A-Za-z_]\w*'),      # Identificadores
    ('OP',      r'(\+\+|<=|>=|==|!=|<|>|\+|-|\*|\/|\.)'),  # Operadores, incluyendo punto y otros operadores aritméticos
    ('LPAREN',  r'\('),                # Paréntesis izquierdo
    ('RPAREN',  r'\)'),                # Paréntesis derecho
    ('LBRACE',  r'\{'),                # Llave izquierda
    ('RBRACE',  r'\}'),                # Llave derecha
    ('SEMICOLON', r';'),               # Punto y coma
    ('EQ',      r'='),                 # Igual
    ('STRING',  r'"[^"]*"'),           # Cadenas de texto
    ('SKIP',    r'[ \t]+'),            # Espacios y tabulaciones
    ('NEWLINE', r'\n'),                # Nuevas líneas
    ('MISMATCH',r'.'),                 # Cualquier otro carácter
]

tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
get_token = re.compile(tok_regex).match

class Token:
    def __init__(self, type, value, line):
        self.type = type
        self.value = value
        self.line = line

def lex(text):
    line_num = 1
    pos = line_start = 0
    mo = get_token(text)
    tokens = []
    while mo is not None:
        typ = mo.lastgroup
        val = mo.group(typ)
        if typ == 'NEWLINE':
            line_start = pos
            line_num += 1
        elif typ != 'SKIP' and typ != 'MISMATCH':
            token = Token(typ, val, line_num)
            tokens.append(token)
        pos = mo.end()
        mo = get_token(text, pos)
    return tokens

if __name__ == '__main__':
    code = 'global'
    tokens = lex(code)
    for token in tokens:
        print(f'{token.type}: {token.value}')
