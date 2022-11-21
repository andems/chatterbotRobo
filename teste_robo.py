import unittest
from robo import *

class testeSaudacoes(unittest.TestCase):
    
    def setUp(self):
        self.robo = ChatBot("Robô de atendimento do açai",
                   read_only=True,
                   statement_comparison_function= comparar_mensagens,
                   response_selection_method= selecionar_resposta,
                   logic_adapters=[
                       {
                           "import_path": "chatterbot.logic.BestMatch"
                       }
                ])
        
    def test_oi(self):
        print("testando a saudaçao 'oi', 'ola'")
        
        SAUDACAO = ["oi", "ola"]
        
        for saudacao in SAUDACAO:
            print(f"testando {saudacao}")
                    
            resposta = self.robo.get_response(saudacao)
        
        self.assertIn("ola, sou o robo de atendimento do acai, como posso ajudar?", resposta.text)
        
    def test_bomdia(self):
        
        print("testando a saudaçao 'bom dia'")
        
        resposta = self.robo.get_response("bom dia")
        
        self.assertIn("bom dia, sou o robo de atendimento do acai, como posso ajudar?", resposta.text)
        
        
    def test_tarde(self):
            
        print("testando a saudaçao 'boa tarde'")
        
        resposta = self.robo.get_response("boa tarde")
        
        self.assertIn("boa tarde, sou o robo de atendimento do acai, como posso ajudar?", resposta.text)
            
        
        
    def test_noite(self):
        
        print("testando a saudaçao 'boa noite'")
        
        resposta = self.robo.get_response("boa noite")
        
        self.assertIn("boa noite, sou o robo de atendimento do acai, como posso ajudar?", resposta.text)
        
        
class test_acai(unittest.TestCase):
    
    def setUp(self):
        self.robo = ChatBot("Robô de atendimento do açai",
                   read_only=True,
                   statement_comparison_function= comparar_mensagens,
                   response_selection_method= selecionar_resposta,
                   logic_adapters=[
                       {
                           "import_path": "chatterbot.logic.BestMatch"
                       }
                ])
        
    
    def test_sorvete(self):
        
        print("testando sorvetes")
        
        resposta = self.robo.get_response("Quais os sabores de sorvetes ?")
        
        self.assertIn("Morango, Chocolate, Coco, Maracuja e Creme", resposta.text)
        
    def test_valores(self):
        
        print("testando valores")
        
        resposta = self.robo.get_response("Quais os valores ?")
        
        self.assertIn("Todos sao pesados, temos precos aparte de 8,00 reais", resposta.text)
        
    def test_funcionamento(self):
        
        print("testando funcionamento")
        
        resposta = self.robo.get_response("Qual o horario de funcionamento ?")
        
        self.assertIn("Funcionamos de terca aos domingos de 13:30 as 20:00", resposta.text)
        
    def test_pagamento(self):
        
        print("testando pagamento")
        
        resposta = self.robo.get_response("Quais as formas de pagamentos ?")
        
        self.assertIn("Aceitamos cartao de credito e debito, dinheiro e pix", resposta.text)
        
    def test_complementos(self):
        
        print("testando complementos")
        
        resposta = self.robo.get_response("Quais os complementos ?")
        
        self.assertIn("Temos frutas (uva, morango e banana), gotas de chocolate, granola, leite em po, leite condesado, bis e MMs", resposta.text)
        
    def test_localizacao(self):
        
        print("testando localizaçao")
        
        resposta = self.robo.get_response("Qual a localização ?")
        
        self.assertIn("Ficamos localizado na avenida progresso, numero 70", resposta.text)
        
    def test_quantidade(self):
        
        print("testando quantidade complementos")
        
        resposta = self.robo.get_response("Até quantos complementos ?")
        
        self.assertIn("pode ser escolhido ate cinco(5) complementos", resposta.text)
        
    def test_pdd(self):
        print("testando a")
        
        SAUDACAO = ["Quais as massas?", "quero um acai", "quero fazer um pedido"]
        
        for saudacao in SAUDACAO:
            print(f"testando {saudacao}")
                    
            resposta = self.robo.get_response(saudacao)
        
        self.assertIn("Trabalhamos com as massas de acai, cupuacu, acai com creme, acai com morango e sorvetes", resposta.text)
        
    
    
if __name__ == "__main__":
    carregador = unittest.TestLoader()
    test = unittest.TestSuite()
    
    test.addTest(carregador.loadTestsFromTestCase(testeSaudacoes))
    test.addTest(carregador.loadTestsFromTestCase(test_acai))
    
    
    executor = unittest.TextTestRunner()
    executor.run(test)