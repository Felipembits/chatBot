# Dê o comando: pip install selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime

print("It's running!")

# Abrindo o navegador e redirecionando para o WhatsApp Web
navegador = webdriver.Edge()
navegador.maximize_window()
navegador.get("https://web.whatsapp.com/")

# Lista de usuários em atendimento humano
atendimentoHumano = []
erros = []
# Obtém a data atual
ultimaExecucao = datetime.datetime.now().strftime("%d-%m-%Y")

# Lê a última execução a partir do arquivo ultimaExecucao.txt
with open('ultimaExecucao.txt', 'r') as arquivoUltimaExecucao:
    ultimaExecucaoTxt = arquivoUltimaExecucao.read().strip()

# Converte o texto de ultimaExecucao.txt para um objeto datetime, se houver
if ultimaExecucaoTxt:
    ultimaExecucaoSalva = ultimaExecucaoTxt 
else:
    ultimaExecucaoSalva = None

print(
    f"Última execução: {ultimaExecucaoSalva}, data e hora atual: {ultimaExecucao}")

# Se a última execução for diferente da última salva, atualiza o arquivo usuariosAtendidos.txt
if str(ultimaExecucao) != ultimaExecucaoSalva:
    with open('usuariosAtendidos.txt', 'w') as arquivoNomes:
        arquivoNomes.write("")
        print("Arquivo 'usuariosAtendidos.txt' apagado com sucesso.")
    with open('ultimaExecucao.txt', 'w') as arquivoUltimaExecucao:
        arquivoUltimaExecucao.write(ultimaExecucao)
    usuariosAtendidos = []
else:
    # Lê a lista de usuários atendidos do arquivo
    with open('usuariosAtendidos.txt', 'r') as arquivo:
        usuariosAtendidos = [linha.strip()
                             for linha in arquivo.readlines() if linha.strip()]
while len(navegador.find_elements(By.ID, "side")) < 1:
    time.sleep(1)
filtro = WebDriverWait(navegador, 5).until(EC.presence_of_element_located(
    (By.XPATH, '//*[@id="side"]/div[1]/div/button/div/span')))
filtro.click()
time.sleep(5)
while True:
    # Verificando os usuários atendidos anteriormente e adicionando-os à lista
    with open('usuariosAtendidos.txt', 'a+') as arquivo:
        # Move o ponteiro para o início do arquivo
        arquivo.seek(0)

        # Lê o conteúdo atual do arquivo e armazena em uma lista
        usuarios_no_arquivo = arquivo.read().split("\n")

        # Itera sobre os usuários
        for usuario in usuariosAtendidos:
            # Verifica se o usuário já está no arquivo
            if usuario not in usuarios_no_arquivo:
                # Adiciona o usuário ao arquivo
                arquivo.write(f"{usuario}\n")
                print(
                    f"Usuário '{usuario}' adicionado ao arquivo 'usuariosAtendidos.txt' com sucesso.")
    try:
        # Obtém todas as conversas não lidas
        todasConversasNaoLidas = WebDriverWait(navegador, 5).until(EC.presence_of_all_elements_located(
            (By.CLASS_NAME, 'ggj6brxn.gfz4du6o.r7fjleex.g0rxnol2.lhj4utae.le5p0ye3.l7jjieqr._11JPr')))

        # Filtra as conversas não lidas
        conversasNaoLidas = [conversa for conversa in todasConversasNaoLidas]

        # seleciona a primeira conversa não lida da lista
        conversa = conversasNaoLidas[0]

        for conversa in conversasNaoLidas if conversasNaoLidas != "" else time.sleep(1):
            mensagemPreview = WebDriverWait(navegador, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "p357zi0d.r15c9g6i")))
            if mensagemPreview.text.lower() == "voltar" and conversa.text in atendimentoHumano:
                atendimentoHumano.remove(conversa.text)
                conversa.click()
                mensagem = """Você optou por voltar ao atendimento com Samy.\nDigite o número relacionado com o que eu posso fazer por você:\n\n1- Tabela de preços\n2 - agendar reunião\n3 - Atendimento humano"""
                mensagem = mensagem.split("\n")
                caixaMensagem = WebDriverWait(navegador, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "_3Uu1_")))

                for texto in mensagem:
                    caixaMensagem.send_keys(texto)
                    caixaMensagem.send_keys(Keys.SHIFT, Keys.ENTER)

                caixaMensagem.send_keys(Keys.RETURN)
                opcoes2 = WebDriverWait(navegador, 5).until(EC.presence_of_element_located(
                    (By.CLASS_NAME, 'kiiy14zj')))
                opcoes2.click()
                time.sleep(1)
                fecharConversa = WebDriverWait(navegador, 5).until(EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="app"]/div/span[4]/div/ul/div/div/li[3]/div')))
                fecharConversa.click()

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
                textosMensagens = [
                    mensagem.text for mensagem in todasMensagens]
                textoUltimaMensagem = textosMensagens[-1]
                print(textoUltimaMensagem)

                # Responda a mensagem do cliente
                mensagem = ""

                if textoUltimaMensagem.lower() in ["ola boa noite", "oi boa noite", "ola, boa noite.", "oi, boa noite", "ola, boa noite", "oi, boa noite.", "boa noite", "boa noite!"]:

                    mensagem = f"""Boa noite! Eu sou Samy. Uma robô assistente.\nPor favor, digite o número relacionado com o que eu posso fazer por você:\n\n1- Tabela de preços\n2 - agendar reunião\n3 - Atendimento humano"""
                    usuariosAtendidos.append(nome)

                elif textoUltimaMensagem.lower() in ["ola bom dia", "oi bom dia", "ola, bom dia.", "oi, bom dia", "ola, bom dia", "oi, bom dia.", "bom dia", "bom dia!"]:

                    mensagem = """Bom dia! Eu sou Samy. Uma Robô assistente.\nPor favor, digite o número relacionado com o que eu posso fazer por você:\n\n1- Tabela de preços\n2 - agendar reunião\n3 - Atendimento humano"""
                    usuariosAtendidos.append(nome)

                elif textoUltimaMensagem.lower() in ["ola boa tarde", "oi boa tarde", "ola, boa tarde.", "oi, boa tarde", "ola, boa tarde", "oi, boa tarde.", "boa tarde", "boa tarde!"]:

                    mensagem = """Boa tarde! Eu sou Samy. Uma Robô assistente.\nPor favor, digite o número relacionado com o que eu posso fazer por você:\n\n1- Tabela de preços\n2 - agendar reunião\n3 - Atendimento humano"""
                    usuariosAtendidos.append(nome)

                elif nome not in usuariosAtendidos:

                    mensagem = """Olá, eu sou Samy. Uma Robô assistente.\nPor favor, digite o número relacionado com o que eu posso fazer por você:\n\n1- Tabela de preços\n2 - agendar reunião\n3 - Atendimento humano"""
                    usuariosAtendidos.append(nome)

                elif textoUltimaMensagem.lower() in ["1", "Tabela de preços", "tabela", "preços", "one", "um", "preco", "preço", "preço", "preco", "uno", "11", "1-", "1 -"]:

                    mensagem = """Os preços de uma landing page podem variar de acordo com a complexidade do projeto. Podendo custar entre R$ 500,00 e R$ 1.500,00.\n"""

                elif textoUltimaMensagem.lower() in ["2", "2-", "2 -", "marcar reunião", "marcar", "reunião", "two", "dois", "agendar reunião", "agendar", "agendar reuniao", "agendar reuniao", "marca", "agenda"]:

                    mensagem = """Para agendar uma reunião, acesse o link: https://calendly.com/felipebittencourt-4-o\nSelecione o serviço desejado e o reunião disponível, em seguida preencha com seu nome e email para identificação."""

                elif textoUltimaMensagem.lower() in ["3", "3-", "3 -", "atendimento humano", "atendimento", "humano", "three", "três", "humano"]:

                    mensagem = """Você optou por falar com um atendente humano. Quando desejar retornar ao atendimento com a Samy, digite "voltar". O atendente humano entrará em contato assim que possível."""
                    atendimentoHumano.append(nome)

                elif textoUltimaMensagem.lower() in ["obrigado", "obrigada", "brigado", "brigada", "obg", "obgd", "valeu", "vlw", "obrigado!", "obrigada!", "brigado!", "brigada!", "obg!", "obgd!", "valeu!", "vlw!", "obrigado.", "obrigada.", "brigado.", "brigada.", "obg.", "obgd.", "valeu.", "vlw.", "muito obrigado", "muito obrigada", "brigadão", "obrigadão"]:

                    mensagem = "Por nada! Estou aqui para ajudar."

                elif textoUltimaMensagem.lower() in ['valida', 'válida', 'mensagem', 'mensagem válida', 'mensagem valida']:
                    mensagem = "Engraçadinho(a) você, hein?"

                elif erros.count(nome) < 3:
                    if erros.count(nome) == 0:
                        mensagem = "Desculpa, não entendi o que você quis dizer. Por favor, envie uma mensagem válida."
                    elif erros.count(nome) == 1:
                        mensagem = "Por ser uma robô assistente, ainda não consigo entender tudo o que você diz. Por favor, envie uma mensagem válida."
                    elif erros.count(nome) == 2:
                        mensagem = "Peço perdão, não consegui entender. Por favor, envie uma mensagem válida."
                    erros.append(nome)

                else:
                    mensagem = "Talvez tenha ocorrido uma falha na nossa comunicação. Por favor, digite o número relacionado com o que eu posso fazer por você:\n\n1- Tabela de preços\n2 - agendar reunião\n3 - Atendimento humano"
                    erros.remove(nome)
                    erros.remove(nome)
                    erros.remove(nome)
                if mensagem != "":
                    mensagem = mensagem.split("\n")
                    caixaMensagem = WebDriverWait(navegador, 5).until(
                        EC.presence_of_element_located((By.CLASS_NAME, "_3Uu1_")))

                    for texto in mensagem:
                        caixaMensagem.send_keys(texto)
                        caixaMensagem.send_keys(Keys.SHIFT, Keys.ENTER)

                caixaMensagem.send_keys(Keys.RETURN)
                opcoes2 = WebDriverWait(navegador, 5).until(EC.presence_of_element_located(
                    (By.CLASS_NAME, 'kiiy14zj')))
                opcoes2.click()
                time.sleep(1)
                fecharConversa = WebDriverWait(navegador, 5).until(EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="app"]/div/span[4]/div/ul/div/div/li[3]/div')))
                fecharConversa.click()
                print(nome, usuariosAtendidos)

    except:
        time.sleep(1)
        continue
