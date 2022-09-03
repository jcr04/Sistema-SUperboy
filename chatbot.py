from util import Voz
from util import Arquivo
from paciencia import Paciencia
from classificador import Classificador
from buscaWeb import BuscaWeb

class Chatbot():
    entradasrecentes=[]

    def __init__(self):
        pass

    def interagir(self, entrada, log=[] ): 
       
        cl=Classificador()
        entrada=cl.normalizar(entrada) 

        resposta = "Infelizmente não tenho nenhuma resposta para isso" 

	   
        if("pare" == entrada or "sair" in entrada): exit() 

         
        paciencia=Paciencia() 
        resp=paciencia.ent_rep(self.entradasrecentes,entrada)
        if(resp[1]==True):  
            self.entradasrecentes=[]
            return resp 
        self.entradasrecentes.append(entrada) 


        
        repita=["repita", "repete", "o que você disse", "repete por favor"]
        
        for r in repita:
            if(r==entrada and len(log)!=0): 
                
                return log[len(log)-1][1],True
            
        
        numop=cl.idacao(entrada)
        if(numop[0]!=0):    
            resp=cl.execacao(entrada,numop)
            if(resp[0]!=0):
                return resp,True
                     
        
        
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
