import time

from dragonfly import Choice, Dictation, Function, MappingRule, Pause, Repeat

from castervoice.lib.actions import Text, Key
from castervoice.lib.ctrl.mgr.rule_details import RuleDetails
from castervoice.lib.merge.additions import IntegerRefST
from castervoice.lib.merge.state.short import R

from castervoice.rules.core.numbers_rules import words_to_numbers

# VS helpers:    
# As many as we can from python, including comment, big comment, and so on.


codeSnippetMap = {
    "if" : "stcsif",    
    "else" : "stcselse",
    "switch" : "stcsswitch",
    "do while" : "stcsdo",
    "while" : "stcswhile",
    "for" : "stcsfor",    
    "range for" : "stcsrfor",    
    "try" : "stcstry",
    "catch" : "stcscatch",
    "const cast" : "stcsconstcast",
    "dynamic cast" : "stcsdynamiccast",
    "reinterpret cast" : "stcsreinterpretcast",
    "static cast" : "stcsstaticcast",
    "static assert" : "stcsstaticassert",
    "define class" : "stcsclass",
    "define derived class" : "stcsclassderived",
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


def _goToLine(numbers):
    numbersStr = words_to_numbers.wordsToNumbers(str(numbers))    
    R(Key('c-g')).execute()
    time.sleep(0.5) # Wait for popup
    
    for character in numbersStr:
        R(Key(character)).execute()
        
    R(Key('enter')).execute()


def _elseIf():
    R(Text("else ")).execute()
    _codeSnippet("if")
    

class CppNon(MappingRule):
    mapping = {
        "<codeSnippet>" :
            R(Function(_codeSnippet)),
        "L if" : 
            R(Function(_elseIf)),
            
        #"comment" : 
        #    R(Key("c-slash")),
        #"big comment" :
        #    R(Key("sa-a")),
        #"line <numbers>":
        #    R(Function(_goToLine)),
            
        #"step in [<n>]":
        #    R(Key("f11"))* Repeat(extra="n"),
        #"step out [<n>]":
        #    R(Key("s-f11"))* Repeat(extra="n"),
        #"step over [<n>]":
        #    R(Key("f10"))* Repeat(extra="n"),
        #"debug [continue]":
        #    R(Key("f5")),
        #"debug stop":
        #    R(Key("s-f5")),
            
        #"breakpoint":
        #    R(Key("f9")),
            
        #"go definition":
        #    R(Key("f12")),
        #"peek definition":
        #    R(Key("a-f12")),
        #"side definition":
        #    R(Key("c-k") + Pause("20") + Key("f12")),
            
        #"peek references":
        #    R(Key("s-f12")),
            
        #"show command palette":
        #    R(Key("cs-p")),
            
        #"go bracket":
        #    R(Key("cs-backslash")),
            
        #"fold":
        #    R(Key("cs-[")),
        #"unfold":
        #    R(Key("cs-]")),
        #"fold all":
        #    R(Key("c-k") + Pause("20") + Key("c-0")),
        #"unfold all":
        #    R(Key("c-k") + Pause("20") + Key("c-j")),            
        
        #"next tab [<n>]":
        #    R(Key("c-k") + Pause("20") + Key("c-pgdown")) * Repeat(extra="n"),
        #"previous tab [<n>]":
        #    R(Key("c-k") + Pause("20") + Key("c-pgup")) * Repeat(extra="n"),
        #"close tab [<n>]":
        #    R(Key("c-w/20"))*Repeat(extra="n"),
        #"split editor":
        #    R(Key("c-backslash")),
        #"close editor":
        #    R(Key("c-f4")),
        #"next editor [<n>]":
        #    R(Key("c-k") + Pause("20") + Key("c-right")) * Repeat(extra="n"),
        #"previous editor [<n>]":
        #    R(Key("c-k") + Pause("20") + Key("c-left")) * Repeat(extra="n"),
        #"(focus|show) explorer":
        #    R(Key("cs-e")), # Navigate with up/down/left/right, press enter to open selected file        
        #"hide explorer":
        #    R(Key("c-b")),
        #"focus editor":
        #    R(Key("c-1")),
        #"[focus] terminal":
        #    R(Key("c-backtick")),
            
            
        #"search for file":
        #    R(Key("c-p")),
            
        #"go symbol" :
        #    R(Key("cs-o") + Pause("20") + Key("colon")),
            
        #"hover" :
        #    R(Key("c-k") + Pause("20") + Key("c-i")),
        #"IntelliSense" :
        #    R(Key("c-space")),
        
        #"expand [<n>]":
        #    R(Key("sa-right")) * Repeat(extra="n"),
        #"shrink [<n>]":
        #    R(Key("sa-left")) * Repeat(extra="n"),
            
        #"scroll up [<n>]":
        #    R(Key("c-up")*Repeat(extra='n')),
        #"scroll down [<n>]":
        #    R(Key("c-down")*Repeat(extra='n')),
        #"scroll page up [<n>]":
        #    R(Key("a-pgup")*Repeat(extra='n')),
        #"scroll page down [<n>]":
        #    R(Key("a-pgdown")*Repeat(extra='n')),
            
        #"delete line":
        #    R(Key("s-del")),
    }
    
    extras = [  
        Choice("codeSnippet", _getChoiceMap(codeSnippetMap)),
        Dictation("numbers"),
        IntegerRefST("n", 1, 3000),
    ]
    
    defaults = {
        "n": 1,
    }


def get_rule():
    return CppNon, RuleDetails("cpp companion")
