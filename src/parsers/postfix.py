from ..config import Expression, Operator, TOKEN_TYPE

class PostfixParser: 

  def __init__(self, tokens): 
    if tokens[-1].type != TOKEN_TYPE.OPERATOR:
      raise Exception("last token should be an operator")
    self.pointer = Operator(tokens[-1].value)
    self.chain =[self.pointer]
    self.tokens = tokens[-2::-1]

  def parse(self):
    for token in self.tokens:
      if not self.pointer:
        raise Exception("there is no pointer")

      if token.type == TOKEN_TYPE.OPERATOR:
        operator = Operator(token.value)
        if not self.pointer.rc:
          self.pointer.rc = operator
          self.chain.append(self.pointer)
        elif not self.pointer.lc:
          self.pointer.lc = operator
        self.pointer = operator
      else:
        expression = Expression(token.value)
        if not self.pointer.rc:
          self.pointer.rc = expression
        elif not self.pointer.lc:
          self.pointer.lc = expression
          self.pointer = self.findPointer()
    self.temp = self.chain[0]

  def findPointer(self):
    if len(self.chain) <= 1:
      return None
    nPointer = self.chain.pop()
    while nPointer.lc:
      if len(self.chain):
        nPointer = self.chain.pop()
      else:
        return None
    return nPointer
