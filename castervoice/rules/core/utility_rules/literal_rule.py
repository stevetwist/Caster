from dragonfly import Choice, Dictation, Function

from castervoice.lib.actions import Text    
from castervoice.lib.const import CCRType
from castervoice.lib.ctrl.mgr.rule_details import RuleDetails
from castervoice.lib.merge.mergerule import MergeRule
import castervoice.lib.textformat


def _writeText(capitalization, words):
    spacing = 0 # ace (normal spacing)
    Text(castervoice.lib.textformat.TextFormat.formatted_text(capitalization, spacing, str(words))).execute()

class Literal(MergeRule):
    pronunciation = "literal"
    mapping = {
        "literal <capitalization> <words> literal": Function(_writeText),
    }

    extras = [
        Dictation("words"),
        Choice("capitalization", {            
            "yell": 1,
            "tie": 2,
            "camel": 3,
            "sing": 4,
            "laws": 5,
            "say": 6,
            "cop": 7,
            "slip": 8,
        })
    ]
    defaults = {}


def get_rule():
    return Literal, RuleDetails(ccrtype=CCRType.GLOBAL)
