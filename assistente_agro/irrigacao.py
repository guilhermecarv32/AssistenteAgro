from time import sleep

def iniciar_irrigadores():
    return None

def atuar_sobre_irrigadores(acao, objeto, _):
    if acao in [ "ligar", "ativar" ] and objeto in [ "irrigadores", "irrigador", "irrigação" ]:
        print("Ativando Irrigadores")
        
        sleep(5)
    elif acao in [ "desligar", "desativar" ] and objeto in [ "irrigadores", "irrigador", "irrigação" ]:
        print("Desativando Irrigadores")
        
        sleep(5)
        
        print("Atuação sobre irrigadores finalizada!")