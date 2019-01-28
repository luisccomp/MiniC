# -*- coding: utf-8 -*-

class No(object):
    """
    Classe base representando os nós da árvore sintática abstrata.
    """

    def __str__(self):
        raise NotImplementedError

    def __repr__(self):
        return self.__str__()


class CmdReturn(No):
    """
    Comando return da linguagem C
    """

    def __init__(self, tipo, valor):
        self.tipo = tipo
        self.valor = valor

    def __str__(self):
        if self.valor is not None:
            return "Return(%s, %s)" % (self.tipo, self.valor)
        else:
            return "Return(%s)" % (self.tipo)


class Argumento(No):
    """
    Representa um argumento de função
    """

    def __init__(self, tipo, nome):
        self.tipo = tipo
        self.nome = nome

    def __str__(self):
        return "Arg(%s, %s)" % (self.tipo, self.nome)


class Funcao(No):
    """
    Representa uma definição de uma função em C
    """

    def __init__(self, tipo_retorno, nome, argumentos, corpo):
        self.tipo_retorno = tipo_retorno
        self.nome = nome
        self.argumentos = argumentos
        # A implementação da função é feita no corpo
        self.corpo = corpo

    def __str__(self):
        return "Função(%s, %s, %s, %s)" % (self.tipo_retorno, self.nome, self.argumentos, self.corpo)
