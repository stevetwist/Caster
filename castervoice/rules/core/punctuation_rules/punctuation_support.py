import dragonfly


def double_text_punc_dict():
    return {
        "double quote":                        "\"\"",
        "double chicky":                       "''",
        "double ticky":                        "``",
        "par":                                 "()",
        "brax":                                "[]",
        "curly":                               "{}",
        "angle":                               "<>",
    }


def _inv_dtpb():
    return {v: k for k, v in double_text_punc_dict().items()}


def text_punc_dict():
    # Insurers comma is recognized consistently with DNS/Natlink and
    # if/else statement workaround engines that do not expect punctuation symbol as a command
    if (dragonfly.get_current_engine().name == 'natlink'):
        comma = "(comma | ,)"
    else:
        comma = "comma"

    _id = _inv_dtpb()
    return {
        "ace":                                                " ",
        "bang":                                               "!",
        "quote":                                             "\"",
        "hash tag":                                           "#",
        "dollar":                                             "$",
        "mod":                                                " % ",
        "short mod":                                          "%",
        "mod eek":                                           " %= ",
        "short mod eek":                                      "%=",
        "ampersand":                                          "&",
        "apostrophe | chicky":                                "'",
        "open " + _id["()"]:                                  "(",
        "close " + _id["()"]:                                 ")",
        "(star | short times)":                               "*",
        "times":                                              " * ",
        "times eek":                                          " *= ",
        "short times eek":                                    "*=",
        "plus":                                               " + ",
        "short plus":                                         "+",
        "double plus":                                        "++",        
        "plus eek":                                          " += ",
        "short plus eek":                                     "+=",
        comma:                                                ", ",
        "short %s" % comma:                                   ",",
        "minus":                                              " - ",
        "short minus":                                        "-",
        "double minus":                                       "--",        
        "minus eek":                                         " -= ",
        "short minus eek":                                    "-=",
        "period":                                             ". ",
        "dot":                                                ".",
        "(slash | short divide)":                             "/",
        "divide":                                            " / ",        
        "divide eek":                                        " /= ",
        "short divide eek":                                   "/=",
        "colon":                                              ":",
        "semicolon":                                          ";",
        "less than":                                          " < ",
        "open " + _id["<>"]:                                  "<",
        "less eek":                                           " <= ",
        "equals":                                             " = ",
        "short equals":                                       "=",
        "equal to":                                           " == ",
        "not eek":                                            " != ",
        "greater than":                                       " > ",
        "close " + _id["<>"]:                                 ">",
        "greater eek":                                        " >= ",
        "question":                                           "?",
        "(atty | at symbol)":                                 "@",
        "open " + _id["[]"]:                                  "[",
        "backslash":                                         "\\",
        "double backslash":                                  "\\\\",
        "close " + _id["[]"]:                                 "]",
        "carrot":                                             "^",
        "underscore":                                         "_",
        "(double underscore|dunder)":                         "__",
        "ticky":                                              "`",
        "open " + _id["{}"]:                                  "{",
        "pipe (sim | symbol)":                                "|",
        "close " + _id["{}"]:                                 "}",
        "tilde":                                              "~",
    }
