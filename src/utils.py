import re
from .config import EXPR_TYPE,OPERATOR_REGEX, PRIORITY, Operator, Expression

def expr_type(expr): 
  if re.match(OPERATOR_REGEX, expr[0], ):
    return EXPR_TYPE.PREFIX
  elif re.match(OPERATOR_REGEX, expr[len(expr) - 1]):
    return EXPR_TYPE.POSTFIX
  else:
    return EXPR_TYPE.INFIX

def hasMorePriority(op1, op2): 
  return bool(PRIORITY[op1] - PRIORITY[op2] > 0)

def normalizeTree(node):
  if isinstance(node, Operator):
    if node.rc and isinstance(node.rc, Expression) and isinstance(node.rc.value, Operator):
      node.rc = node.rc.value
    if node.lc and isinstance(node.lc, Expression) and isinstance(node.lc.value, Operator):
      node.lc = node.lc.value
    
    if isinstance(node.rc, Operator):
      node.rc = normalizeTree(node.rc)
    if isinstance(node.lc, Operator):
      node.lc = normalizeTree(node.lc)
    return node
  elif isinstance(node.value, Operator):
    return normalizeTree(node.value)
  else:
    return node