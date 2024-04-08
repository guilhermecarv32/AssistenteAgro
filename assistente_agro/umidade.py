from time import sleep
import random

def iniciar_umidade():
    return None

def atuar_sobre_umidade(acao, objeto, _):
    if acao == "medir" and objeto == "umidade":
        umidade = random.randint(30, 80)
        print(f"A umidade do solo nas plantações atualmente é de {umidade:.2f}%")
        
        sleep(5)
        
        print("Atuação sobre medidor de umidade finalizada!")