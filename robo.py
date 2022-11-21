from chatterbot import ChatBot
from difflib import SequenceMatcher

ACEITACAO = 0.70

def comparar_mensagens(mensagem, mensagem_candidata):
    confiaca = 0.0
    
    if mensagem.text and mensagem_candidata.text:
        texto_mensagem = mensagem.text
        texto_mensagem_candidata = mensagem_candidata.text
        
        confiaca = SequenceMatcher(
            None,
            texto_mensagem,
            texto_mensagem_candidata
        )
        confiaca = round(confiaca.ratio(), 2)
        if confiaca < ACEITACAO:
            confiaca = 0.0
            
        else:
            print("mensagem do usuario :", texto_mensagem, ", mensagem candidata :", mensagem_candidata, ", nivel de confiaça :", confiaca)
            
            
    return confiaca


def selecionar_resposta(mensagem, lista_resposta, storage=None):
    resposta = lista_resposta[0]
    print("resposta escolhida", resposta)
    
    return resposta

def executar_robo():
    robo = ChatBot("Robô de atendimento do açai",
                   read_only=True,
                   statement_comparison_function= comparar_mensagens,
                   response_selection_method= selecionar_resposta,
                   logic_adapters=[
                       {
                           "import_path": "chatterbot.logic.BestMatch"
                       }
                   ]
                   )
    
    while True:
        entrada = input("digite alguma coisa...\n")
        resposta = robo.get_response(entrada)
        if resposta.confidence > 0.0:
            print(resposta.text)
            
        else:
            print("ainda nao sei responder")
            print("pergunte outra coisa...")
    
    
    
    
if __name__ == "__main__":
    executar_robo()
    
