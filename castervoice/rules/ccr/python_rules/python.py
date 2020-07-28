'''
@author: stevetwist

Note: commands that utilize code snippets are designed for use with VisualStudio Code
and the Python extension for VS Code.
'''
from dragonfly import Pause, Dictation, Choice

from castervoice.lib.actions import Text, Key
from castervoice.rules.ccr.standard import SymbolSpecs
from castervoice.lib.const import CCRType
from castervoice.lib.ctrl.mgr.rule_details import RuleDetails
from castervoice.lib.merge.mergerule import MergeRule
from castervoice.lib.merge.state.short import R
from castervoice.lib.temporary import Store, Retrieve


class Python(MergeRule):

    mapping = { 
        "bit shift left":
            R(Text(" << ")),
        "bit shift right":
            R(Text(" >> ")),
        "bitwise and":
            R(Text(" & ")),
        "bitwise or":
            R(Text(" | ")),
        "bitwise complement":
            R(Text(" ~")),
        "bitwise (exclusive|ex) or":
            R(Text(" ^ ")),
        "and":
            R(Text(" and ")),    
        "break":
            R(Text("break ")),
        "continue":
            R(Text("continue ")),
        "pie deli": # py deli
            R(Text("del ")),
        "false":
            R(Text("False")),        
        "in":
            R(Text(" in ")),
        "is":
            R(Text(" is ")),
        "none":
            R(Text("None")),
        "not":
            R(Text("not ")),        
        "or":
            R(Text(" or ")),    
        "pass":
            R(Text("pass ")),        
        "true":
            R(Text("True")),
        
        # import (simple word "import ")
        # as -> simple text (" as ")
        # global -> simple text "global "
        # raise -> simple text ("raise ")
        # return -> (simple text ("return ")
        
        # from -> should be a code snippet: from <token> import <token>
        # class -> code snippet
        # derived class -> code snippet
        # method, static method, class method, function -> code snippets
        # if, elif, else -> code snippets
        # try-except, try-finally, try-except-finally -> code snippets
        # for -> code snippet: for <TOKEN> in <TOKEN>:\n<TOKEN=pass>        
        # while -> code snippet
        # with -> code snippet (with <TOKEN> as <TOKEN>:)
        # short with -> code snippet (with <TOKEN>:)
        # helpers?
        #   init -> "__init__"
        #   "dunder" -> "__" (possibly in punctuation)
        #
        # VS Code Helpers
        #   line <number>
        #   eventually: debugging helpers (step in, step over, step out, debug continue, etc.)
    }

    extras = [        
    ]
    defaults = {}


def get_rule():
    return Python, RuleDetails(ccrtype=CCRType.GLOBAL)
