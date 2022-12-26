from ..config import Operator, Expression
from ..utils import hasMorePriority
class InfixOutput:
  def __init__(self, rootNode):
    self.parentChain = []
    self.rootNode = rootNode
  
  def output(self, node = None, parentV = None):
    if not node:
      node = self.rootNode
    if isinstance(node, Operator):
      rc = None;
      lc = None;
      if isinstance(node.rc, Operator):
        rc = self.output(node.rc, node.v)
      else:
        rc = node.rc.value
      if isinstance(node.lc, Operator):
        lc = self.output(node.lc, node.v)
      else:
        lc = node.lc.value
      exp = lc + node.v + rc 
      if parentV and hasMorePriority(parentV, node.v):
        return "(" + exp + ")"
      return exp
    