# 📜 Tradutor de Arquivos SRT

Este script automatiza a tradução de arquivos `.srt` (legendas) utilizando a **Microsoft Translator API**. Ele processa arquivos de uma pasta de entrada, traduzindo apenas o texto relevante (ignorando números e timestamps) e salva os resultados em uma pasta de saída.

---

## 🚀 Pré-requisitos

### 🔹 Requisitos de Software
- **Python 3.6 ou superior**
- **Biblioteca Requests** (instale executando o comando abaixo):

  ```bash
  pip install requests
  ```

### 🔹 Configuração do Microsoft Translator API
- Criar uma conta no **Azure**.
- Configurar o recurso **Translator**.
- Gerar uma **chave de subscrição** e obter as informações de **região** e **endpoint**.

---

## ⚙️ Configuração

### 1️⃣ Clone ou Baixe o Repositório
```bash
git clone https://github.com/seu-usuario/tradutor-srt.git
cd tradutor-srt
```

### 2️⃣ Personalize as Variáveis no Script
Edite o script para definir os diretórios de entrada e saída, além das credenciais da API:

```python
input_dir = r"C:\MeusArquivos\SRT"
output_dir = r"C:\MeusArquivos\Traduzidos"
subscription_key = "minha-chave-de-subscrição"
region = "brazilsouth"
endpoint = "https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&to=pt"
```

### 3️⃣ Prepare as Pastas de Entrada e Saída
- Coloque os arquivos `.srt` na pasta especificada por `input_dir`.
- Certifique-se de que a pasta `output_dir` existe ou será criada pelo script.

---

## ▶️ Como Usar

1. **Execute o Script**
   Navegue até a pasta onde o script está localizado e execute:

   ```bash
   python nome_do_arquivo.py
   ```

2. **Saída**
   - Os arquivos traduzidos serão salvos em `output_dir`.
   - O console exibirá mensagens indicando o progresso e erros, se houver.

---

## 🔍 Funcionamento

### 📝 Processo de Tradução
- O script **lê** cada arquivo `.srt` da pasta de entrada.
- **Traduz** apenas o texto relevante, ignorando timestamps.
- **Envia** o texto para a API do Translator e recebe a tradução.

### ⚠️ Tratamento de Erros
- Caso ocorra um erro ao traduzir uma linha, o script **registra o erro** no console e **mantém a linha original** no arquivo traduzido.

### 📂 Estrutura dos Arquivos

**Arquivo Original (`input_dir/exemplo.srt`)**:
```srt
1
00:00:00,000 --> 00:00:02,000
Olá, como você está?

2
00:00:02,000 --> 00:00:04,000
Este é um exemplo de tradução.
```

**Arquivo Traduzido (`output_dir/exemplo.srt`)**:
```srt
1
00:00:00,000 --> 00:00:02,000
Hello, how are you?

2
00:00:02,000 --> 00:00:04,000
This is an example of translation.
```

---

## 📜 Licença

Este projeto é distribuído sob a **licença MIT**. Sinta-se livre para usar e modificar conforme necessário.

---

## 👤 Autor
**Patrick Oliveira**

