# -*- coding: utf-8 -*-
from lexico import tokens
from ply.yacc import yacc

import ast


class ParseError(Exception):
    # Os erros de análise sintática serão tratados por esta classe

    def __init__(self, mensagem):
        self.mensagem = mensagem

    def __str__(self):
        return "ParseError: %s" % (self.mensagem)


# Retorna uma instância do parser
def get_parser():

    return yacc()
