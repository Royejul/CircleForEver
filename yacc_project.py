import ply.yacc as yacc

from lex5 import tokens
import AST

vars = {}

def p_programme_statement(p):
    ''' programme : statement '''
    p[0] = AST.ProgramNode(p[1])

# Si une ligne contient plusieurs codes exécutables
def p_programme_recursive(p):
    ''' programme : statement ';' programme '''
    p[0] = AST.ProgramNode([p[1]]+p[3].children)


# Défini une ligne
def p_statement(p):
    ''' statement : assignation
        | structure '''
    p[0] = p[1]

# Défini un PRINT()
#def p_statement_print(p):
#    ''' statement : PRINT expression '''
#    p[0] = AST.PrintNode(p[2])

def p_structure_for(p):
    ''' structure : FOR expression '{' programme '}' '''
    p[0] = AST.ForNode([p[2],p[4]])
    #TODO Gérer le for

# Défini une fonction WHILE
def p_structure_while(p):
    ''' structure : WHILE expression '{' programme '}' '''
    p[0] = AST.WhileNode([p[2],p[4]])

# TODO Vérifier les structures LINE, TEXT, ELLIPSE, SQUARE
# Défini une fonction LINE
def p_structure_figure_line(p):
    ''' structure : LINE '(' programme ')' '''
    p[0] = AST.FigureNode(p[3])
    
# Défini une fonction TEXT
def p_structure_figure_text(p):
    ''' structure : TEXT '(' programme ')' '''
    p[0] = AST.FigureNode(p[3])
    
# Défini une fonction ELLIPSE
def p_structure_figure_ellipse(p):
    ''' structure : ELLIPSE '(' programme ')' '''
    p[0] = AST.FigureNode(p[3])
    
# Défini une fonction SQUARE
def p_structure_figure_square(p):
    ''' structure : SQUARE '(' programme ')' '''
    p[0] = AST.FigureNode(p[3])
    
# Défini une structure comme un IDPARAMS (line, text, ...) et son EXPRESSION (ses paramètres)
def p_structure_param(p):
    ''' structure : IDPARAMS ':' EXPRESSION '''
    p[0] = p[3]

# Défini une expression comme une opération (+, -, *)
def p_expression_op(p):
    ''' expression : expression ADD_OP expression
            | expression MUL_OP expression'''
    p[0] = AST.OpNode(p[2], [p[1], p[3]])

# Défini une expression comme un NUMBER ou IDENTIFIER ou IDPARAMS
def p_expression_num_or_var(p):
    ''' expression : NUMBER
        | IDENTIFIER 
        | IDPARAMS '''
    p[0] = AST.TokenNode(p[1])

# Défini une expression comme une expression entre parenthèse
def p_expression_paren(p):
    ''' expression : '(' expression ')' '''
    p[0] = p[2]

# Défini une expression comme une suite d'expressions, séparées par une virgule (paramètres)
#todo A VéRIFIER ICI !! PARAMèTRES
#TODO CHECKER COULEURS 
def p_expression_param(p):
    ''' expression : expression ',' expression '''
    p[0] = AST.ParamNode([p[1], p[2]])

# Défini 
def p_minus(p):
    ''' expression : ADD_OP expression %prec UMINUS'''
    p[0] = AST.OpNode(p[1], [p[2]])

def p_assign(p):
    ''' assignation : IDENTIFIER '=' expression '''
    p[0] = AST.AssignNode([AST.TokenNode(p[1]),p[3]])

def p_error(p):
    if p:
        print ("Syntax error in line %d" % p.lineno)
        yacc.errok()
    else:
        print ("Sytax error: unexpected end of file!")


precedence = (
    ('left', 'ADD_OP'),
    ('left', 'MUL_OP') 
)

def parse(program):
    return yacc.parse(program)

yacc.yacc(outputdir='generated')

if __name__ == "__main__":
    import sys 

    prog = open(sys.argv[1]).read()
    result = yacc.parse(prog)
    if result:
        print (result)
            
        import os
        graph = result.makegraphicaltree()
        name = os.path.splitext(sys.argv[1])[0]+'-ast.pdf'
        graph.write_pdf(name) 
        print ("wrote ast to", name)
    else:
        print ("Parsing returned no result!")