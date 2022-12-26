from ..config import Operator, Expression

class PrefixOutput:
  def __init__(self, rootNode):
    self.rootNode = rootNode

  def output(self, node = None):
    if not node:
      node = self.rootNode
    if isinstance(node, Operator):
      rc = None;
      lc = None;
      if isinstance(node.rc, Operator):
        rc = self.output(node.rc)
      else:
        rc = node.rc.value
      if isinstance(node.lc, Operator):
        lc = self.output(node.lc)
      else:
        lc = node.lc.value
      return node.v + lc + rc 