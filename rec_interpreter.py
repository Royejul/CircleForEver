import AST
import operator
from AST import addToClass
from functools import reduce
from drawTools import DrawTools

operations = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
}

comparators = {
    '<': operator.lt,
    '>': operator.gt,
    '=>': operator.ge,
    '=<': operator.le,
    '==': operator.eq,
}

p = DrawTools((1200, 800), (255, 255, 255))


collect_params = {
    'line': ('pos','color','width'),
    'text': ('pos','word','fontsize','color'),
    'ellipse': ('pos','color','linecolor'),
    'rectangle': ('pos','color','linecolor'),

}

params = (
    'pos',
    'width',
    'color',
    'linecolor',
    'fontsize',
    'word'
)

vars = {
    'white': (255, 255, 255),
    'black': (0, 0, 0),
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255),
    'yellow': (255, 255, 0),
    'pink': (255, 0, 255),
    'purple': (127, 0, 255),
    'maroon': (153, 76, 0),
    'orange': (255, 128, 0),
    'lime': (128, 255, 0),
}

@addToClass(AST.InitNode)
def execute(self, namefile):
    for c in self.children:
        c.execute()
    p.PDFSave(namefile)

@addToClass(AST.ProgramNode)
def execute(self):
    for c in self.children:
        c.execute()

@addToClass(AST.TokenNode)
def execute(self, diff='test'):
    if diff == 'word':
        return self.tok
    if isinstance(self.tok, str):
        try:
            return vars[self.tok]
        except KeyError:
            print("*** Error : variable %s undefined!" % self.tok)
    elif isinstance(self.tok, float):
        return int(self.tok)
    return self.tok

@addToClass(AST.OpNode)
def execute(self, name='fix'):
    args = [c.execute() for c in self.children]
    if len(args) == 1:
        args.insert(0,0)
    return reduce(operations[self.op], args)

@addToClass(AST.AssignNode)
def execute(self):
    vars[self.children[0].tok] = self.children[1].execute()


@addToClass(AST.PrintNode)
def execute(self):
    print(self.children[0].execute())

@addToClass(AST.WhileNode)
def execute(self):
    while self.children[0].execute():
        self.children[1].execute()

@addToClass(AST.ForNode)
def execute(self):
    self.children[0].execute()
    while self.children[1].execute():
        self.children[3].execute()
        self.children[2].execute()

@addToClass(AST.CompareNode)
def execute(self):
    args = [c.execute() for c in self.children]
    compar = comparators.get(self.comparator)
    return compar(args[0],args[1])

@addToClass(AST.FormNode)
def execute(self):
    args = self.children[0].execute()
    param = collect_params[self.name]
    val =[]
    for i in param:
        if i in args:
            if i == 'pos':
                val.append(tuple(args.get(i)))
            else:
                val.append(args.get(i)[0])
    attrib = tuple(val)
    if self.name == 'line':
        p.addLine(*attrib)
    elif self.name == 'rectangle':
        p.addRectangle(*attrib)
    elif self.name == 'ellipse':
        p.addEllipse(*attrib)
    elif self.name == 'text':
        p.addText(*attrib)


@addToClass(AST.ParameterList)
def execute(self):
    args = {}
    for c in self.children:
        t = c.execute()
        args[t[0]] = t[1]
    return args

@addToClass(AST.ParameterNode)
def execute(self):
    args = self.children[0].execute(self.name)
    return [self.name, args]

@addToClass(AST.ValueNode)
def execute(self, namevalue):
    return [c.execute(namevalue) for c in self.children]


if __name__ == "__main__":
    from yacc_project import parse
    import sys
    import os
    prog = open(sys.argv[1]).read()
    name = os.path.splitext(sys.argv[1])[0] + '-image.pdf'
    ast = parse(prog)

    ast.execute(name)
