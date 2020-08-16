import time

from dragonfly import Choice, Dictation, Function, MappingRule, Pause, Repeat

from castervoice.lib.actions import Text, Key
from castervoice.lib.ctrl.mgr.rule_details import RuleDetails
from castervoice.lib.merge.additions import IntegerRefST
from castervoice.lib.merge.state.short import R

from castervoice.rules.core.numbers_rules import words_to_numbers

# NOTE: Visual Studio hotkeys based on configuring Visual Studio for the C++ environment
# Some changes were made:
#   Assign Shift+Alt+a to "Project.NewFolder" in Global
#   Assign Shift+F12 to "Edit.FindAllReferences" in Global
#   Assign Ctrl+Shift+Alt+F8 to "Build.RunCodeAnalysisonProject" in Global
#   Assign Ctrl+Shift+Alt+F9 to "Build.SolutionConfigurations" in Global
#   Assign Ctrl+Shift+Alt+F10 to "Build.SolutionPlatforms" in Global


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


def _configuartion(n):
    R(Key("cas-f9") + Pause("20")).execute()
    R(Key("home")).execute()
    for i in range(n-1):
        R(Key("down")).execute()
    R(Key("enter")).execute()


def _platform(n):
    R(Key("cas-f10") + Pause("20")).execute()
    R(Key("home")).execute()
    for i in range(n-1):
        R(Key("down")).execute()
    R(Key("enter")).execute()


def _elseIf():
    R(Text("else ")).execute()
    _codeSnippet("if")
    

class CppNon(MappingRule):
    mapping = {
        "<codeSnippet>" :
            R(Function(_codeSnippet)),
        "L if" : 
            R(Function(_elseIf)),
            
        "toggle comment" :
            R(Key("c-k") + Pause("20") + Key("c-slash")),        
        "comment" :
            R(Text("// ")),
        "big comment" :
            R(Text("/*\n/*")),
            
        "line <numbers>":
            R(Function(_goToLine)),
            
        "analyze file":
            R(Key("csa-f7")),
        "analyze project":
            R(Key("csa-f8")),
        "analyze solution":
            R(Key("a-f11")),
            
        "format": # Apply formatting to document
            R(Key("c-k") + Pause("20") + Key("c-d")), 
            
        "next issue":
            R(Key("a-pgdown")),
        "previous issue":
            R(Key("a-pgup")),
            
        "step in [<n>]":
            R(Key("f11"))* Repeat(extra="n"),
        "step out [<n>]":
            R(Key("s-f11"))* Repeat(extra="n"),
        "step over [<n>]":
            R(Key("f10"))* Repeat(extra="n"),
        "debug [continue]":
            R(Key("f5")),
        "run":
            R(Key("c-f5")),
        "debug stop":
            R(Key("s-f5")),
            
        "build": # Build project
            R(Key("c-b")),            
        "build solution":
            R(Key("f7")),
            
        "breakpoint":
            R(Key("f9")),
                        
        "bookmark": # Toggle bookmark on current line
            R(Key("c-k") + Pause("20") + Key("c-k")), 
        "next bookmark [<n>]":
            R(Key("f2"))* Repeat(extra="n"),
        "previous bookmark [<n>]":
            R(Key("s-f2"))* Repeat(extra="n"),
            
        "go definition":
            R(Key("f12")),
        "peek definition":
            R(Key("a-f12")),
        "find references":
            R(Key("s-f12")),
        
        "quick actions": # Use this to create definition, copy signature, move definition (toggle between header/source) and so on
            R(Key("c-.")),
    
        "go bracket": # Only works if bracket currently under cursor
            R(Key("c-]")),
        "select bracket": # Only works if bracket currently under cursor
            R(Key("cs-]")),
            
        "fold all":
            R(Key("c-m") + Pause("20") + Key("c-a")),
        "fold to definitions":
            R(Key("c-m") + Pause("20") + Key("c-o")),
        "[toggle] (fold|unfold)":
            R(Key("c-m") + Pause("20") + Key("c-m")),        
        "unfold all":
            R(Key("c-m") + Pause("20") + Key("c-l")),          
        
        "next tab [<n>]":
            R(Key("ca-pgdown/20"))*Repeat(extra="n"),
        "previous tab [<n>]":
            R(Key("ca-pgup/20"))*Repeat(extra="n"),
        "close tab [<n>]":
            R(Key("c-f4/20"))*Repeat(extra="n"),
        "keep tab":
            R(Key("ca-home")),
        
        "(focus|show) explorer":
            R(Key("ca-l")), # Navigate with up/down/left/right, press enter to open selected file        
        "add new folder":
            R(Key("sa-a")),
        "add new header":
            R(Key("cs-a") + Pause("20") + Key("c-e") + Pause("20") + Text("Header File (.h)") + Pause("200") + Key("tab/20:2") + Pause("20") + Key("home,c-delete")),            
        "add new source file":
            R(Key("cs-a") + Pause("20") + Key("c-e") + Pause("20") + Text("C++ File (.cpp)") + Pause("200") + Key("tab/20:2") + Pause("20") + Key("home,c-delete")),
        # TODO: Can add any "add new..." command, such as "Add new compute shader"
        #       Will also need to figure out configuring said shader to compile correctly, ideally via Visual Studio
            

        "(focus|show) class view": # Note: if you "copy" on an entry, it copies the fully qualified name to the clipboard. Cannot paste via caster, must say "press ctrl v"
            R(Key("cs-c")),
        "(focus|show) output":
            R(Key("a-2")),
        "(focus|show) error list": # Can navigate with up/down, then press enter to go to selected error
            R(Key("c-backslash") + Pause("20") + Key("e")),
        "(focus|show) test explorer":
            R(Key("c-e") + Pause("20") + Key("t")),
        
        "(focus|show) bookmarks":
            R(Key("c-k") + Pause("20") + Key("c-w")), 
               
        "(show|view) call hierarchy":
            R(Key("c-k") + Pause("20") + Key("c-t")), 
                              
        "search explorer":
            R(Key("c-;")),
            
        "go file":
            R(Key("cs-t")),
        "go type":
            R(Key("c-1") + Pause("20") + Key("c-t")),
        "go member":
            R(Key("a-backslash")),
        "go symbol":
            R(Key("c-1") + Pause("20") + Key("c-s")),
            
        "hover" :
            R(Key("c-k") + Pause("20") + Key("c-i")),
        
        "expand [<n>]":
            R(Key("sa-equals")) * Repeat(extra="n"),
        "shrink [<n>]":
            R(Key("sa-minus")) * Repeat(extra="n"),
            
        "scroll up [<n>]":
            R(Key("c-up")*Repeat(extra='n')),
        "scroll down [<n>]":
            R(Key("c-down")*Repeat(extra='n')),
            
        "delete line":
            R(Key("s-del")),
            
        "configuration <n>":
            R(Function(_configuartion)),     
        "platform <n>":
            R(Function(_platform)),
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
