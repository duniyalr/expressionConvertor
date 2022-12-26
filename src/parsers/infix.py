from enum import Enum
from ..config import TOKEN_TYPE, Expression, Operator
from ..utils import hasMorePriority, normalizeTree
from ..tokenizer import Token
from ..printer import Printer
class Mode(Enum):
  IDLE = 1
  OPERATOR = 2
  AFTER_OPERATOR = 3

class InfixParser: 
  i = 0
  mode = Mode.IDLE
  activeToken = None
  temp = None
  chain = []

  def __init__(self, tokens):
    self.tokens = tokens;

  def findNextOperator(self): 
    i = self.i + 1;
    while (len(self.tokens) > i):
      token = self.tokens[i];
      if token.type == TOKEN_TYPE.OPERATOR:
        return i
      i += 1

  def parHandle(self): 
    newTokens = []
    temp = None;
    i = 0
    j = 0

    for token in self.tokens:
      if token.type == TOKEN_TYPE.OPEN_PAR:
        if j == 0:
          temp = i
        j += 1
      elif token.type == TOKEN_TYPE.CLOSE_PAR:
        if j == 1:
          if i-temp != 1:
            infixParser = InfixParser(self.tokens[temp + 1:i])
            infixParser.parse()
            newToken = Token(TOKEN_TYPE.VAR, infixParser.temp)
            newTokens.append(newToken)
      
        j -= 1
      elif j == 0:
        newTokens.append(token)
      i += 1
    self.tokens = newTokens

  def parse(self):
    self.parHandle()
    self.chain = []

    while self.i < len(self.tokens):
      token = self.tokens[self.i]
      self.activeToken = token
      if self.mode == Mode.IDLE: 
        self.idleHandle()
      elif self.mode == Mode.OPERATOR:
        self.operatorHandle()
      elif self.mode == Mode.AFTER_OPERATOR:
        self.afterOperatorHandle()
      self.i += 1
    
    self.temp = normalizeTree(self.temp)

  def idleHandle(self):
    if self.activeToken.type == TOKEN_TYPE.OPERATOR:
      self.operatorHandle()
      
    elif self.activeToken.type == TOKEN_TYPE.VAR:
      self.varHandle()

    elif self.mode == Mode.AFTER_OPERATOR:
      self.afterOperatorHandle()

  def varHandle(self):
    expression = Expression(self.activeToken.value)

    self.temp = expression
    self.mode = Mode.OPERATOR

  def operatorHandle(self):
    if not self.temp: 
      raise Exception("you should add a var before operator in infix")
        
    operator = Operator(self.activeToken.value)
    operator.lc = self.temp
    self.chain.append(operator)
    self.temp = None;
    self.mode = Mode.AFTER_OPERATOR
    nextOperator = self.findNextOperator()
    if nextOperator:
      # todo check for position of operator
      if hasMorePriority(self.tokens[nextOperator].value, self.activeToken.value):
        self.temp = self.rollback()
        self.chain.append(self.temp)
        self.mode = Mode.IDLE
      elif self.tokens[nextOperator].value == "^":
        self.mode = Mode.IDLE
        

  def afterOperatorHandle(self):
    if self.activeToken.type == TOKEN_TYPE.VAR:
      self.chain.append(Expression(self.activeToken.value))
      self.temp = self.rollback()
      self.mode = Mode.OPERATOR

  def rollback(self): 
    i = len(self.chain) - 1;
    temp = None;
    while(i >= 0):
      elm = self.chain[i]       
      if temp:
        elm.rc = temp
      temp = elm
      i -= 1
    self.chain = []
    return temp
      