from time import sleep
import random

def iniciar_consulta():
    return None

def atuar_sobre_consultor(acao, objeto, _):
    if acao == "consultar" and objeto in [ "clima", "tempo" ]:
        
        numero = random.randint(0, 9)
        
        if numero <= 2:
            print("O tempo está Ensolarado")
        elif 3 <= numero <= 5:
            print("O tempo está Chuvoso")
        elif 6 <= numero <= 8:
            print("O tempo está Nublado")
        else:
            print("O tempo está Nevando")
        
        sleep(5)
        
        print("Atuação sobre consulta climática finalizada!")