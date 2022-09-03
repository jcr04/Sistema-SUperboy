import random
import util


class Classificador(object):
    def __init__(self):
        pass
    
    def fatiar(self,frase): 
        palavras=frase.split(" ")
        return palavras


    def normalizar(self,frase): 
        frase=frase.lower()
        return frase

    def aprende(self,listadetreino): #
        listadetreino
             
                
    def analisarresp(self,entrada):
        

        resp_afir=["yes", "sim", "claro","claro que sim", "com certeza", "afirmativo", "pode crer", "agora","óbvio que sim","por favor","correto", "certo", "isso mesmo", "pode pá"]
        resp_nega=["not","não","claro que não", "nem pensar", "com certeza não","nunca", "negativo","nunca","jamais","errado","incorreto"]

        resp_duv=["não sei","talvez","pode ser","talvez sim","talvez não","incerto"] 

        resp_duva=["pode ser","talvez sim","provavelmente","é provável"]
        resp_duvn=["acho que não","talvez não","provavelmente não","é provável que não","melhor não"] 

 
        ra=0 #%
        rn=0 #%
        rdv=0 #%
        rdva=0 #%
        rdvn=0 #%
        
        for resp in resp_afir:
            if (entrada==resp): 
                ra=100
                break
            if (entrada in resp or resp in entrada): 
                ra+=1 
                
        for resp in resp_nega:
            if (entrada==resp):
                rn=100
                break
            if (entrada in resp or resp in entrada):
                rn+=1 
                
        for resp in resp_duv:
            if (entrada==resp): 
                rdv=100
                break
            if (entrada in resp or resp in entrada): 
                rdv+=1
                
        for resp in resp_duva:
            if (entrada==resp):
                rn=100
                break
            if (entrada in resp or resp in entrada): 
                rdva+=1 

        for resp in resp_duvn:
            if entrada==resp: 
                rdva=100
                break
            if (entrada in resp or resp in entrada):
                rdvn+=1 

        total=ra+rn+rdv+rdva+rdvn 

        if ra != 0: ra=ra*100/total
        if rn != 0: rn=rn*100/total
        if rdv != 0: rdv=rdv*100/total
        if rdva != 0: rdva=rdva*100/total
        if rdvn != 0: rdvn=rdvn*100/total

        prob={"Afirmativa:":ra,"Negativa:":rn,"Talvez:":rdv,"Talvez sim:":rdva,"Talvez não:":rdvn}
        
        for i in sorted(prob, key = prob.get,reverse=True):
            print (i,prob[i])
        return
    
    nome_cat=[] 
    categorias=[]



    def treinar(self,listadetreino): 

        

        nome_cat=[]
        categorias=[]

        j=0
        for i in range(len(listadetreino)): 
            if ((listadetreino[j][0] in nome_cat) == False):
                categorias.append([])
                nome_cat.append(listadetreino[j][0])
            j+=1

        j=0 
        for i in range(len(listadetreino)): 
            for h in nome_cat:
                if (listadetreino[j][0]==h):
                    categorias[nome_cat.index(h)]=listadetreino[j][1]
            j+=1

        self.nome_cat=nome_cat 
        self.categorias=categorias

        return
        
        
    def testartreino(self,entrada,literal=True):

        k=0
        resultado=[]
        corre100=False 

        for i in self.nome_cat: 
            for resp in self.categorias[self.nome_cat.index(i)]:
                if (entrada==resp): 
                    for a in range(100): 
                        resultado.append(i) 
                    corre100=True
                    break   

                if (literal==False): 
                    if (entrada in resp or resp in entrada):
                        resultado.append(i)
                else: 
                    if(entrada in resp): 
                        resultado.append(i) 



            if(corre100==True):
                
                break 
                 

        total=0
        pontoscatego=[] 
        for i in self.nome_cat:
            pontoscatego.append([i,resultado.count(i)])
            total+=resultado.count(i)


        for i in pontoscatego: 
            if (i[1] != 0):
                pontoscatego[pontoscatego.index(i)][1]=i[1]*100/total

        
        pontoscatego.sort(key=lambda x: x[1], reverse=True) 

        saida=pontoscatego[0]

        if (saida[1]==0):
            saida= False
        return saida

    def conta(self,entrada): 
        conta=False 
        operacao=[["+","mais"],["-","menos"],["*","x","vezes","multiplicado por"],["/","dividido por"]]

        
        for sinal in operacao:
            for i in sinal:
                if i in entrada:
                    posiope=entrada.index(i) 
                    tamposiope=len(i)
                    

                    k=2 
                    while (posiope-k>=0): 
                        
                        
                       
                        try:
                            x=int(entrada[posiope-k]) 
                             
                        except:
                            try:
                                num1=int(entrada[(posiope-k):posiope-1])
                                
                                break 

                            except: 
                                return False
                        
                        if(posiope-k==0):
                            num1=int(entrada[(posiope-k):posiope-1])
                            
                            break 

                       
                        k+=1

                   
                    k=tamposiope+2 


                    while (True and k<=len(entrada)): 
                        try:
                            x=int(entrada[posiope+k]) 

                        except:
                            num2=int(entrada[posiope+tamposiope+1:(posiope+k)])
                            break
                            
                        k+=1
                    
                    
                    resultado=0

                    while (True):
                        if (i=="+") or (i=="mais"):
                            resultado=(str(num1)+" mais "+str(num2)+" é igual a "+str(num1+num2))                         
                            break
                        
                        if (i=="-") or (i=="menos"):
                            resultado=(str(num1)+" menos "+str(num2)+" é igual a "+str(num1-num2))      
                            break
                        
                        if (i=="x") or (i=="vezes") or (i=="multiplicado por"):
                            resultado=(str(num1)+" vezes "+str(num2)+" é igual a "+str(num1*num2))
                            break
                        
                        if (i=="/" or "dividido por"):
                            resultado=(str(num1)+" dividido por "+str(num2)+" é igual a "+str(num1/num2))
                            break

                     
                    return resultado
        
        
        
        return False

    def idacao(self,entrada):  

        if(self.conta(entrada)!=False): 
            saida=self.conta(entrada)    
            return 1, saida             
            

            
        else:
            hora=["2 Saber horas",["que horas são", "que hora é agora", "horas por favor","me diga as horas"]]
            
            data=["3 Saber data",["que dia é hoje", "qual a data de hoje","data de hoje"]]
        
            fecharIa=["4 Fechar App do BOT",["sair", "encerrar", "fechar programa", "cessar funções motoras"]]  
  
            abrirapp=["5 Abrir um aplicativo",["abrir aplicativo","abrir app","iniciar app","iniciar aplicativo","abrir"]]

            tocarmusica=["6 Reproduzir música",["tocar música", "toque a música", "reproduzir música", "toque uma música", "tocar", "toque", "reproduzir" ]] 
            

            listadetreino1=[fecharIa]
            listadetreino2=[hora,data,fecharIa,abrirapp,tocarmusica]
            

            self.treinar(listadetreino1) 
            saida=self.testartreino(entrada)

            
            if (saida==False):
                

                self.treinar(listadetreino2) 
                saida=self.testartreino(entrada,False)

                if (saida==False):
                    
                    saida=0,"Nenhuma ação"
               
                else: 
                    saida=(int(self.testartreino(entrada,False)[0][0]), True) 
               
        return saida

    def execacao(self,entrada,na): 
        saida=0,False 
        
        if (na[0]==1): 
            saida=str(na[1])
            return saida
            
        if(na[0]==2): 
            cr=util.Cronos()
            saida=str("São "+str(cr.tempo()[1])+" e "+str(cr.tempo()[2]))         
            return saida
            
        if(na[0]==3): 
            cr=util.Cronos()
            t=cr.tempo()
            saida=str("Hoje é dia "+str(t[3]) +" de "+str(t[4]) +" de "+str(t[5])) 
            return saida

        if(na[0]==4): 
            v=util.Voz()
            v.fale("Programa encerrado")
            print("Programa encerrado")
            exit()
            
        if(na[0]==5): 
            
            a=util.Apps()
            a.listarapps()
            listaapp=a.listaapps
                
            for i in listaapp:
                #print(i[0])
                if(i[0] in entrada): 
                    saida=a.abrirapp(i[0])
                    return saida

            for i in listaapp: 
                j=self.fatiar(i[0])                   
                for k in j:
                    if(k in entrada):
                        saida=a.abrirapp(k)
        
        if(na[0]==6): 
            chaves=["tocar música", "toque a música", "reproduzir música", "toque uma música", "tocar", "toque", "reproduzir" ]
            
            ms=util.Musicas()
            musicas=ms.nomemusicas

            for chave in chaves:
                if chave in entrada:
                    if (chave=="toque uma música"): 
                        musica=random.choice(musicas)
                        
                    else: 
                        musica=entrada[entrada.index(chave)+len(chave)+1:len(entrada)]

                    musica=ms.locmusica(musica)
                    if(musica[1] != False): 
                        saida=ms.tocarmusica(musica[0])[0]
                        return saida
                    else:
                        saida=musica[0]                        
                        return saida                                        
        return saida


resp_afir=["Respostas Afirmativas",["yes", "sim", "claro","claro que sim", "com certeza", "afirmativo", "pode crer", "agora","óbvio que sim","por favor","correto", "certo", "isso mesmo", "pode pá","obviamente"]]
resp_nega=["Respostas Negativas",["not","não","claro que não", "nem pensar", "com certeza não","nunca", "negativo","nunca","jamais","errado","incorreto"]]
resp_duv=["Em dúvida",["não sei","talvez","pode ser","talvez sim","talvez não","incerto"]] 
resp_duva=["Provavelmente sim",["pode ser","talvez sim","provavelmente","é provável"]] # Com maior probabilidade de sim
resp_duvn=["Provavelmente não",["acho que não","talvez não","provavelmente não","é provável que não","melhor não"]] # Com maior probabilidade de não

listadetreino=[resp_afir,resp_nega,resp_duv,resp_duva,resp_duvn]


