def parse(tokens):
    if not tokens:
        return "Error: No hay tokens para analizar."
    
    index = 0
    length = len(tokens)
    declared_vars = set()

    def match(expected_type, expected_value=None):
        nonlocal index
        if index < length and tokens[index].type == expected_type:
            if expected_value is None or tokens[index].value == expected_value:
                index += 1
                return True
        return False

    def parse_for_loop():
        nonlocal declared_vars

        if not match('ID', 'for'):
            return "Error: Se esperaba 'for'."
        
        if not match('LPAREN'):
            return "Error: Se esperaba '('."
        
        if not match('ID', 'var'):
            return "Error: Se esperaba 'var'."
        
        if not match('ID'):
            return "Error: Se esperaba un identificador."
        
        var_name = tokens[index - 1].value
        declared_vars.add(var_name)
        
        if not match('EQ'):
            return "Error: Se esperaba '='."
        
        if not match('NUMBER'):
            return "Error: Se esperaba un número."
        
        if not match('SEMICOLON'):
            return "Error: Se esperaba ';'."
        
        if not match('ID'):
            return "Error: Se esperaba un identificador."
        
        if not match('OP'):
            return "Error: Se esperaba un operador relacional."
        
        if not match('NUMBER'):
            return "Error: Se esperaba un número."
        
        if not match('SEMICOLON'):
            return "Error: Se esperaba ';'."
        
        if not match('ID'):
            return "Error: Se esperaba un identificador."
        
        if not match('OP', '++'):
            return "Error: Se esperaba '++'."
        
        if not match('RPAREN'):
            return "Error: Se esperaba ')'."
        
        if not match('LBRACE'):
            return "Error: Se esperaba '{'."
        
        # Validar el cuerpo del bucle
        if not match('ID', 'console'):
            return "Error: Se esperaba 'console'."
        
        if not match('OP', '.'):
            return "Error: Se esperaba '.'."
        
        if not match('ID', 'log'):
            return "Error: Se esperaba 'log'."
        
        if not match('LPAREN'):
            return "Error: Se esperaba '('."
        
        if not match('STRING'):
            return "Error: Se esperaba una cadena de texto."
        
        if not match('OP', '+'):
            return "Error: Se esperaba '+'."
        
        if not match('ID'):
            return "Error: Se esperaba un identificador."

        var_name_in_log = tokens[index - 1].value
        if var_name_in_log not in declared_vars:
            return f"Error: La variable '{var_name_in_log}' no ha sido declarada."
        
        if not match('RPAREN'):
            return "Error: Se esperaba ')'."
        
        if not match('SEMICOLON'):
            return "Error: Se esperaba ';'."
        
        if not match('RBRACE'):
            return "Error: Se esperaba '}'."
        
        # Verificar la llamada a console.log(global)
        if not match('ID', 'console'):
            return "Error: Se esperaba 'console'."
        
        if not match('OP', '.'):
            return "Error: Se esperaba '.'."
        
        if not match('ID', 'log'):
            return "Error: Se esperaba 'log'."
        
        if not match('LPAREN'):
            return "Error: Se esperaba '('."
        
        if not match('ID', 'global'):
            return "Error: Se esperaba 'global'."
        
        if not match('RPAREN'):
            return "Error: Se esperaba ')'."
        
        if not match('SEMICOLON'):
            return "Error: Se esperaba ';'."
        
        return "Estructura for correcta"

    return parse_for_loop()
