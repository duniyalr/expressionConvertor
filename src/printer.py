from .config import Expression, Operator

boxChars = {
  0: "├─ ",
  1: "│  ",
  2: "└─ "
}

class Printer:
  simpleSpace = 2



  def __init__(self, root):
    self.root = root
    self.charChain = []

  def simple(self, node = None, depth = 0):
    if not node:
      node = self.root
    if len(self.charChain):
      i = 0
      for char in self.charChain:
        if char == 0:
          print(boxChars[0], end="")
          self.charChain[i] += 1
        elif char == 1:
          print(boxChars[1], end="")
        elif char == 2:
          print(boxChars[2], end="")
          self.charChain[i] += 1
        else:
          print("   ", end="")
        i += 1
    if isinstance(node, Operator):
      print(node.v)
      self.charChain.append(0)
      self.simple(node.lc, depth + 1)
      self.charChain[depth] += 1
      self.simple(node.rc, depth + 1)
      self.charChain.pop()
    else:
      print(node.value)
      

