import os
import requests

# Definindo as variáveis
input_dir = r"PASTA-ARQUIVOS-SRT"
output_dir = r"PASTA-SRT-TRADUZIDOS"
subscription_key = "SUA-CHAVE-DE-SUBSCRIÇÃO"
region = "REGIÃO-DA-SUBSCRIÇÃO"
endpoint = f"SEU-ENDPOINT-DO-TRANSLATOR"

# Função para traduzir o texto
def traduzir_texto(texto):
    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Ocp-Apim-Subscription-Region': region,
        'Content-Type': 'application/json'
    }

    body = [{
        'Text': texto
    }]

    response = requests.post(endpoint, headers=headers, json=body)
    response.raise_for_status()

    return response.json()[0]['translations'][0]['text']

# Função para processar os arquivos .srt
def processar_arquivos():
    # Criando a pasta de saída se não existir
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.endswith(".srt"):
            caminho_entrada = os.path.join(input_dir, filename)
            caminho_saida = os.path.join(output_dir, filename)

            # Abrindo o arquivo SRT para ler
            with open(caminho_entrada, 'r', encoding='utf-8') as file:
                conteudo = file.readlines()

            novo_conteudo = []
            for linha in conteudo:
                if linha.strip() and not linha.strip().isdigit() and '-->' not in linha:
                    try:
                        # Traduzindo o texto (ignorando números e timestamps)
                        nova_linha = traduzir_texto(linha.strip())
                        novo_conteudo.append(nova_linha + '\n')
                    except Exception as e:
                        print(f"Erro ao traduzir: {linha} - Erro: {e}")
                        novo_conteudo.append(linha)
                else:
                    novo_conteudo.append(linha)

            # Salvando o arquivo traduzido
            with open(caminho_saida, 'w', encoding='utf-8') as file:
                file.writelines(novo_conteudo)

            print(f"Arquivo traduzido: {filename}")

if __name__ == "__main__":
    processar_arquivos()
