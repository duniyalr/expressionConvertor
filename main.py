# error in postfix and prefix (a*b)^c+u+r+g+h*b-(f+g)*m
from src.utils import expr_type
from src.config import EXPR_TYPE
from src.tokenizer import Tokenizer
from src.parsers.infix import InfixParser
from src.parsers.postfix import PostfixParser
from src.parsers.prefix import PrefixParser
from src.outputs.postfix import PostfixOutput
from src.outputs.infix import InfixOutput
from src.outputs.prefix import PrefixOutput
from src.printer import Printer
print(
"""
Hi!
This app can convert the expressions from infix, prefix and 
postfix to another ones.
Just type your expression and press enter.
"""
)
while True:
  print(">>>", end=" ")
  expr = input()
  exprType = expr_type(expr)
  typeWord = "infix" if exprType == EXPR_TYPE.INFIX else "prefix" if exprType == EXPR_TYPE.PREFIX else "postfix"
  print("Your expression is" + (" an " if typeWord[0] == "i" else " a ") + typeWord)

  tokenizer = Tokenizer(expr)
  tokenizer.tokenize();
  parser = InfixParser(tokenizer.tokens) if exprType == EXPR_TYPE.INFIX else PrefixParser(tokenizer.tokens) if exprType == EXPR_TYPE.PREFIX else PostfixParser(tokenizer.tokens)
  parser.parse()
  postfixOutput = PostfixOutput(parser.temp)
  infixOutput = InfixOutput(parser.temp)
  prefixOutput = PrefixOutput(parser.temp)
  print("")
  print("Prefix  = " + prefixOutput.output())
  print("Infix   = " + infixOutput.output())
  print("Postfix = " + postfixOutput.output())
  print("")

  printer = Printer(parser.temp)
  printer.simple();
  print("")