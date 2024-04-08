import unittest
from assistente import *

CHAMANDO_OUTRO_NOME = "D:/Users/User/Desktop/Guilherme/java_progs_vscode/assistente_agro/audios/Gravação (Erro).wav"
LIGAR_IRRIGADOR = "D:/Users/User/Desktop/Guilherme/java_progs_vscode/assistente_agro/audios/Gravação (1).wav"
LIGAR_IRRIGADORES = "D:/Users/User/Desktop/Guilherme/java_progs_vscode/assistente_agro/audios/Gravação (2).wav"
LIGAR_IRRIGACAO = "D:/Users/User/Desktop/Guilherme/java_progs_vscode/assistente_agro/audios/Gravação (3).wav"
DESLIGAR_IRRIGADOR = "D:/Users/User/Desktop/Guilherme/java_progs_vscode/assistente_agro/audios/Gravação (4).wav"
DESLIGAR_IRRIGADORES = "D:/Users/User/Desktop/Guilherme/java_progs_vscode/assistente_agro/audios/Gravação (5).wav"
DESLIGAR_IRRIGACAO = "D:/Users/User/Desktop/Guilherme/java_progs_vscode/assistente_agro/audios/Gravação (6).wav"
ATIVAR_IRRIGADOR = "D:/Users/User/Desktop/Guilherme/java_progs_vscode/assistente_agro/audios/Gravação (7).wav"
ATIVAR_IRRIGADORES = "D:/Users/User/Desktop/Guilherme/java_progs_vscode/assistente_agro/audios/Gravação (8).wav"
ATIVAR_IRRIGACAO = "D:/Users/User/Desktop/Guilherme/java_progs_vscode/assistente_agro/audios/Gravação (9).wav"
DESATIVAR_IRRIGADOR = "D:/Users/User/Desktop/Guilherme/java_progs_vscode/assistente_agro/audios/Gravação (10).wav"
DESATIVAR_IRRIGADORES = "D:/Users/User/Desktop/Guilherme/java_progs_vscode/assistente_agro/audios/Gravação (11).wav"
DESATIVAR_IRRIGACAO = "D:/Users/User/Desktop/Guilherme/java_progs_vscode/assistente_agro/audios/Gravação (12).wav"
CONSULTAR_CLIMA = "D:/Users/User/Desktop/Guilherme/java_progs_vscode/assistente_agro/audios/Gravação (13).wav"
CONSULTAR_TEMPO = "D:/Users/User/Desktop/Guilherme/java_progs_vscode/assistente_agro/audios/Gravação (14).wav"
MEDIR_UMIDADE = "D:/Users/User/Desktop/Guilherme/java_progs_vscode/assistente_agro/audios/Gravação (15).wav"
VERIFICAR_PRAGAS = "D:/Users/User/Desktop/Guilherme/java_progs_vscode/assistente_agro/audios/Gravação (16).wav"
VERIFICAR_DOENCAS = "D:/Users/User/Desktop/Guilherme/java_progs_vscode/assistente_agro/audios/Gravação (17).wav"

class TesteNome(unittest.TestCase):
    def setUp(self):
        self.iniciado, self.reconhecedor, _, self.nome_do_assistente, _ = iniciar()
    
    def testar_01_reconhecer_nome(self):
        tem_transcricao, transcricao = processar_audio_de_teste(LIGAR_IRRIGADOR, self.reconhecedor)
        
        self.assertTrue(tem_transcricao)
        
        tokens = tokenizar_trancricao(transcricao)
        self.assertIsNotNone(tokens)
        self.assertEqual(tokens[0], self.nome_do_assistente)
        
    def testar_02_nao_reconhecer_outro_nome(self):
        tem_transcricao, transcricao = processar_audio_de_teste(CHAMANDO_OUTRO_NOME, self.reconhecedor)

        self.assertTrue(tem_transcricao)

        tokens = tokenizar_trancricao(transcricao)
        self.assertIsNotNone(tokens)
        self.assertNotEqual(tokens[0], self.nome_do_assistente)

class TesteIrrigador(unittest.TestCase):
    
    def setUp(self):
        self.iniciado, self.reconhecedor, self.palavras_de_parada, self.nome_do_assistente, self.acoes = iniciar()
        
    def testar_01_ligar_irrigador(self):
        tem_transcricao, transcricao = processar_audio_de_teste(LIGAR_IRRIGADOR, self.reconhecedor)

        self.assertTrue(tem_transcricao)

        tokens = tokenizar_trancricao(transcricao)
        self.assertIsNotNone(tokens)

        tokens = eliminar_palavras_de_parada(tokens, self.palavras_de_parada)
        valido, _, _ = validar_comando(tokens, self.nome_do_assistente, self.acoes)
        self.assertTrue(valido)
        
    def testar_02_ligar_irrigadores(self):
        tem_transcricao, transcricao = processar_audio_de_teste(LIGAR_IRRIGADORES, self.reconhecedor)

        self.assertTrue(tem_transcricao)

        tokens = tokenizar_trancricao(transcricao)
        self.assertIsNotNone(tokens)

        tokens = eliminar_palavras_de_parada(tokens, self.palavras_de_parada)
        valido, _, _ = validar_comando(tokens, self.nome_do_assistente, self.acoes)
        self.assertTrue(valido)
        
    def testar_03_ligar_irrigacao(self):
        tem_transcricao, transcricao = processar_audio_de_teste(LIGAR_IRRIGACAO, self.reconhecedor)

        self.assertTrue(tem_transcricao)

        tokens = tokenizar_trancricao(transcricao)
        self.assertIsNotNone(tokens)

        tokens = eliminar_palavras_de_parada(tokens, self.palavras_de_parada)
        valido, _, _ = validar_comando(tokens, self.nome_do_assistente, self.acoes)
        self.assertTrue(valido)
        
    def testar_04_desligar_irrigador(self):
        tem_transcricao, transcricao = processar_audio_de_teste(DESLIGAR_IRRIGADOR, self.reconhecedor)

        self.assertTrue(tem_transcricao)

        tokens = tokenizar_trancricao(transcricao)
        self.assertIsNotNone(tokens)

        tokens = eliminar_palavras_de_parada(tokens, self.palavras_de_parada)
        valido, _, _ = validar_comando(tokens, self.nome_do_assistente, self.acoes)
        self.assertTrue(valido)
        
    def testar_05_desligar_irrigadores(self):
        tem_transcricao, transcricao = processar_audio_de_teste(DESLIGAR_IRRIGADORES, self.reconhecedor)

        self.assertTrue(tem_transcricao)

        tokens = tokenizar_trancricao(transcricao)
        self.assertIsNotNone(tokens)

        tokens = eliminar_palavras_de_parada(tokens, self.palavras_de_parada)
        valido, _, _ = validar_comando(tokens, self.nome_do_assistente, self.acoes)
        self.assertTrue(valido)
        
    def testar_06_desligar_irrigacao(self):
        tem_transcricao, transcricao = processar_audio_de_teste(DESLIGAR_IRRIGACAO, self.reconhecedor)

        self.assertTrue(tem_transcricao)

        tokens = tokenizar_trancricao(transcricao)
        self.assertIsNotNone(tokens)

        tokens = eliminar_palavras_de_parada(tokens, self.palavras_de_parada)
        valido, _, _ = validar_comando(tokens, self.nome_do_assistente, self.acoes)
        self.assertTrue(valido)
        
    def testar_07_ativar_irrigador(self):
        tem_transcricao, transcricao = processar_audio_de_teste(ATIVAR_IRRIGADOR, self.reconhecedor)

        self.assertTrue(tem_transcricao)

        tokens = tokenizar_trancricao(transcricao)
        self.assertIsNotNone(tokens)

        tokens = eliminar_palavras_de_parada(tokens, self.palavras_de_parada)
        valido, _, _ = validar_comando(tokens, self.nome_do_assistente, self.acoes)
        self.assertTrue(valido)
        
    def testar_08_ativar_irrigadores(self):
        tem_transcricao, transcricao = processar_audio_de_teste(ATIVAR_IRRIGADORES, self.reconhecedor)

        self.assertTrue(tem_transcricao)

        tokens = tokenizar_trancricao(transcricao)
        self.assertIsNotNone(tokens)

        tokens = eliminar_palavras_de_parada(tokens, self.palavras_de_parada)
        valido, _, _ = validar_comando(tokens, self.nome_do_assistente, self.acoes)
        self.assertTrue(valido)
        
    def testar_09_ativar_irrigacao(self):
        tem_transcricao, transcricao = processar_audio_de_teste(ATIVAR_IRRIGACAO, self.reconhecedor)

        self.assertTrue(tem_transcricao)

        tokens = tokenizar_trancricao(transcricao)
        self.assertIsNotNone(tokens)

        tokens = eliminar_palavras_de_parada(tokens, self.palavras_de_parada)
        valido, _, _ = validar_comando(tokens, self.nome_do_assistente, self.acoes)
        self.assertTrue(valido)
        
    def testar_10_desativar_irrigador(self):
        tem_transcricao, transcricao = processar_audio_de_teste(DESATIVAR_IRRIGADOR, self.reconhecedor)

        self.assertTrue(tem_transcricao)

        tokens = tokenizar_trancricao(transcricao)
        self.assertIsNotNone(tokens)

        tokens = eliminar_palavras_de_parada(tokens, self.palavras_de_parada)
        valido, _, _ = validar_comando(tokens, self.nome_do_assistente, self.acoes)
        self.assertTrue(valido)   
        
    def testar_11_desativar_irrigadores(self):
        tem_transcricao, transcricao = processar_audio_de_teste(DESATIVAR_IRRIGADORES, self.reconhecedor)

        self.assertTrue(tem_transcricao)

        tokens = tokenizar_trancricao(transcricao)
        self.assertIsNotNone(tokens)

        tokens = eliminar_palavras_de_parada(tokens, self.palavras_de_parada)
        valido, _, _ = validar_comando(tokens, self.nome_do_assistente, self.acoes)
        self.assertTrue(valido)   
        
    def testar_12_desativar_irrigacao(self):
        tem_transcricao, transcricao = processar_audio_de_teste(DESATIVAR_IRRIGACAO, self.reconhecedor)

        self.assertTrue(tem_transcricao)

        tokens = tokenizar_trancricao(transcricao)
        self.assertIsNotNone(tokens)

        tokens = eliminar_palavras_de_parada(tokens, self.palavras_de_parada)
        valido, _, _ = validar_comando(tokens, self.nome_do_assistente, self.acoes)
        self.assertTrue(valido)   
        
class TesteClima(unittest.TestCase):   
    def setUp(self):
        self.iniciado, self.reconhecedor, self.palavras_de_parada, self.nome_do_assistente, self.acoes = iniciar()
    
    def testar_13_consultar_clima(self):
        tem_transcricao, transcricao = processar_audio_de_teste(CONSULTAR_CLIMA, self.reconhecedor)

        self.assertTrue(tem_transcricao)

        tokens = tokenizar_trancricao(transcricao)
        self.assertIsNotNone(tokens)

        tokens = eliminar_palavras_de_parada(tokens, self.palavras_de_parada)
        valido, _, _ = validar_comando(tokens, self.nome_do_assistente, self.acoes)
        self.assertTrue(valido)  
        
    def testar_14_consultar_tempo(self):
        tem_transcricao, transcricao = processar_audio_de_teste(CONSULTAR_TEMPO, self.reconhecedor)

        self.assertTrue(tem_transcricao)

        tokens = tokenizar_trancricao(transcricao)
        self.assertIsNotNone(tokens)

        tokens = eliminar_palavras_de_parada(tokens, self.palavras_de_parada)
        valido, _, _ = validar_comando(tokens, self.nome_do_assistente, self.acoes)
        self.assertTrue(valido) 
        
class TesteUmidade(unittest.TestCase):       
    def setUp(self):
        self.iniciado, self.reconhecedor, self.palavras_de_parada, self.nome_do_assistente, self.acoes = iniciar()
    
    def testar_15_medir_umidade(self):
        tem_transcricao, transcricao = processar_audio_de_teste(MEDIR_UMIDADE, self.reconhecedor)

        self.assertTrue(tem_transcricao)

        tokens = tokenizar_trancricao(transcricao)
        self.assertIsNotNone(tokens)

        tokens = eliminar_palavras_de_parada(tokens, self.palavras_de_parada)
        valido, _, _ = validar_comando(tokens, self.nome_do_assistente, self.acoes)
        self.assertTrue(valido) 
        
class TestePragas(unittest.TestCase):     
    def setUp(self):
        self.iniciado, self.reconhecedor, self.palavras_de_parada, self.nome_do_assistente, self.acoes = iniciar()

    def testar_16_verificar_pragas(self):
        tem_transcricao, transcricao = processar_audio_de_teste(VERIFICAR_PRAGAS, self.reconhecedor)

        self.assertTrue(tem_transcricao)

        tokens = tokenizar_trancricao(transcricao)
        self.assertIsNotNone(tokens)

        tokens = eliminar_palavras_de_parada(tokens, self.palavras_de_parada)
        valido, _, _ = validar_comando(tokens, self.nome_do_assistente, self.acoes)
        self.assertTrue(valido) 
        
    def testar_16_verificar_doencas(self):
        tem_transcricao, transcricao = processar_audio_de_teste(VERIFICAR_DOENCAS, self.reconhecedor)

        self.assertTrue(tem_transcricao)

        tokens = tokenizar_trancricao(transcricao)
        self.assertIsNotNone(tokens)

        tokens = eliminar_palavras_de_parada(tokens, self.palavras_de_parada)
        valido, _, _ = validar_comando(tokens, self.nome_do_assistente, self.acoes)
        self.assertTrue(valido) 


if __name__ == '__main__':
    carregador = unittest.TestLoader()
    testes = unittest.TestSuite()

    testes.addTest(carregador.loadTestsFromTestCase(TesteNome))
    testes.addTest(carregador.loadTestsFromTestCase(TesteIrrigador))
    testes.addTest(carregador.loadTestsFromTestCase(TesteClima))
    testes.addTest(carregador.loadTestsFromTestCase(TesteUmidade))
    testes.addTest(carregador.loadTestsFromTestCase(TestePragas))

    executor = unittest.TextTestRunner()
    executor.run(testes)