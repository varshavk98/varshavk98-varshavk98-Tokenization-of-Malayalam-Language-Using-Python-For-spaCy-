# coding: utf8
from __future__ import unicode_literals

from .stop_words import STOP_WORDS
from .lex_attrs import LEX_ATTRS

from ...language import Language
from ...attrs import LANG


class MalayalamDefaults(Language.Defaults):
    lex_attr_getters = dict(Language.Defaults.lex_attr_getters)
    lex_attr_getters.update(LEX_ATTRS)
    lex_attr_getters[LANG] = lambda text: "ml"
    stop_words = STOP_WORDS


class Malayalam(Language):
    lang = "ml"
    Defaults = MalayalamDefaults


__all__ = ["Malayalam"]
