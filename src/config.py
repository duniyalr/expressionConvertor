from enum import Enum

VAR_REGEX = r'\w'
OPERATOR_REGEX = r'[\+\/\*\-\^]'
OPEN_PAR_REGEX = r'\('
CLOSE_PAR_REGEX = r'\)'

class TOKEN_TYPE(Enum):
  VAR = 1;
  OPERATOR = 2;
  OPEN_PAR = 3;
  CLOSE_PAR = 4;

class EXPR_TYPE(Enum):
  INFIX = 1
  PREFIX = 2
  POSTFIX = 3

PRIORITY = {
  "+": 0,
  "-": 0,
  "*": 1,
  "/": 1,
  "^": 2
}

class Operator: 
  def __init__(self, v):
    self.v = v
    self.rc = None
    self.lc = None

class Expression:

  def __init__(self, value):
    self.value = value 