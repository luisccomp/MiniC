# -*- coding: utf-8 -*-
from ply.lex import TOKEN
from ply.lex import lex


class LexError(Exception):
    # Os erros do analisador léxico serão lançados na forma de Exceptions para o programa principal tratar

    def __init__(self, mensagem):
        self.mensagem = mensagem

    def __str__(self):
        return "LexError: %s" % (self.mensagem)


def coluna(lexer):
    # Retorna a coluna onde o ponteiro do analisador léxico se encontra
    inicio_linha = lexer.lexdata.rfind("\n", 0, lexer.lexpos) + 1

    return (lexer.lexpos - inicio_linha) + 1



# Palavras reservadas da mini linguagem
reserved = {
    "int": "INT",
    "return": "RETURN",
    "void": "VOID",
    "float": "FLOAT"
}

# Tokens lexicais da mini linguagem
tokens = [
    "ID",
    "APAR",
    "FPAR",
    "ACHAVE",
    "FCHAVE",
    "PTOVIRG",
    "LITINT",
    "VIRG"
] + list(reserved.values())


# Regras de produção de tokens lexicais
t_APAR = r"\("
t_FPAR = r"\)"
t_ACHAVE = r"{"
t_FCHAVE = r"}"
t_PTOVIRG = r";"
t_VIRG = r","


@TOKEN(r"[a-zA-Z_][a-zA-Z0-9_]*")
def t_ID(t):
    t.type = reserved.get(t.value, "ID")

    return t


@TOKEN(r"[0-9]+")
def t_LITINT(t):
    # Gerando um literal inteiro. Ele só gera um literal inteiro dentro do intervalo de 64 bits. Caso contrário ele
    # lança uma exceção.
    valor = int(t.value)

    if valor < -2**64 or valor > 2**64-1:
        raise LexError("%d-%d: Valor inteiro fora do intervalo de 64 bits!" % (t.lexer.lineno, coluna(t.lexer)))

    t.value = valor

    return t


@TOKEN(r"//[^\n\r]*")
def t_comentario(t):
    # O token do comentário é descartado
    pass


def t_error(t):
    # Trata caracteres deconhecidos da linguagem
    raise LexError("%d-%d: Caractere desconhecido '%s'" % (t.lexer.lineno, coluna(t.lexer), t.value[0]))


# Simbolos ignorados
t_ignore = " \t"


@TOKEN(r"\n+")
# Atualiza o contador de linhas do analisador léxico
def t_novalinha(t):
    t.lexer.lineno += t.value.count("\n")


# Retorna uma instância do analisador léxico
def get_lexer():

    return lex()
