# Calculadora Python (GUI e API)

Este repositório contém o código para uma aplicação de calculadora básica desenvolvida em Python, dividida em duas partes principais:
1.  Uma **aplicação de desktop com interface gráfica (GUI)** construída com a biblioteca padrão `Tkinter`.
2.  Uma **API REST** que expõe a lógica de cálculo, construída com o micro-framework `Flask`.

## Funcionalidades

### Calculadora GUI
-   Interface gráfica de calculadora de desktop.
-   Operações de adição, subtração, multiplicação e divisão.
-   Interface intuitiva com tela de exibição e botões de fácil acesso.
-   Botão para limpar a tela (`C`).

### API REST
-   Endpoint (`/calcular`) para realizar cálculos remotamente via requisições HTTP.
-   Comunicação padronizada utilizando o formato JSON.
-   Lógica de negócio desacoplada, permitindo que diferentes clientes (web, mobile, etc.) a consumam.

## Pré-requisitos

Antes de começar, garanta que você tenha os seguintes softwares instalados:
-   **Python 3.8 ou superior**
-   **pip** (geralmente incluído na instalação do Python)

## Instalação e Configuração

Siga os passos abaixo para configurar o ambiente de desenvolvimento local.

**1. Clone o repositório:**
```bash
git clone [https://github.com/seu-usuario/nome-do-repositorio.git](https://github.com/seu-usuario/nome-do-repositorio.git)
cd nome-do-repositorio
```

**2. Crie um ambiente virtual (venv):**
É uma boa prática isolar as dependências do projeto. O comando a seguir cria uma pasta chamada `venv` no diretório do projeto.
```bash
python -m venv venv
```

**3. Ative o ambiente virtual:**
A ativação precisa ser feita toda vez que você for trabalhar no projeto em um novo terminal.

-   **No Windows (PowerShell/CMD):**
    ```bash
    .\venv\Scripts\activate
    ```
-   **No Linux ou macOS:**
    ```bash
    source venv/bin/activate
    ```
    Após a ativação, você verá `(venv)` no início do seu prompt de comando.

**4. Instale as dependências:**
Com o ambiente virtual ativado, instale as bibliotecas listadas no arquivo `requirements.txt`.
```bash
pip install -r requirements.txt
```

## Como Usar

A aplicação é dividida em duas partes que podem ser executadas de forma independente.

### Executando a Calculadora Desktop (GUI)

Para abrir a calculadora de desktop, execute o seguinte comando no seu terminal:
```bash
python calculadora_gui.py
```
Isso abrirá a janela da calculadora em seu desktop.

### Executando a API REST

Para iniciar o servidor da API, execute o seguinte comando:
```bash
python calculadora_api.py
```
O terminal indicará que o servidor está rodando, geralmente no endereço `http://127.0.0.1:5000`.

Você pode testar o endpoint `/calcular` usando uma ferramenta como `curl` ou Postman.

**Exemplo de requisição com `curl` para somar 20 e 15:**
```bash
curl -X POST [http://127.0.0.1:5000/calcular](http://127.0.0.1:5000/calcular) \
-H "Content-Type: application/json" \
-d '{"operando1": 20, "operando2": 15, "operacao": "adicionar"}'
```

**Resposta esperada:**
```json
{
  "resultado": 35.0,
  "detalhes": "20 adicionar 15"
}
```

## Estrutura do Projeto
```
calculadora-python
├── calculadora_gui.py     # Código da aplicação desktop com Tkinter
├── calculadora_api.py     # Código da API REST com Flask
├── operacoes.py           # Lógica das operações matemáticas
├── requirements.txt       # Lista de dependências Python para a API
└── README.md              # Este arquivo de instruções
```

## Tecnologias Utilizadas
-   **Python 3**
-   **Tkinter** - Para a interface gráfica (GUI).
-   **Flask** - Para a API REST.