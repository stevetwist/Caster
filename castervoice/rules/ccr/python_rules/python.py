'''
@author: stevetwist

Note: commands that utilize code snippets are designed for use with VisualStudio Code
and the Python extension for VS Code.
'''
import time

from dragonfly import Choice, Function

from castervoice.lib.actions import Key, Text
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
    "from" : "st_cs_from",
    "class" : "st_cs_class",
    "derived class" : "st_cs_derived_class",
    "function" : "st_cs_function",
    "method" : "st_cs_method",
    "static method" : "st_cs_static_method",
    "see method" : "st_cs_class_method",
    "if" : "st_cs_if",
    "L if" : "st_cs_elif",
    "else" : "st_cs_else",
    "for" : "st_cs_for",
    "while" : "st_cs_while",
    "try" : "st_cs_try",
    "except" : "st_cs_except",    
    "finally" : "st_cs_finally",
    "with" : "st_cs_with",
    "short with" : "st_cs_short_with",
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
    snippetId = codeSnippetMap[codeSnippet]
    commandChain = []
    for character in snippetId:
        commandChain.append(Key(character))        
    
    command = commandChain[0]
    for c in commandChain[1:]:
        command += c
        
    R(command).execute()
    
    time.sleep(0.5) # Wait for intellisense
    
    R(Key('tab')).execute()
    

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
