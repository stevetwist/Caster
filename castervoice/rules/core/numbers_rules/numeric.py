from dragonfly import Choice, Dictation, Function, MappingRule, Text

try:  # Try first loading from caster user directory
    from numeric_support import word_number, numbers2
except ImportError: 
    from castervoice.rules.core.numbers_rules.numeric_support import word_number, numbers2
    
from castervoice.lib.const import CCRType
from castervoice.lib.ctrl.mgr.rule_details import RuleDetails
from castervoice.lib.merge.additions import IntegerRefST
from castervoice.lib.merge.state.short import R

from word2number import w2n

def _processNumbers(minus, numbers, literal_suffix):    
    numberWordsStr = str(numbers)
    numberWordsStr = numberWordsStr.replace('.',' point ')
    
    try:
        numbersStr = str(w2n.word_to_num(numberWordsStr))
    except:
        print ("ERROR: Invalid numbers: %s" % numbers)
        return
    
    Text(minus + numbersStr + literal_suffix).execute()
    
    
class Numbers(MappingRule):
    mapping = {
        "word numb <wn>":
            R(Function(word_number, extra="wn")),
        #"numb <wnKK>":
        #    R(Function(numbers2, extra="wnKK"),
        #      rspec="Number"),
        "numb [<minus>] <numbers> [<literal_suffix>]":
            R(Function(_processNumbers))
    }

    extras = [
        IntegerRefST("wn", 0, 10),
        IntegerRefST("wnKK", 0, 1000000),
        Choice("minus", { "minus" : "-", "negative" : "-" }),
        Dictation("numbers"),
        Choice("literal_suffix", { "F" : "f", "f" : "f", "foxy" : "f", "foxtrot" : "f" })
    ]
    defaults = {
        "minus" : "",
        "literal_suffix" : ""
    }


def get_rule():
    return Numbers, RuleDetails(name="numbers")
