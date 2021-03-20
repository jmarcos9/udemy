from time import sleep
from datetime import datetime


class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo')
            return
        if self.falando:
            print(f'{self.nome} já está falando')
            return
        print(f'{self.nome} está falando sobre {assunto}')
        self.falando = True

    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando')
            return
        print(f'{self.nome} parou de falar')
        self.falando = False

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo')
            return
        if self.falando:
            print(f'{self.nome} não pode comer está falando')
            return
        print(f'{self.nome} Está comendo {alimento}')
        self.comendo = True

        sleep(2)

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo')
            sleep(5)
            return
        print(f'{self.nome} parou de comer')
        self.comendo = False
        sleep(5)

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade
