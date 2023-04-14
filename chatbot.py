from util import Voz
from util import Arquivo
from paciencia import Paciencia
from classificador import Classificador
from buscaWeb import BuscaWeb

class Chatbot:
    def __init__(self):
        self.data = {}

    def train(self, inputs, outputs):
        for i in inputs:
            self.data[i] = outputs[inputs.index(i)]
        self.save()

    def save(self):
        with open("data.txt", "w") as f:
            for i in self.data:
                f.write(i + ":" + self.data[i] + "\n")

    def load(self):
        with open("data.txt", "r") as f:
            for line in f:
                parts = line.strip().split(":")
                self.data[parts[0]] = parts[1]

    def normalize(self, text):
        return text.lower()

    def respond(self, text):
        text = self.normalize(text)
        if text in self.data:
            return self.data[text], True
        else:
            response = "Desculpe, não entendi o que você disse."
            return response, False

    def learn(self, text):
        response = ""
        while response == "":
            response = input("Qual é a resposta para " + text + "? ")
        self.data[self.normalize(text)] = response
        self.save()
        return "Obrigado por me ensinar!"

    def run(self):
        self.load()
        print("Olá, sou o Chatbot. O que você quer saber?")

        while True:
            text = input("> ")
            if text.lower() in ["sair", "pare"]:
                print("Até mais!")
                break
            elif text.lower() in ["ajuda", "help"]:
                print("Digite uma pergunta ou frase, e eu tentarei responder da melhor forma possível.")
            elif text.lower() in ["aprender", "ensinar"]:
                text = input("Qual é a pergunta que você quer ensinar? ")
                print(self.learn(text))
            else:
                response, success = self.respond(text)
                print(response)       
        
        arq=Arquivo()

        if((arq.lertudo("/BD/txt/i.txt")[1]==False) or (arq.lertudo("/BD/txt/o.txt")[1]==False)):               
            arq.criar("/BD/txt/i.txt") 
            arq.criar("/BD/txt/o.txt")

        inputs=arq.lertudo("/BD/txt/i.txt") 
        outputs=arq.lertudo("/BD/txt/o.txt") 
        
        
        n=0 
        for i in inputs: 
            
            if(entrada+"\n"==i): 
                resposta=outputs[n]              
                return resposta,True
            n+=1


        
        cb = BuscaWeb()
        resultado = cb.start(entrada)
        if(resultado[1]):
            return resultado 
            
		
		
        
        return resposta,False 

    
    def aprender1(self, entrada): 
        v=Voz() 
        cl=Classificador()
        
        v.fale("Quer Cadastrar uma agora?")
        saida=(v.escute())     
        saida=cl.normalizar(saida) 
                
        sim=["sim", "claro", "com certeza", "óbvio que sim","por favor", "correto", "certo", "isso mesmo"] 
        
        for i in sim:
            if(saida in i):
                while(True): 
                    v.fale("Qual a resposta?")
                    saida=(v.escute())
                    
                
                    v.fale("Então a sua entrada é:, "+entrada)
                    v.fale("E a saída é:, "+saida)
                    v.fale("Correto?") 
                    resp=(v.escute())
                
                    for i in sim:
                        if(resp in i):
                            v.fale("Ok, gravando resposta") 
                       
                            entrada=cl.normalizar(entrada) 
                            saida=cl.normalizar(saida)
                           
                            arq=Arquivo() 
                            arq.gravar("/BD/txt/i.txt",entrada)
                            arq.gravar("/BD/txt/o.txt",saida)
                               
                            return
                
                     
                    v.fale("Você pode repitir por favor?")
                    v.fale("Qual é a pergunta?") 
                    entrada=(v.escute())
        
        
        v.fale("Ok, fica para próxima") 
        return 

    
    def aprenderTxt1(self, entrada): 
        v=Voz() 
        cl=Classificador()
        
        saida = input("Quer Cadastrar uma agora?: ")         
        saida=cl.normalizar(saida) 
                
        sim=["sim", "claro", "com certeza", "óbvio que sim","por favor", "correto", "certo", "isso mesmo"] 
        
        for i in sim:
            if(saida in i):
                while(True): 
                    saida=input("Qual a resposta?: ")
                    
                    saida=cl.normalizar(saida) 
                    
                
                    print("Então a sua entrada é: "+entrada)
                    print("E a saída é: "+saida)
                     
                    resp=input("Correto?: ") 
                
                    for i in sim:
                        if(resp in i):
                            print("Ok, gravando resposta") 
                       
                            entrada=cl.normalizar(entrada) 
                            saida=cl.normalizar(saida)
                           
                            arq=Arquivo() 
                            arq.gravar("/BD/txt/i.txt",entrada)
                            arq.gravar("/BD/txt/o.txt",saida)
                               
                            return
                
                     
                    print("Você pode repitir por favor?")
                    entrada=input("Qual é a pergunta?") 
                    
        
        
        print("Ok, fica para próxima") 
        return 
