class Medicamento():
    def __init__(self, nome):
        self.__nome = nome

    def __del__(self):
        pass

    # @property
    def nome_medicamento(self):
        return self.__nome
