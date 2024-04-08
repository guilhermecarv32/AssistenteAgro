from time import sleep

def iniciar_controle_pragas():
    return None

def atuar_sobre_controle(acao, objeto, _):
    if acao == "verificar" and objeto in [ "pragas", "doenças" ]:
        print("Nenhuma praga ou doença detectada nas plantações.")
        
        sleep(5)
        
        print("Atuação sobre controle de pragas finalizada!")