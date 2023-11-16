from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

print("It's running")
# Abrindo o navegador e redirecionando pro whatsapp web
navegador = webdriver.Chrome()
navegador.maximize_window()
navegador.get("https://web.whatsapp.com/")
usuariosAtendidos = []
atendimentoHumano = []
while len(navegador.find_elements(By.ID, "side")) < 1:
    time.sleep(1)
filtro = WebDriverWait(navegador, 5).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="side"]/div[1]/div/button/div/span')))
filtro.click()
time.sleep(5)
while True:
    # Tentando encontrar uma conversa não lida e entrar nela  
  
    try:

        todasConversasNaoLidas = WebDriverWait(navegador, 5).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'ggj6brxn.gfz4du6o.r7fjleex.g0rxnol2.lhj4utae.le5p0ye3.l7jjieqr._11JPr')))
        conversasNaoLidas = [conversa for conversa in todasConversasNaoLidas]
        conversa = conversasNaoLidas[0]
        print(conversa.text)

        for conversa in conversasNaoLidas if conversasNaoLidas != "" else time.sleep(1):
            mensagemPreview = WebDriverWait(navegador, 5).until(EC.presence_of_element_located((By.CLASS_NAME,"p357zi0d.r15c9g6i")))
            if mensagemPreview.text.lower() == "voltar" and conversa.text in atendimentoHumano:
                atendimentoHumano.remove(conversa.text)
            elif conversa.text in atendimentoHumano:
                conversasNaoLidas.remove(conversa)
                conversasNaoLidas.remove(conversasNaoLidas[0])
                continue
            else:
                conversa.click()
                # Obtenha o nome do cliente
                nomeCliente = WebDriverWait(navegador, 5).until(EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="main"]/header/div[2]/div/div/div/span')))
                nome = nomeCliente.text
                
                # Obtenha o conteúdo da última mensagem do cliente
                todasMensagens = WebDriverWait(navegador, 5).until(
                    EC.presence_of_all_elements_located((By.CLASS_NAME, "_21Ahp")))
                textosMensagens = [mensagem.text for mensagem in todasMensagens]
                textoUltimaMensagem = textosMensagens[-1]
                print(textoUltimaMensagem)

                # Responda a mensagem do cliente
                mensagem = ""
                if nome not in usuariosAtendidos:

                    mensagem = """Olá, eu sou Samy. Um robô assistente em fase de testes.\nDigite o número relacionado com o que eu posso fazer por você:\n\n1- Tabela de preços\n2 - Marcar horário\n3 - Falar com um atendente humano"""
                    usuariosAtendidos.append(nome)     

                elif textoUltimaMensagem == "1" or textoUltimaMensagem.lower() == "tabela de preços" or textoUltimaMensagem.lower() == "tabela" or textoUltimaMensagem.lower() == "preços" or textoUltimaMensagem.lower() == "one" or textoUltimaMensagem.lower() == "um":
                    
                    mensagem = """Tabela de preços."""

                elif textoUltimaMensagem == "2" or textoUltimaMensagem.lower() == "marcar horário" or textoUltimaMensagem.lower() == "marcar" or textoUltimaMensagem.lower() == "horário" or textoUltimaMensagem.lower() == "two" or textoUltimaMensagem.lower() == "dois":

                    mensagem = """Marcar horário."""

                elif textoUltimaMensagem == "3" or textoUltimaMensagem.lower() == "falar com um atendente humano" or textoUltimaMensagem.lower() == "falar" or textoUltimaMensagem.lower() == "atendente" or textoUltimaMensagem.lower() == "humano" or textoUltimaMensagem.lower() == "three" or textoUltimaMensagem.lower() == "três":
                
                    mensagem = """Você optou por falar com um atendente humano. Quando desejar retornar ao atendimento com o robô, digite "voltar". O atendente humano entrará em contato em breve."""
                    atendimentoHumano.append(nome)
                    
                elif textoUltimaMensagem.lower() == "voltar":
                    
                    mensagem = """Você optou por voltar ao atendimento com Samy.\nDigite o número relacionado com o que eu posso fazer por você:\n\n1- Tabela de preços\n2 - Marcar horário\n3 - Falar com um atendente humano"""

                else:
                    mensagem = "Não entendi o que você quis dizer."
                if mensagem != "":
                    mensagem = mensagem.split("\n")
                    caixaMensagem = WebDriverWait(navegador, 5).until(
                        EC.presence_of_element_located((By.CLASS_NAME, "_3Uu1_")))
                    for texto in mensagem:
                        caixaMensagem.send_keys(texto)
                        caixaMensagem.send_keys(Keys.SHIFT, Keys.ENTER)
                caixaMensagem.send_keys(Keys.RETURN)
                opcoes2 = WebDriverWait(navegador, 5).until(EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="main"]/header/div[3]/div/div[3]/div/div/span')))
                opcoes2.click()
                time.sleep(1)
                fecharConversa = WebDriverWait(navegador, 5).until(EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="app"]/div/span[4]/div/ul/div/div/li[3]/div')))
                fecharConversa.click()
                print(nome, usuariosAtendidos)
                time.sleep(3)
    except:
        time.sleep(1)
        continue
