from loadAndroid import Load
from chatbot import Chatbot
from util import Voz
from util import Log

voz = Voz()
log = Log()
load = Load()
chatbor = Chatbot()

infos = load.carregarInformacoesIniciais()

modo_texto_ativo = False
aprender = True


def iniciar():
    if not modo_texto_ativo:
        voz.fale(load.iniciar(infos)) 
    else:
        load.iniciar(infos)


def receber_entrada():
    if not modo_texto_ativo:
        entrada_recebida = (voz.escute())
    else:
        entrada_recebida = input(str("%s: " % load.nomeUsu))

    return entrada_recebida


def responder(entrada):
    saida = chatbor.interagir(entrada, log.listar())

    if not modo_texto_ativo:
        voz.fale(saida[0])
    print(load.nomeUsu, ": ", entrada)
    print(load.nomeIa, ": ", saida[0])

    log.reg(entrada, saida[0])  

    if not saida[1] and aprender:  
        if not modo_texto_ativo:
            chatbor.aprender1(entrada)
        else:
            chatbor.aprenderTxt1(entrada)


iniciar()

while True:
    responder(receber_entrada())
    
