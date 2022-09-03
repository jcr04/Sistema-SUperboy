import os
import time
import glob
from androidhelper import sl4a
import androidhelper as android
from classificador import Classificador

droid = android.Android()


class Apps(object):
    
    listaapps = []
    pacotes = ""

    os.chdir(os.path.dirname(os.path.abspath(__file__)))  
    os.chdir("..")
    os.chdir("..")  
    os.chdir(os.getcwd() + "/Android/data")  
    pacotes = sorted(os.listdir())

    def __init__(self):
        pass

    def listarapps(self):  
        apps = droid.getLaunchableApplications()  

        
        listaapps = []

        for i in apps[1]:  
            cl = Classificador()
            nomeapp = cl.normalizar(
                i)  
            atividade = apps[1][i]

            listaapps.append([nomeapp, atividade])

        self.listaapps = sorted(listaapps)  

        lapps = self.listaapps
        lpacotes = self.pacotes

        for j in lapps:  
            for i in lpacotes:
                if (i in j[1]):
                    self.listaapps[self.listaapps.index(j)].append(
                        i)  
                    lpacotes.pop(lpacotes.index(
                        i))  

        self.listaapps = lapps  

        # A lista a seguir é o conjunto de pacotes que não puderam ser identificados pelo código e vão ter que ser adicionados manualmente 
        listan = [["com.google.android.apps.youtube.creator", "yt studio"],
                      ["com.socialnmobile.dictapps.notepad.color.note", "colornote"],
                      ["com.cyberlink.powerdirector.DRA140225_01", "powerdirector"],
                      ["com.estrongs.android.pop.pro", "es file explorer pro"],
                      ["com.iudesk.android.photo.editor", "editor de fotos"],
                      ["com.zeptolab.thieves.google", "king of thieves"],
                      ["com.touchtype.swiftkey", "teclado swiftKey"],
                      ["com.google.android.videos", "play filmes"],
                      ["com.google.android.music", "play música"],
                      ["com.google.android.youtube", "youtube"],
                      ["com.google.android.apps.maps", "maps"],
                      ["pl.solidexplorer2", "solid explorer"]]

        for i in listan:  
            for j in self.listaapps:
                if i[1] == j[0]:  
                    self.listaapps[self.listaapps.index(j)].append(i[0])

        return

    def abrirapp(self, appsele):
        saida = "Nenhum aplicativo correspondente foi encontrado"

        apps = self.listaapps

        for i in apps:  
            if (appsele in i[0]) or (i[
                                         0] in appsele):  

                if (len(i) == 2):  
                    droid.launch(i[1])
                else:  
                    droid.startActivity('android.intent.action.MAIN', None, None, None, False, i[2], i[1])

                saida = ("Abrindo " + i[0])
                break

        return saida


class Arquivo(object):

    def __init__(self):
        pass

    def criar(self, nomearquivo, texto="Junior\nAIA\n0\n"):
        os.chdir(os.path.dirname(os.path.abspath(__file__)))  
        caminho = os.getcwd()
        arq = open(caminho + nomearquivo, "w+")
        arq.writelines(texto)  
        arq.close()

    def lertudo(self, complemento="/infos.txt"):  

        os.chdir(os.path.dirname(os.path.abspath(__file__)))  
        caminho = os.getcwd() + complemento  

        try:
            arq = open(caminho, 'r')
        except:
            
            return ["Arquivo não existe", False]

        info = arq.readlines()
        arq.close()

        return info  

    def gravar(self, caminho, texto):  

        os.chdir(os.path.dirname(os.path.abspath(__file__)))  
        cc = os.getcwd() + caminho  

        arq = open(cc, 'r+')
        arq.readlines()  
        arq.write(texto + "\n")  

        arq.close()  


class Cronos(object):

    def __init__(self):
        pass

    def tempo(self):
        t = time.localtime()
        hora = t[3]

        periodo = "Boa noite"
        if (hora > 0 and hora <= 4): periodo = "Boa noite"
        if (hora > 4 and hora < 12): periodo = "Bom dia"
        if (hora >= 12 and hora < 18): periodo = "Boa tarde"

       
        meses = ["Só pra usar o índice 0", "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Julho",
                 "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

        tempo = [periodo, t[3], t[4], t[2], meses[t[1]], t[0]]  
        return tempo


class Log(object):
    listaLogs = []  

    def __init__(self):
        pass

    def reg(self, entrada, saida):  
        cr = Cronos()
        agora = cr.tempo()

        log = [entrada, saida, agora]

        self.listaLogs.append(log)

        return True

    def listar(self):
        return self.listaLogs 


class Musicas(object):
    
    listamusicas = []  
    nomemusicas = []  

    def __init__(self):
        self.locext()
        self.locint()

    def listar(self, diretorio_usuario, diretorio):  
        if os.path.isdir(diretorio_usuario + diretorio):
            os.chdir(diretorio_usuario + diretorio)
            for arquivo in glob.glob("*.mp3"):
                if os.path.isdir(diretorio_usuario + diretorio + arquivo):
                    self.listar(diretorio_usuario, diretorio + arquivo + '/')


                else:
                    
                    caminho = str(diretorio_usuario + diretorio + arquivo)
                    self.listamusicas.append(caminho)
                    self.nomemusicas.append(arquivo.lower())
        else:
            print('arquivo: ' + diretorio_usuario + diretorio)

    def tdp(self, caminho):  
        try:
            pastas = next(os.walk(caminho))[1]  
            return pastas
        except:
            return None

    def tda(self, caminho):  
        try:
            arquivos = next(os.walk(caminho))[2]  
            return arquivos
        except:
            return None

    def locint(self):  
        os.chdir(os.path.dirname(os.path.abspath(__file__)))  
        os.chdir(
            "..")  
        os.chdir("..")

        x = os.getcwd()
        diretorio_usuario = x + "/"

        musicsd = self.tda(os.getcwd())

        if musicsd != None:
            for i in musicsd:
                if ".mp3" in i:
                    musica = diretorio_usuario + i
                    self.listamusicas.append(musica)

        for i in self.tdp(x):
            diretorio = i + "/"
            self.listar(diretorio_usuario, diretorio)

    def locext(self):  
        os.chdir(os.path.dirname(os.path.abspath(__file__)))  

        for i in range(4):
            os.chdir(
                "..")  

        pasext = os.listdir()  
        raiz = os.getcwd()  

        for i in pasext:
            z = raiz + "/" + i + "/"
            os.chdir(z)  

            pastas = self.tdp(os.getcwd())  

            if pastas == None: break
            for j in pastas:
                j = j + "/"

                listar(z, j)

    def locmusica(self,
                  musica):  
        saida = "Nenhuma música correspondente encontrada", False

        for i in self.listamusicas:
            k = i.lower()  
            if (musica in k):
                return i, True
        return saida

    def tocarmusica(self, caminhomusica):

        droid.mediaPlay(caminhomusica)

        print("\nReproduzindo " + caminhomusica)
        print("\nAumente o brilho da tela no máximo para parar a reprodução")
        print("\nDiminua no mínimo para pausar/despausar")

        brilho = int(droid.getScreenBrightness()[1])  
        bmax = 255
        bmin = 10
        pausado = False

        if brilho == 255: bmax = 254  

        if brilho <= 10: bmin = brilho + 1

        brilho = 0  

        while (brilho != bmax):  
            brilho = int(droid.getScreenBrightness()[1])

            if (brilho <= bmin):  
                if (pausado == False):
                    droid.mediaPlayPause()
                    pausado = True
                    print("Música pausada")

                else:
                    droid.mediaPlayStart()
                    pausado = False
                    print("Reproduzindo música")

                while (droid.getScreenBrightness()[
                           1] <= bmin):  
                    pass

            from time import sleep
            sleep(5)

            if (droid.mediaIsPlaying()[1] == False and pausado == False): break  

        if (droid.mediaIsPlaying()[1] == True):  
            droid.mediaPlayClose()

        return "Música encerrada", True

        


class Voz(object):
    delay = 0.2  

    def __init__(self):
        pass

    def fale(self, texto):
        
        droid = sl4a.Android()
        droid.ttsSpeak(texto)
        
        while (droid.ttsIsSpeaking()[1]):  
            pass

        return

    def escute(self):
        droid = android.Android()
        (id, result, error) = droid.recognizeSpeech("Fale")

        return result 
