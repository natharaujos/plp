from medico import Medico


class Prontuario:

    def __init__(self):
        self.__lista = []

    def __del__(self):
        pass

    # @property
    def exibe_prontuario(self):
        self.exibe = ''

        for x in self.__lista:
            self.exibe = self.exibe + '{} - {} - {} -{} - {} '.format(x['medicamento'], x['posologia'], x['medico'],
                                                                      x['data'], x['hora'])
            self.exibe = self.exibe + '\n'
        return print(self.exibe)

    def insere_procedimento(self, medicamento, posologia, medico, data, hora):
        nomeMedico = medico.nome_medico()
        nomeMedicamento = medicamento.nome_medicamento()
        __dicionario = {'medicamento': nomeMedicamento, 'posologia': posologia, 'medico': nomeMedico, 'data': data,
                        'hora': hora}
        self.__lista.append(__dicionario)
