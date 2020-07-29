import time

from dragonfly import Choice, Function, MappingRule

from castervoice.lib.actions import Text, Key
from castervoice.lib.ctrl.mgr.rule_details import RuleDetails
from castervoice.lib.merge.state.short import R

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


class PythonNon(MappingRule):
    mapping = {
        "<codeSnippet>" :
            R(Function(_codeSnippet)),
        "comment" : 
            R(Key("c-slash")),
        "big comment" :
            R(Key("sa-a")),    
    }
    
    extras = [  
        Choice("codeSnippet", _getChoiceMap(codeSnippetMap))
    ]
    defaults = {}


def get_rule():
    return PythonNon, RuleDetails("python companion")
