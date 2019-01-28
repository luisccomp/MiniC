# -*- coding: utf-8 -*-
import lexico
import sintatico
import sys


def tokens(string):
    """
    Dado uma string, essa função retorna uma lista de tokens lexicais resultante desta sequência de caracteres.
    @param string: um trecho de código ou um código fonte completo
    @return: tokens lexicais gerados a partir da string de entrada
    """
    lexer = lexico.get_lexer()
    lexer.input(string)
    toks = []

    while True:
        try:
            tok = lexer.token()
        except lexico.LexError as le:
            sys.stderr.write(str(le) + "\n")

            return []

        if tok:
            toks.append(tok)
        else:
            break

    return toks


def lex(caminho):
    """
    Gera uma lista de tokens lexicais a partir de um arquivo fonte em disco.
    @param caminho: localização do arquivo fonte no disco
    @return: tokens lexicais gerados a partir do arquivo
    """
    # O arquivo fonte é aberto no modo somente leitura
    arquivo = open(caminho, "r")
    toks = tokens(arquivo.read())
    arquivo.close()

    return toks


def parse(caminho):
    """
    Gera uma árvore sintática abstrata a partir de um arquivo fonte.
    @param caminho: localização do arquivo no disco
    @return: AST resultante da análise sintática do arquivo.
    """
    arquivo = open(caminho, "r")
    parser = sintatico.get_parser()
    ast = parser.parse(input=arquivo.read(), lexer=lexico.get_lexer())
    arquivo.close()

    return ast
