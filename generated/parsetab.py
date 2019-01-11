
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = '163F4D71E55F01F4452A4111330810F9'
    
_lr_action_items = {'PRINT':([0,10,47,62,],[5,5,5,5,]),'IDENTIFIER':([0,5,10,16,17,18,19,20,23,24,37,39,40,41,42,45,47,55,57,62,],[6,13,6,13,13,13,6,13,13,13,13,13,13,13,13,13,6,6,13,6,]),'FOR':([0,10,47,62,],[7,7,7,7,]),'WHILE':([0,10,47,62,],[8,8,8,8,]),'FORMS':([0,10,47,62,],[9,9,9,9,]),'$end':([1,2,3,4,11,12,13,14,15,22,26,27,34,35,36,43,59,64,],[0,-1,-3,-4,-5,-18,-19,-20,-21,-2,-25,-26,-23,-24,-22,-12,-11,-10,]),'}':([2,3,4,11,12,13,14,15,22,26,27,34,35,36,43,56,59,63,64,],[-1,-3,-4,-5,-18,-19,-20,-21,-2,-25,-26,-23,-24,-22,-12,59,-11,64,-10,]),';':([2,3,4,11,12,13,14,15,26,27,28,32,34,35,36,43,46,48,49,50,51,53,54,59,60,64,],[10,-3,-4,-5,-18,-19,-20,-21,-25,-26,37,44,-23,-24,-22,-12,55,-6,-7,-8,-9,-13,-17,-11,-16,-10,]),'NUMBER':([5,16,17,18,20,23,24,37,39,40,41,42,45,57,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'COLORPARAMS':([5,16,17,18,20,23,24,37,39,40,41,42,45,57,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'STRING':([5,16,17,18,20,23,24,37,39,40,41,42,45,57,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'(':([5,7,8,9,16,17,18,20,23,24,37,39,40,41,42,45,57,],[16,19,20,21,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'ADD_OP':([5,11,12,13,14,15,16,17,18,20,23,24,25,26,27,30,34,35,36,37,39,40,41,42,45,48,49,50,51,54,57,],[17,23,-18,-19,-20,-21,17,17,17,17,17,17,23,-25,23,23,-23,-24,-22,17,17,17,17,17,17,23,23,23,23,23,17,]),'=':([6,],[18,]),'MUL_OP':([11,12,13,14,15,25,26,27,30,34,35,36,48,49,50,51,54,],[24,-18,-19,-20,-21,24,-25,24,24,24,-24,-22,24,24,24,24,24,]),')':([12,13,14,15,25,26,27,29,31,32,34,35,36,48,49,50,51,52,53,54,58,60,],[-18,-19,-20,-21,36,-25,-26,38,43,-14,-23,-24,-22,-6,-7,-8,-9,-15,-13,-17,61,-16,]),'COMP':([12,13,14,15,26,30,34,35,36,],[-18,-19,-20,-21,-25,39,-23,-24,-22,]),'EQUALS':([12,13,14,15,26,30,34,35,36,],[-18,-19,-20,-21,-25,40,-23,-24,-22,]),'LESSTHAN':([12,13,14,15,26,30,34,35,36,],[-18,-19,-20,-21,-25,41,-23,-24,-22,]),'GREATTHAN':([12,13,14,15,26,30,34,35,36,],[-18,-19,-20,-21,-25,42,-23,-24,-22,]),',':([12,13,14,15,26,34,35,36,54,],[-18,-19,-20,-21,-25,-23,-24,-22,57,]),'IDPARAMS':([21,44,],[33,33,]),':':([33,],[45,]),'{':([38,61,],[47,62,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programme':([0,10,47,62,],[1,22,56,63,]),'statement':([0,10,47,62,],[2,2,2,2,]),'assignation':([0,10,19,47,55,62,],[3,3,28,3,58,3,]),'structure':([0,10,47,62,],[4,4,4,4,]),'expression':([5,16,17,18,20,23,24,37,39,40,41,42,45,57,],[11,25,26,27,30,34,35,30,48,49,50,51,54,54,]),'compare':([20,37,],[29,46,]),'params':([21,44,],[31,52,]),'param':([21,44,],[32,32,]),'paramvalue':([45,57,],[53,60,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programme","S'",1,None,None,None),
  ('programme -> statement','programme',1,'p_programme_statement','yacc_project.py',9),
  ('programme -> statement ; programme','programme',3,'p_programme_recursive','yacc_project.py',14),
  ('statement -> assignation','statement',1,'p_statement','yacc_project.py',18),
  ('statement -> structure','statement',1,'p_statement','yacc_project.py',19),
  ('statement -> PRINT expression','statement',2,'p_statement','yacc_project.py',20),
  ('compare -> expression COMP expression','compare',3,'p_compare','yacc_project.py',27),
  ('compare -> expression EQUALS expression','compare',3,'p_compare','yacc_project.py',28),
  ('compare -> expression LESSTHAN expression','compare',3,'p_compare','yacc_project.py',29),
  ('compare -> expression GREATTHAN expression','compare',3,'p_compare','yacc_project.py',30),
  ('structure -> FOR ( assignation ; compare ; assignation ) { programme }','structure',11,'p_structure_for','yacc_project.py',35),
  ('structure -> WHILE ( compare ) { programme }','structure',7,'p_structure_while','yacc_project.py',39),
  ('structure -> FORMS ( params )','structure',4,'p_structure_form','yacc_project.py',43),
  ('param -> IDPARAMS : paramvalue','param',3,'p_param','yacc_project.py',47),
  ('params -> param','params',1,'p_param_list','yacc_project.py',51),
  ('params -> param ; params','params',3,'p_param_list_rec','yacc_project.py',55),
  ('paramvalue -> expression , paramvalue','paramvalue',3,'p_paramvalue','yacc_project.py',59),
  ('paramvalue -> expression','paramvalue',1,'p_paramvalue','yacc_project.py',60),
  ('expression -> NUMBER','expression',1,'p_expression_num_or_id','yacc_project.py',68),
  ('expression -> IDENTIFIER','expression',1,'p_expression_num_or_id','yacc_project.py',69),
  ('expression -> COLORPARAMS','expression',1,'p_expression_num_or_id','yacc_project.py',70),
  ('expression -> STRING','expression',1,'p_expression_num_or_id','yacc_project.py',71),
  ('expression -> ( expression )','expression',3,'p_expression_paren','yacc_project.py',76),
  ('expression -> expression ADD_OP expression','expression',3,'p_expression_op','yacc_project.py',81),
  ('expression -> expression MUL_OP expression','expression',3,'p_expression_op','yacc_project.py',82),
  ('expression -> ADD_OP expression','expression',2,'p_minus','yacc_project.py',87),
  ('assignation -> IDENTIFIER = expression','assignation',3,'p_assign','yacc_project.py',91),
]
