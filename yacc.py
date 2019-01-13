import ply.yacc as yacc
import sys
import os

from lex import tokens
import AST

vars = {}

def p_init_statement(p):
    '''init : programme'''
    p[0] = AST.InitNode(p[1])

def p_programme_statement(p):
    ''' programme : statement '''
    p[0] = AST.ProgramNode(p[1])


def p_programme_recursive(p):
    ''' programme : statement ';' programme '''
    p[0] = AST.ProgramNode([p[1]]+p[3].children)

def p_statement(p):
    """ statement : assignation
        | structure
        | PRINT expression """
    try:
        p[0] = AST.PrintNode(p[2])
    except:
        p[0] = p[1]

def p_compare(p):
    """ compare : expression COMP expression
        | expression EQUALS expression
        | expression LESSTHAN expression
        | expression GREATTHAN expression
        """
    p[0] = AST.CompareNode(p[2], [p[1], p[3]])

def p_structure_for(p):
    """ structure : FOR '(' assignation ';' compare ';' assignation ')' '{' programme '}' """
    p[0] = AST.ForNode([p[3], p[5], p[7], p[10]])

def p_structure_while(p):
    ''' structure : WHILE '(' compare ')' '{' programme '}' '''
    p[0] = AST.WhileNode([p[3], p[6]])

def p_structure_form(p):
    ''' structure : FORMS '(' params ')' '''
    p[0] = AST.FormNode(p[1], [p[3]])

def p_param_list(p):
    ''' params : param '''
    p[0] = AST.ParameterList([p[1]])

def p_param_list_rec(p):
    ''' params : param ';' params '''
    p[0] = AST.ParameterList([p[1]]+p[3].children)

def p_param(p):
    '''param : IDPARAMS ':' paramvalue '''
    p[0]= AST.ParameterNode(p[1], [p[3]])
 
def p_paramvalue(p):
    ''' paramvalue : expression ',' paramvalue 
        | expression '''
    try:
        p[0] = AST.ValueNode([p[1]]+p[3].children)
    except:
        p[0] = AST.ValueNode([p[1]])

def p_expression_num_or_id(p):
    ''' expression : NUMBER
        | IDENTIFIER 
        | COLORPARAMS
        | STRING '''
    p[0] = AST.TokenNode(p[1])

def p_expression_paren(p):
    ''' expression : '(' expression ')' '''
    p[0] = p[2]

def p_expression_op(p):
    ''' expression : expression ADD_OP expression
            | expression MUL_OP expression '''
    p[0] = AST.OpNode(p[2], [p[1], p[3]])

def p_minus(p):
    ''' expression : ADD_OP expression %prec UMINUS'''
    p[0] = AST.OpNode([p[1], p[2]])

def p_assign(p):
    """ assignation : IDENTIFIER '=' expression """
    p[0] = AST.AssignNode([AST.TokenNode(p[1]), p[3]])


def p_error(p):
    if p:
        tok = yacc.token()
        print("Syntax error at token \"%s\" near line %s" % (p.type, p.lineno))
        # Just discard the token and tell the parser it's okay.
        yacc.errok()
        return tok
    else:
        print("Syntax error at EOF")


precedence = (
    ('left', 'ADD_OP'),
    ('left', 'MUL_OP'),
    ('right', 'UMINUS')
)

def parse(program):
    return yacc.parse(program)

yacc.yacc(outputdir='generated')

if __name__ == "__main__":
    try:
        filename = sys.argv[1]
    except:
        filename = "ExempleBoucle.txt"

    prog = open(filename).read()
    result = yacc.parse(prog)
    print(result)

    # graph = result.makegraphicaltree()
    # name = os.path.splitext(sys.argv[1])[0] + '-ast.pdf'
    # graph.write_pdf(name)
    # print("wrote ast to", name)