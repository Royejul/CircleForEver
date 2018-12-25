import ply.yacc as yacc

from lex_project import tokens
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
    ''' statement : structure
        | assignation '''
    p[0] = p[1]

# Défini un PRINT()
#def p_statement_print(p):
#    ''' statement : PRINT expression '''
#    p[0] = AST.PrintNode(p[2])

# Défini une fonction FOR
def p_structure_for(p):
    ''' structure : FOR expression '{' programme '}' '''
    p[0] = AST.ForNode([p[2],p[4]])

# Défini une fonction WHILE
def p_structure_while(p):
    ''' structure : WHILE expression '{' programme '}' '''
    p[0] = AST.WhileNode([p[2],p[4]])

# Défini une structure comme un IDENTIFIER(programme) --> (Line(pos: ...))
def p_structure_form(p):
    ''' structure : FORMS '(' params ')' '''
    p[0] = AST.FormNode(p[1])

#TODO HERE : AST.ParameterNode ???    
# Défini une suite de paramètres comme un IDPARAMS (pos, width, etc) et son EXPRESSION (ses paramètres)
def p_params(p):
    ''' params : IDPARAMS ':' paramvalue ';' params
        | IDPARAMS ':' paramvalue '''
    p[0] = AST.ParameterNode(p[1], [p[3]])

#TODO HERE : Est-ce à compléter ? Il me semble que c'est correct (pris de l'explication du prof)
#TODO Le problème vient surement des AST.TokenNode et AST.ParameterNode (pour p_params). 
# Défini une expression comme une suite d'expressions, séparées par une virgule (paramètres)
def p_paramvalue(p):
    ''' paramvalue : expression ',' paramvalue 
        | expression '''
    p[0] = AST.TokenNode(p[1]) #TODO p[1].children me semble correcte pour moi...

# Défini une expression comme un NUMBER ou IDENTIFIER ou une COLOR
def p_expression_num_or_id(p):
    ''' expression : NUMBER
        | IDENTIFIER 
        | COLORPARAMS
        | '"' STRING  '"' '''
    p[0] = AST.TokenNode(p[1])

# Défini une expression comme une expression entre parenthèse
def p_expression_paren(p):
    ''' expression : '(' expression ')' '''
    p[0] = p[2]

# Défini une expression comme une opération (+, -, *)
def p_expression_op(p):
    ''' expression : expression ADD_OP expression
            | expression MUL_OP expression '''
    p[0] = AST.OpNode(p[2], [p[1], p[3]])

#def p_expression_compare(p):
#    ''' expression : expression COMPARE expression '''
#    p[0] = AST.CompareNode(p[4])

#def p_expression_plusegal(p):
#    ''' expression : expression PLUSEGAL expression '''
#    p[0] = AST.PlusEgalNode(p[3])

# Défini nombre négatif
def p_minus(p):
    ''' expression : ADD_OP expression %prec UMINUS'''
    p[0] = AST.OpNode([p[1], p[2]])

def p_assign(p):
    ''' assignation : IDENTIFIER '=' expression '''
    p[0] = AST.AssignNode([AST.TokenNode(p[1]),p[3]])
    vars[p[1]] = p[3]

def p_error(p):
    if p:
        print ("Syntax error in line %d" % p.lineno)
        yacc.errok()
    else:
        print ("Sytax error: unexpected end of file!")


precedence = (
    ('left', 'ADD_OP'),
    ('left', 'MUL_OP'),
    ('left', 'PLUSEGAL'),
    ('right', 'UMINUS'),
)

def parse(program):
    return yacc.parse(program)

yacc.yacc(outputdir='generated')

if __name__ == "__main__":
    import sys
    prog = open(sys.argv[1]).read()
    result = yacc.parse(prog)
    print(result)
    
    import os
    #graph = result.makegraphicaltree()
    #name = os.path.splitext(sys.argv[1])[0] + '-ast.pdf'
    #graph.write_pdf(name)
    #print("wrote ast to", name)