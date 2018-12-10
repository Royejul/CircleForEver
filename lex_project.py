import ply.lex as lex
import sys


reserved_words = (
    'while',
    'for',
    'line',
    'text',
    'ellipse',
    'square')

reserved_params = (
    'pos',
    'width',
    'color',
    'fontsize',
    'word',
    'radius')
    
reserved_colors = (
    'white',
    'black',
    'red',
    'blue',
    'yellow',
    'green',
    'pink',
    'purple',
    'maroon',
    'orange',
    'lime')
    
tokens = ('NUMBER', 'ADD_OP', 'MUL_OP', 'IDENTIFIER', 'IDPARAMS', 'WORDPARAMS') + tuple(map(lambda s:s.upper(), reserved_words) + tuple(map(lambda s:s.upper(), reserved_params) + tuple(map(lambda s:s.upper(), reserved_colors))

t_ignore = ' \t'

literals = '();=,'

def t_ADD_OP(t):
    r'[+-]'
    return t

def t_MUL_OP(t):
    r'[*/]'
    return t

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t
    
def t_IDENTIFIER(t):
    r'[A-Za-z_]\w*'
    if t.value in reserved_words:
        t.type = t.value.upper()
    return t

def t_IDPARAMS(t):
    r'[A-Za-z_]\w*'
    if t.value in reserved_params:
        t.type = t.value.upper()
    return t

def t_WORDPARAMS(t):
    r'[A-Za-z_]\w*'
    if t.value in reserved_colors:
        t.type = t.value.upper()
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    
def t_error(t):
    print("Illegal character '%s'" %t.value[0])
    t.lexer.skip(1)
    
lex.lex()
    
if __name__ == "__main__":
    prog = open(sys.argv[1]).read()
    lex.input(prog)
    while 1:
        tok = lex.token()
        if not tok:
            print("No token")
            break
        print("line %d: %s(%s)" %(tok.lineno, tok.type, tok.value))