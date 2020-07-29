'''
@author: stevetwist

Note: commands that utilize code snippets are designed for use with VisualStudio Code
and the Python extension for VS Code.
'''
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

def _getChoiceMap(mapVariable):
    choiceMap = {}
    for key in mapVariable:
        choiceMap[key] = key
        
    return choiceMap


def _basicKeyword(basicKeyword):
    text = basicKeywordMap[basicKeyword]
    R(Text(text)).execute()
    


class Python(MergeRule):

    mapping = { 
        "<basicKeyword>" :
            R(Function(_basicKeyword)),
    }
    extras = [  
        Choice("basicKeyword", _getChoiceMap(basicKeywordMap))
    ]
    defaults = {}


def get_rule():
    return Python, RuleDetails(ccrtype=CCRType.GLOBAL)
