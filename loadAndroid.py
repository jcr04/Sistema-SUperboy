import os
import time
from util import Cronos
from util import Arquivo
from androidhelper import sl4a
import androidhelper as android


class Load:
    nomeUsu, nomeIa, primeiroUso = "", "", ""  

    def __init__(self):
        pass

    def carregarInformacoesIniciais(self):
        arquivo = Arquivo()

        if not arquivo.lertudo()[1]:
            arquivo.criar("/infos.txt")

        info = arquivo.lertudo()
        return info

    def iniciar(self, info):
        self.nomeUsu = info[0]  
        self.nomeIa = info[1]
        self.primeiroUso = str(info[2])  

        self.nomeUsu = self.nomeUsu[:-1]  
        self.nomeIa = self.nomeIa[:-1]

        if "0" in self.primeiroUso:
            droid = sl4a.Android()
            self.nomeUsu, self.nomeIa = None, None

            while self.nomeUsu is None:
                self.nomeUsu = droid.dialogGetInput("Como devo lhe chamar? ", "Insira seu nome").result

            while self.nomeIa is None:
                self.nomeIa = droid.dialogGetInput("Nome da IA", "Insira um nome").result

            os.chdir(os.path.dirname(os.path.abspath(__file__)))  
            caminho = os.getcwd() + "/infos.txt"  

            arq = open(caminho, 'w')
            arq.writelines(self.nomeUsu + "\n" + self.nomeIa + "\n" + "1 \n")
            arq.close()

        cronos = Cronos()
        saudacao_gerada = str(cronos.tempo()[0] + " " + self.nomeUsu)  
        time.sleep(1)  

        return saudacao_gerada
