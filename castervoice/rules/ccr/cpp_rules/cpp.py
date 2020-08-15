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
    "class" : "class ", # Just enters the word "class", see code-snippets for "define class"
    "concept" : "concept ",
    "const" : "const ",
    "const eval" : "consteval ",
    "const expression" : "constexpr ",
    "const INIT" : "constinit ",
    "continue" : "continue;",    
    "default" : "default:",
    "delete" : "delete ", # Note: if confused with "deli", write this as "sea deli"
    "dub" : "double ",
    "E num" : "enum ", # Just enters the word "enum",  No namespace code-snippet, easier to dictate as-is
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
    "namespace" : "namespace ", # Just enters the word "namespace", No namespace code-snippet, easier to dictate as-is
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
    "struct" : "struct ", # Just enters the word "struct",  No namespace code-snippet, easier to dictate as-is
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
            R(Function(_basicKeyword)),
        
        "align as" :
            R(Text("alignas()") + Key("left")),
    
        "align of" :
            R(Text("alignof()") + Key("left")),

        "case" :
            R(Text("case :") + Key("left")),
        
        "declared type" :
            R(Text("decltype()") + Key("left")),
    
        "defined" :
            R(Text("defined()") + Key("left")),
        
        "template" :
            R(Text("template<>") + Key("left")),
            
        "terminate" :
            R(Key("end, semicolon, enter")),
            
        "type eye D" :
            R(Text("typeid()") + Key("left")),
            
        "shared pointer" :
            R(Text("shared_ptr<>") + Key("left")),
        "unique pointer" :
            R(Text("unique_ptr<>") + Key("left")),
        "weak pointer" :
            R(Text("weak_ptr<>") + Key("left")),
    
    }
    extras = [  
        Choice("basicKeyword", _getChoiceMap(basicKeywordMap))
    ]
    defaults = {}


def get_rule():
    return Cpp, RuleDetails(ccrtype=CCRType.GLOBAL)
