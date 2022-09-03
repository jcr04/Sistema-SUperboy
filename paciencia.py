import random as r

class Paciencia():
    paciencia="" 
    
    def __init__(self):
        self.paciencia=r.randrange(2,5) 
        
    def ent_rep(self,lista_entradas,entrada_atual):  
        if(lista_entradas.count(entrada_atual)>=self.paciencia) : 
            
            ordinal=["0","primeira", "segunda", "terceira", "quarta", "quinta"] 
            
            p = self.paciencia  
            
            saidas=["parece que alguém está com mau de Alzheimer",  
            	"sabe a definição de insanidade?, fazer a mesma coisa sempre esperando resultados diferentes", 
            	"então você acha que se repetir muda algo?",  
            	"não se cansa de repetir a mesma coisa? ",  
            ]
                       
            saida=r.choice(saidas) 
            return saida, True
        
        return "Paciência ok", False
"""
i = Paciencia()
print("Level:", i.paciencia)
print(i.ent_rep(["5", "5", "5","5"],"5"))
"""
