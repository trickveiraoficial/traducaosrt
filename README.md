### README

# Tradutor de Arquivos SRT

Este script automatiza a tradução de arquivos `.srt` (legendas) utilizando o Microsoft Translator API. Ele processa os arquivos de uma pasta de entrada, traduzindo apenas o texto relevante (ignora números e timestamps) e salva os resultados em uma pasta de saída.

---

## Pré-requisitos

- **Python 3.6 ou superior**: Certifique-se de ter o Python instalado no seu sistema.
- **Biblioteca Requests**: Instale-a executando o comando:

  ```bash
  pip install requests
  ```

- **Chave de Subscrição do Microsoft Translator API**:
  - Você deve criar uma conta no Azure e configurar o recurso "Translator".
  - Gere uma chave de subscrição e obtenha as informações da região e do endpoint.

---

## Configuração

1. **Clone ou baixe o repositório.**

2. **Personalize as variáveis no script**:
   - `input_dir`: Caminho absoluto para a pasta onde os arquivos `.srt` estão localizados.
   - `output_dir`: Caminho absoluto para a pasta onde os arquivos traduzidos serão salvos.
   - `subscription_key`: Sua chave de subscrição do Translator.
   - `region`: Região associada ao serviço Translator.
   - `endpoint`: Endpoint do Translator fornecido pelo Azure.

   **Exemplo:**
   ```python
   input_dir = r"C:\MeusArquivos\SRT"
   output_dir = r"C:\MeusArquivos\Traduzidos"
   subscription_key = "minha-chave-de-subscrição"
   region = "brazilsouth"
   endpoint = "https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&to=pt"
   ```

3. **Prepare as pastas de entrada e saída**:
   - Coloque os arquivos `.srt` na pasta especificada por `input_dir`.
   - Certifique-se de que a pasta especificada em `output_dir` existe ou será criada pelo script.

---

## Como usar

1. **Execute o script**:
   Navegue até a pasta onde o script está localizado e execute-o com:

   ```bash
   python nome_do_arquivo.py
   ```

2. **Saída**:
   - Os arquivos traduzidos serão salvos na pasta especificada em `output_dir`.
   - O console exibirá mensagens indicando o progresso e erros, se houver.

---

## Funcionamento

1. **Tradução**:
   - O script lê cada arquivo `.srt` na pasta de entrada.
   - Traduz apenas o texto relevante (ignora números e timestamps).
   - Utiliza o endpoint do Translator para enviar o texto e receber a tradução.

2. **Tratamento de Erros**:
   - Caso ocorra um erro ao traduzir uma linha, o script registra o erro no console e mantém a linha original no arquivo traduzido.

3. **Resultados**:
   - Os arquivos traduzidos terão o mesmo nome que os originais, mas estarão localizados na pasta de saída.

---

## Exemplo de Uso

- Arquivo original (`input_dir\exemplo.srt`):
  ```
  1
  00:00:00,000 --> 00:00:02,000
  Olá, como você está?

  2
  00:00:02,000 --> 00:00:04,000
  Este é um exemplo de tradução.
  ```

- Arquivo traduzido (`output_dir\exemplo.srt`):
  ```
  1
  00:00:00,000 --> 00:00:02,000
  Hello, how are you?

  2
  00:00:02,000 --> 00:00:04,000
  This is an example of translation.
  ```

---

## Licença

Este projeto é distribuído sob a licença MIT. Sinta-se livre para usar e modificar conforme necessário.

--- 

### Autor
Patrick Oliveira
