'''
@author: stevetwist

Note: commands that utilize code snippets are designed for use with VisualStudio

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
    
    "logical and" : " && ",
    "logical or" : " || ",
    "not" : "!",
    
    # c++ keywords (non-code-snippet. See cpp2.py for code-snippets)    
    # NOTE: Define variables so they read right-to-left, such as:
    # "int const pointer const" -> "int const * const " (constant pointer to constant int)
    # "int reference" -> "int & "
    # "int double reference" -> "int && "
    "auto" : "auto ",
    "bool" : "bool ",
    "break" : "break;",
    "car" : "char ",
    "class" : "class ", # Just enters the word "class", see code-snippets for declare/define class
    "concept" : "concept ",
    "const" : "const ",
    "const eval" : "consteval ",
    "const expression" : "constexpr ",
    "const INIT" : "constinit ",
    "continue" : "continue;",    
    "default" : "default:",
    "delete" : "delete ", # Note: if confused with "deli", write this as "sea deli"
    "dub" : "double ",
    "explicit" : "explicit ",
    "export" : "export ",
    "extern" : "extern ",
    "false" : "false",
    "final" : "final ",
    "float" : "float ",
    "friend" : "friend ",
    "import" : "import ",
    "in line" : "inline ",
    "INT" : "int ",
    "long" : "long ",
    "module" : "module ",
    "mutable" : "mutable ",
    "namespace" : "namespace ", # Just enters the word "namespace", see code-snippets for define namespace
    "new" : "new ",
    "no except" : "noexcept", # Note: no space, as it is the last part of a function declaration
    "null pointer" : "nullptr",
    "operator" : "operator", # Note: no space, as typical usage is "operator==", for example
    "override" : "override ",
    "private" : "private", # Note: no space. Can either do "private colon enter" or "private ace", as required
    "protected" : "protected", # Note: no space. Can either do "protected colon enter" or "protected ace", as required
    "public" : "public", # Note: no space. Can either do "public colon enter" or "public ace", as required
    "requires" : "requires ",
    "return" : "return ",
    "short return" : "return;",
    "type short" : "short ",
    "signed" : "signed ",
    "static" : "static ",   
    "this" : "this",
    "throw" : "throw ",
    "to do" : "TODO: ",
    "true" : "true",
    "type name" : "typename ",
    "unsigned" : "unsigned ",
    "using" : "using ",
    "virtual" : "virtual ",
    "void" : "void ",
    "volatile" : "volatile ",
    
    # C++ preprocessor
    "hash include" : "#include ",
    "hash if" : "#if ",
    "hash L if" : "#elif ",
    "hash else" : "#else ",
    "hash end if" : "#endif ",
    "hash define" : "#define ",
    "hash un (deaf|define)" : "#undef ",
    "hash pragma" : "#pragma ",
    
    # c++ helpers
    "arrow" : "->",
    "pointer" : "* ",
    "de reference" : "*",
    "address" : "&",
    "reference" : "& ",
    "double reference" : "&& ",
    "scope" : "::",
    "standard" : "std::",
            
    # Commands that move the cursor:
    # "terminate" -> "(end);(newline)"
    # "align as" : "alignas(%1)",
    # "align of" : "alignof(%1)",
    # "declared type" : "decltype(%1)",
    # "template" : "template<%1>"
    # "type eye D" : "typeid(%1)"
    # "defined" : "defined(%1)"
    # "shared pointer" : "shared_ptr<%1>"
    #       same for weak_ptr and unique_ptr
    
    # Code snippets
    # "constant cast" : "const_cast<%1>(%2)"
    # "dynamic_cast", "reinterpret_cast", "static_cast"
    # "static assert"
    # for, including "range for"    
    # "case <%>:"
    # "catch", "try",
    # "declare class", "define class"
    #       same for struct
    #       same for union
    #       same for function
    # "if","elif","else"
    # while, do while,
    # switch
    # "declare namespace"
    # "declare enum class", "define enum class", "declare enum class with type", "define enum class with type"    
        # "e num" (gives an enum class) -> places cursor ready for name. "with type" also has ": <type>"
        # declare vs define change if it's ";" or "{\n}"
    # lambda
    
    # VS helpers:    
    # As many as we can from python, including comment, big comment, and so on.
}


def _getChoiceMap(mapVariable):
    choiceMap = {}
    for key in mapVariable:
        choiceMap[key] = key
        
    return choiceMap


def _basicKeyword(basicKeyword):
    text = basicKeywordMap[basicKeyword]
    R(Text(text)).execute()
    


class Cpp(MergeRule):
    pronunciation = "C plus plus"
    
    mapping = { 
        "<basicKeyword>" :
            R(Function(_basicKeyword))
    }
    extras = [  
        Choice("basicKeyword", _getChoiceMap(basicKeywordMap))
    ]
    defaults = {}


def get_rule():
    return Cpp, RuleDetails(ccrtype=CCRType.GLOBAL)
