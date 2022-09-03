import urllib.request
from unicodedata import normalize

import urllib.parse
import urllib.request

class BuscaWeb(object):
    def __init__(self):
        pass

    def gerarUrl(self,chave): 
        textoBusca = chave.replace(" ","+") 
        
        url = str("https://www.google.com.br/search?q="+textoBusca)
        #print(url)
        return url
    
    def busca(self,url): 
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0','Accept-Charset':'utf-8'}  

        req = urllib.request.Request(url, headers = headers)   
        retorno = urllib.request.urlopen(req).read()
        retorno = str(retorno.decode('utf-8','ignore'))
        
        
        return retorno

    def remover_acentos(self,txt, codif='utf-8'):
        txt=txt.encode('utf-8') 
        semAce = str(normalize('NFKD', txt.decode(codif)).encode('ASCII', 'ignore'))   
        semAce=semAce[2:len(semAce)-1] 
        print(semAce) 
        return semAce

    def responder(self,html): 

        codTipos = ["""class="Z0LcW">""",
            """data-dobid="dfn"><span>""",
            """class="vk_gy vk_sh">""",
                      
            """class="ILfuVd yZ8quc c3biWd">""", #importante
            """class="ILfuVd yZ8quc">""",

            """id="knowledge-currency__tgt-amount">""",
            """class="cwcot" id="cwos">""",
            """id="tw-target-text" style="text-align:left"><span>"""]
        
        tipos = ["quem é ou data de",
            "significado",
            "que dia é",

            "descobrimento 2",
            "descobriento 1",
                
            
            "calcular",
            "tradução"]

        resposta = "nenhum resultado"
        tipoCorte = None
        for ct in codTipos:
            if(ct in html):
                if (tipos[codTipos.index(ct)] == "que dia é"):
                    if( """class="dDoNo vk_bk">""" in html):                        
                        ct2 = """class="dDoNo vk_bk">"""
                       
                        break
                ct2 = ct
                break
            
        try: 
            html = html[(html.index(ct2)+len(ct2)):len(html)] 
            html = html.replace("<b>","") 
            html = html.replace("</b>","") 

            resposta = html[0:html.index("<")]                  

        finally: 
            
            return resposta

    def start(self,busca):
        try:
            cb = BuscaWeb()
            url = cb.gerarUrl(cb.remover_acentos(busca))
            resultado = cb.responder(cb.busca(url))

            if (resultado == "nenhum resultado"):
                return resultado,False
            else:
                resultado = str(resultado)              
                return resultado, True
        except:
            resultado = "não foi possivel concluir a busca"
            return resultado, False
            
               






