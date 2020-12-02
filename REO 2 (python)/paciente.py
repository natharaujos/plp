from pessoa import Pessoa


class Paciente(Pessoa):
    total_pessoas = 0

    def __init__(self, nome):
        super().__init__(nome)
        Paciente.total_pessoas += 1

    def __del__(self):
        Paciente.total_pessoas -= 1

    @classmethod
    def pacientes_ativos(self):
        return Paciente.total_pessoas

    def definir_id(self, identificacao):
        if len(identificacao) > 5:
            print("Identificacao deve ser menor que 5, informe uma nova!")
        else:
            self.identificacao = identificacao

    def definir_prontuario(self, prontuario):
        self.prontuario = prontuario

