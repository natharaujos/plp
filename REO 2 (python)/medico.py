from pessoa import Pessoa


class Medico(Pessoa):
    def __init__(self, nome):
        super().__init__(nome)

    def __del__(self):
        pass

    # @property
    def nome_medico(self):
        return super().get_nome()

    def definir_id(self, identificacao):
        if len(identificacao) > 3:
            print("Identificacao deve ser menor que 3, informe uma nova!")

        else:
            self.identificacao = identificacao
