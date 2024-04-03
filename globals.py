import os
import time
import sys
import traceback
import builtins
import inspect

@staticmethod
def fmt2d(arg): return '{0:.2f}'.format(arg)
@staticmethod
def yesno(arg): return 'yes' if arg == 0 else 'no'
@staticmethod
def _log_fn():
  return os.path.basename(inspect.getframeinfo(inspect.currentframe().f_back.f_back).filename)
@staticmethod
def _log_ln():
  return inspect.getframeinfo(inspect.currentframe().f_back.f_back).lineno
@staticmethod
def msg(args): _msg(f"{logcol.yellow}{_log_fn()}{logcol.reset}:{logcol.green}{_log_ln()} {logcol.reset}{str(args)}{logcol.reset}")
@staticmethod
def dbg(args): _msg(f"{logcol.yellow}{_log_fn()}{logcol.reset}:{logcol.green}{_log_ln()} {logcol.cyan }{str(args)}{logcol.reset}")
@staticmethod
def err(args): _msg(f"{logcol.yellow}{_log_fn()}{logcol.reset}:{logcol.green}{_log_ln()} {logcol.redb }{str(args)}{logcol.reset}")
@staticmethod
def pr(var):  
  dbg(f"{logcol.greenb}{inspect.getframeinfo(inspect.currentframe().f_back).code_context[0].strip()}:{logcol.cyanb}{var}{logcol.reset}")
@staticmethod
def _msg(args):
  builtins.print(args)
  sys.stdout.flush()
  time.sleep(0)
@staticmethod
def printExcept(e):
  extype = type(e)
  tb = e.__traceback__
  traceback.print_exception(extype, e, tb)
  return  
def throw(ex):
  raise Exception(logcol.redb + "" + ex + logcol.reset)
def trap():
  pdb.pm()
class logcol:
  _bold = "\033[1;24;27;"
  _normal = "\033[0;24;27;"
  black = _normal+"30m"
  red = _normal+"31m"
  green = _normal+"32m"
  yellow = _normal+"33m"
  blue = _normal+"34m"
  magenta = _normal+"35m"
  cyan = _normal+"36m"
  white = _normal+"37m"
  blackb = _bold+"30m"
  redb = _bold+"31m"
  greenb = _bold+"32m"
  yellowb = _bold+"33m"
  blueb = _bold+"34m"
  magentab = _bold+"35m"
  cyanb = _bold+"36m"
  whiteb = _bold+"37m"
  reset = "\033[0m"
  # fmt: on
  # autopep8: on
# endregion