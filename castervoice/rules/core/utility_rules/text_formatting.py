from dragonfly import Dictation, MappingRule, Function, Choice

from castervoice.lib.ctrl.mgr.rule_details import RuleDetails
from castervoice.lib.merge.state.short import R
import castervoice.lib.textformat

capitalizationMap = {
    "yell": 1,
    "tie": 2,
    "camel": 3,
    "sing": 4,
    "laws": 5,
    "say": 6,
    "cop": 7,
    "slip": 8,
}

spacingMap = {
    "ace": 0,
    "gum": 1,
    "gun": 1,
    "kebab": 2,
    "snake": 3,
    "pebble": 4,
    "incline": 5,
    "dissent": 6,
    "descent": 6,
}


class TextFormatting(MappingRule):
    mapping = {        
        "(<capitalization> <spacing> | <capitalization> | <spacing>) [(bow|bowel)] <textnv> [brunt]":
            R(Function(castervoice.lib.textformat.master_format_text)),
    }
    extras = [
        Dictation("textnv"),
        Choice("capitalization", capitalizationMap),
        Choice("spacing", spacingMap),
    ]
    defaults = {       
        "textnv": "",
        "capitalization": 0,
        "spacing": -1,       
    }

def get_rule():
    return TextFormatting, RuleDetails(name="text formatting")
