'''
@author: stevetwist

Note: commands that utilize code snippets are designed for use with VisualStudio Code
and the Python extension for VS Code.
'''
from dragonfly import Choice, Function

from castervoice.lib.actions import Text
from castervoice.lib.const import CCRType
from castervoice.lib.ctrl.mgr.rule_details import RuleDetails
from castervoice.lib.merge.mergerule import MergeRule
from castervoice.lib.merge.state.short import R

basicKeywordMap = {
    "bit shift left" : " << ",
    "bit shift right" : " >> ",
    "bitwise and" : " & ",
    "bitwise or" : " | ",
    "bitwise complement" : "~",
    "bitwise (exclusive|ex) or" : " ^ ",
    "and" : " and ",
    "as" : " as ",
    "break" : "break ",
    "continue" : "continue ",
    "pie deli" : "del ",
    "false" : "False",
    "global" : "global ",
    "in" : " in ",
    "import" : "import ",
    "is" : " is ",
    "none" : "None",
    "not" : "not ",
    "or" : " or ",
    "pass" : "pass ",
    "raise" : "raise ",
    "return" : "return ",
    "true" : "True",    
}

codeSnippetMap = {
    "from" : "from",
    "class" : "class", # TODO: Code snippet: Also include def __init__(self):\n\tpass
    "derived class" : "derived class", # TODO: Code snippet: Also include def __init__(self):\n\t<BASE CLASS>.__init__(self)
    "function" : "function",
    "method" : "method",
    "static method" : "static method",
    "see method" : "class method",
    "if" : "if",      
    "L if" : "elif",
    "else" : "else",        
    "for" : "for",        
    "while" : "while",      
    "try" : "try",
    "except" : "except",
    "finally" : "finally",
    "with" : "with",# TODO: Code snippet: with <TOKEN> as <TOKEN>:
    "short with" : "short with", # TODO: Code snippet: with <TOKEN>:
}


def _getChoiceMap(mapVariable):
    choiceMap = {}
    for key in mapVariable:
        choiceMap[key] = key
        
    return choiceMap


def _basicKeyword(basicKeyword):
    text = basicKeywordMap[basicKeyword]
    R(Text(text)).execute()
    
    
def _codeSnippet(codeSnippet):
    print ("TODO: Execute code snippet: %s" % codeSnippet)


class Python(MergeRule):

    mapping = { 
        "<basicKeyword>" :
            R(Function(_basicKeyword)),
        "<codeSnippet>" :
            R(Function(_codeSnippet)),
     
        # VisualStudio Code Helpers
        #
        # VS Code Helpers
        #   line <number>
        #   eventually: debugging helpers (step in, step over, step out, debug continue, etc.)
        #   eventually: tab navigation
        #   ideally: "go to definition" for text under cursor (or, failing that, for hovered text)
    }
    extras = [  
        Choice("basicKeyword", _getChoiceMap(basicKeywordMap)),
        Choice("codeSnippet", _getChoiceMap(codeSnippetMap))
    ]
    defaults = {}


def get_rule():
    return Python, RuleDetails(ccrtype=CCRType.GLOBAL)
