import re
from .config import TOKEN_TYPE, VAR_REGEX, OPEN_PAR_REGEX, CLOSE_PAR_REGEX, OPERATOR_REGEX



class Token: 
  def __init__(self, type, value): 
    self.type = type;
    self.value = value;


class Tokenizer:

  def __init__(self, expr):
    self.tokens = []
    self.expr = expr;

  def tokenize(self): 
    expr = self.expr
  
    for char in expr:
      __type = None
      if re.match(VAR_REGEX, char): 
        __type = TOKEN_TYPE.VAR
      elif re.match(OPERATOR_REGEX, char):
        __type = TOKEN_TYPE.OPERATOR
      elif re.match(OPEN_PAR_REGEX, char):
        __type = TOKEN_TYPE.OPEN_PAR
      elif re.match(CLOSE_PAR_REGEX, char):
        __type = TOKEN_TYPE.CLOSE_PAR

      if __type:
        self.tokens.append(Token(__type, char))
      else:   
        pass
          
