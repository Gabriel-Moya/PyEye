# PyEye
Esse projeto tem como objetivo principal realizar a leitura de um documento em `PDF` que tenha sido scaneado e convertê-lo em um documento `.docx` editável extraindo o texto através de visão computacional com o `pytesseract`.


# Funcionamento
Para converter um arquivo `PDF` para `.docx` basta deixar um arquivo chamado `contrato.pdf` dentro da pasta `assets` e executar o `main.py`, ele irá realizar a leitura do arquivo, extrair o texto e gerar um novo arquivo `contrato.docx` dentro da mesma pasta.

# Dependências externas
Para funcionar corretamente temos algumas dependências que precisam ser instaladas na máquina, que não é possível importar diretamente pelo código nem com instalação de dependência do próprio projeto. Dependências quais, estarão listadas abaixo com as devidas referências para download diretamente da fonte oficial, caso tenha problemas para baixar, deixarei uma cópia de cada uma na pasta `resources`.

## pytesseract
O `pytesseract` é o responsável por fazer a leitura das páginas e extrair os textos.
Instruções de instalação são encontradas diretamente no repositório oficial [aqui](https://github.com/tesseract-ocr/tesseract).

Obs: Para um correto funcionamento para documentos em português, é necessário o pacote de idioma para reconhecimento de textos em português. A lista com todos os idiomas estão listadas [aqui](https://github.com/tesseract-ocr/tessdata). O pacote em português é o arquivo `por.traineddata`, também disponível nos `resources` juntamente com o `tesseract-5.3.3.zip`.

## Poppler
`Poppler` é uma ferramenta para funcionar em conjunto com o pacote `pdf2image` que estamos usando para extrair a imagem de dentro do `PDF` para que seja possível o reconhecimento com o `pytesseract`. Após a instalação do `Poppler` é necessário adicionar o caminho da pasta `bin` às variáveis de ambiente.

Por exemplo, se você extrair para o diretório
```
C:\Poppler
```

Você irá adicionar o caminho abaixo nas variáveis de ambiente:
```
C:\Poppler\bin
```

# Executando o projeto
## Passo 1 - Instalar o virtualenv
Instale o virtualenv para trabalhar com ambientes virtuais no python utilizando o comando:
```
pip install virtualenv
```
Caso dê problema com a versão do pip atual, atualize o pip utilizando:
```
python -m pip install --upgrade pip
```

## Passo 2 - Ative o virtualenv
Para ativar o ambiente virtual rode:
```
virtualenv venv
```

## Passo 3 - (Depende do seu sistema operacional)
### Windows
```
.\venv\Scripts\activate
```

### Linux
```
source venv/bin/activate
```
Para saber se deu certo a ativação, basta ver se fica ```(venv)``` aparecendo antes do caminho no terminal

Com o ambiente virtual ativado, toda instalação de biblioteca externa fica somente no ambiente virtual, ao invés de sujar sua instalação do python na máquina local

Com o ambiente virtual instalado, execute o comando abaixo para instalar as dependências
```
pip install -r requirements.txt
```

# Observações
Esse projeto não foi testado no linux, todas as intalações das dependências externas foram realizadas no Windows 10