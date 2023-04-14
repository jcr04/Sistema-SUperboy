from chatbot import ChatBot
from util import Voz, Log, Load

voz = Voz()
log = Log()
load = Load()
chatbot = ChatBot()

infos = load.carregarInformacoesIniciais()

modo_texto_ativo = False
aprender = True

def iniciar():
    if not modo_texto_ativo:
        # Corrigido erro de sintaxe na linha abaixo
        voz.fale(load.iniciar(infos) + " Verificando nome e primeiro acesso")
    else:
        load.iniciar(infos)

def receber_entrada():
    if not modo_texto_ativo:
        entrada_recebida = voz.escute()
    else:
        entrada_recebida = input(str("%s: " % load.nomeUsu))
    return entrada_recebida

def responder(entrada):
    saida = chatbot.interagir(entrada, log.listar())

    if not modo_texto_ativo:
        voz.fale(saida[0])
    print(load.nomeUsu, ": ", entrada)
    print(load.nomeIa, ": ", saida[0])

    log.reg(entrada, saida[0])

    # Corrigido problema de indentação na linha abaixo
    if not saida[1] and aprender:
        # Corrigido nome do método "aprender1" para "aprender" na linha abaixo
        if not modo_texto_ativo:
            chatbot.aprender(entrada)
        else:
            # Corrigido nome do método "aprenderTxt1
            iniciar()
            while True:
              entrada = receber_entrada()
# Checa se o usuário deseja sair do chatbot
              if entrada.lower() == "sair":
                  break
                  