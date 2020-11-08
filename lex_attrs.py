# coding: utf8
from __future__ import unicode_literals

from ..norm_exceptions import BASE_NORMS
from ...attrs import NORM, LIKE_NUM


# fmt: off
_stem_suffixes = [
	[" ി"," ീ"," ു"," ൂ"," ൃ"," ൄ"," ൢ"," ൣ"," െ"," േ"," ൊ"," ോ"," ാ"," ം "," ഃ",],
	[" ുന്നു"," ിച്ചു","ഞു"," ിരുന്നു"," ിട്ടുണ്ട്"," ിക്കാം","യൂ","ക്കൂ","ക്കും","യ്യും"," ുമോ","ട്ടെ","പ്പെട്ടു","ട്ടിരുന്നു"," ാലും","ങ്ങള്‍","കള്‍","ക്കാന്‍"," ിട്ട്"]]


_num_words = [
	"ഒന്ന്",
	"രണ്ട്",
	"മുന്ന്",
	"നാല്‌",
	"അഞ്ച്",
	"അറ്",
	"ഏഴ്",
	"എട്ട്",
	"ഒന്‍പത്",
	"പത്ത്",
	"പതിനൊന്ന്",
	"പന്ത്രണ്ട്",
	"പതി മുന്നു",
	"പതിനാല്",
	"പതിനഞ്ച്",
	"പതിനാറ്",
	"പതിനേഴ്",
	"പതിനെട്ട്",
	"പത്തൊമ്പതു",
	"ഇരുപത്",
	"നൂര്",
	"ആയിരം",
	"പത്തുലക്ഷം"]

def norm(string):
    
    if string in BASE_NORMS:
        return BASE_NORMS[string]   
    for suffix_group in reversed(_stem_suffixes):
        length = len(suffix_group[0])
        if len(string) <= length:
            break
        for suffix in suffix_group:
            if string.endswith(suffix):
                return string[:-length]
    return string


def like_num(text):
    if text.startswith(("+", "-", "±", "~")):
        text = text[1:]
    text = text.replace(", ", "").replace(".", "")
    if text.isdigit():
        return True
    if text.count("/") == 1:
        num, denom = text.split("/")
        if num.isdigit() and denom.isdigit():
            return True
    if text.lower() in _num_words:
        return True
    return False


LEX_ATTRS = {NORM: norm, LIKE_NUM: like_num}

