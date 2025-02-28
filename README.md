# Gerador de Questões para Vestibulares

Este é um aplicativo web construído com Flask que gera perguntas de múltipla escolha baseadas em um tópico especificado pelo usuário. As questões são formatadas no padrão de vestibulares concorridos como ENEM, UFPR e Fuvest, e podem ser baixadas em formato CSV.
![imagem do projeto](/static/Design%20AnswerAi.png)

## Tecnologias Utilizadas
- Python (Flask)
- OpenAI API
- Pandas
- Dotenv
- HTML e Jinja2 para templates

## Funcionalidades
- Geração automática de perguntas de múltipla escolha com alternativas e respostas corretas.
- Possibilidade de especificar o número de perguntas desejadas.
- Interface web para entrada do tópico e visualização das questões geradas.
- Opção de download das questões em formato CSV.

## Como Usar
### 1. Clonar o Repositório
```sh
git clone <URL_DO_REPOSITORIO>
cd <NOME_DO_REPOSITORIO>
```

### 2. Criar um Ambiente Virtual
```sh
python -m venv venv
source venv/bin/activate  # No Windows, use: venv\Scripts\activate
```

### 3. Instalar Dependências
```sh
pip install -r requirements.txt
```

### 4. Configurar a API Key da OpenAI
Crie um arquivo `.env` na raiz do projeto e adicione:
```sh
OPENAI_API_KEY=seu_token_aqui
```

### 5. Executar a Aplicação
```sh
python app.py
```
Acesse no navegador: [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Estrutura do Projeto
```
/
├── templates/
│   ├── index.html  # Template principal
├── static/
│   ├── styles.css  # Estilos opcionais
├── app.py          # Código principal do Flask
├── requirements.txt # Dependências do projeto
├── .env            # Chave de API da OpenAI (não commitada)
└── README.md       # Documentação do projeto
```

## Exemplo de Uso
1. Digite um tópico no campo de entrada, por exemplo: `10 perguntas sobre fotossíntese`.
2. O sistema gerará 10 perguntas no formato de múltipla escolha.
3. Você pode visualizar as perguntas diretamente na página.
4. Opção de download do arquivo CSV com todas as perguntas e respostas.

## Melhorias Futuras
- Adição de suporte para mais formatos de exportação (PDF, JSON).
- Implementação de um banco de dados para armazenar histórico de perguntas geradas.
- Interface mais interativa com seleção de dificuldade.

## Licença
Este projeto está sob a licença MIT.

