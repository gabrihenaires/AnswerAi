from flask import Flask, render_template, request, send_file, redirect, url_for
from dotenv import load_dotenv
import os
import openai
import pandas as pd
import io
import re

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

# Configurar o Flask
app = Flask(__name__)

# Função para extrair o número de perguntas da solicitação do usuário
def extract_num_questions(user_input):
    match = re.search(r'(\d+)\s+perguntas?', user_input, re.IGNORECASE)
    return int(match.group(1)) if match else 5  # Se não encontrar, usa 5 como padrão

# Função para limpar o tópico, removendo o número de perguntas
def clean_topic(user_input):
    return re.sub(r'\d+\s+perguntas?\s+sobre\s+', '', user_input, flags=re.IGNORECASE).strip()

def generate_questions_answers(topic, num_questions): 
    system_message = "Você é uma IA especializada em criar questões educacionais para estudantes de cursinho pré-vestibular, especialmente aqueles que almejam aprovação em Medicina."

    user_messages = [
        {"role": "user", "content": f"Gere {num_questions} perguntas de múltipla escolha sobre {topic}."},
        {"role": "user", "content": "Cada pergunta deve ter cinco alternativas (A, B, C, D, E), sendo apenas uma delas correta."},
        {"role": "user", "content": "As perguntas devem estar no nível de dificuldade esperado para vestibulares concorridos, como ENEM, UFPR, Fuvest."},
        {"role": "user", "content": "O enunciado deve ser claro, objetivo e sem ambiguidades."},
        {"role": "user", "content": "A alternativa correta deve ser baseada em fatos comprovados e aceitos academicamente, sem margem para especulação ou respostas erradas."},
        {"role": "user", "content": "No final de cada pergunta, informe a alternativa correta com uma explicação breve sobre o porquê ela está certa."},
        {"role": "user", "content": "Indique a alternativa correta junto com a descrição da resposta no final, exemplo: Resposta Correta: C) Paris. Com um breve resumo da resposta ao final."},
        {"role": "user", "content": "Separe as perguntas apenas por quebras de linha. Não utilize caracteres especiais ou espaços extras entre perguntas e respostas."},
        {"role": "user", "content": "As perguntas devem ser enumeradas corretamente de 1 a " + str(num_questions) + "."},
        {"role": "user", "content": ( 
            "As perguntas devem seguir este formato:"
            "Qual é a principal função do sistema circulatório no corpo humano?\n"
            "A) Respiração\n"
            "B) Digestão\n"
            "C) Transporte de nutrientes e oxigênio\n"
            "D) Excreção de resíduos\n"
            "E) Regulação da temperatura corporal\n"
            "Resposta Correta: C) Transporte de nutrientes e oxigênio. O sistema circulatório é responsável por transportar nutrientes, oxigênio, hormônios e outras substâncias essenciais para as células do corpo, além de remover resíduos metabólicos."
        )},
        
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0,
        messages=[{"role": "system", "content": system_message}] + user_messages,
    )

    return response["choices"][0]["message"]["content"]

def format_qa_to_csv(qa_content):
    qa_list = [line.strip() for line in qa_content.strip().split("\n") if line.strip()]
    data = []
    i = 0
    
    while i < len(qa_list):
        # Identifica a pergunta como qualquer linha que não seja uma alternativa
        if not re.match(r"^[A-E]\)", qa_list[i]):  
            try:
                question = qa_list[i]
                option_a = qa_list[i+1] if i+1 < len(qa_list) else "Opção A indisponível"
                option_b = qa_list[i+2] if i+2 < len(qa_list) else "Opção B indisponível"
                option_c = qa_list[i+3] if i+3 < len(qa_list) else "Opção C indisponível"
                option_d = qa_list[i+4] if i+4 < len(qa_list) else "Opção D indisponível"
                option_e = qa_list[i+5] if i+5 < len(qa_list) else "Opção E indisponível"
                correct_answer = qa_list[i+6].replace("Resposta correta:", "").strip() if i+6 < len(qa_list) else "Resposta Indisponível"

                formatted_question = f'{question}\n{option_a}\n{option_b}\n{option_c}\n{option_d}\n{option_e}'
                formatted_answer = f'{correct_answer}'

                data.append([formatted_question, formatted_answer])
                i += 7  # Avança para a próxima pergunta
            except IndexError:
                break
        else:
            i += 1  

    df = pd.DataFrame(data)
    csv_buffer = io.BytesIO()
    df.to_csv(csv_buffer, index=False, header=False, encoding="utf-8", quotechar='"')
    csv_buffer.seek(0)
    return csv_buffer

# Rota principal
@app.route("/", methods=["GET", "POST"])
def index():
    questions = None
    qa_content = None
    if request.method == "POST":
        user_prompt = request.form.get("topic")

        if not user_prompt:
            return "Erro: Você deve informar um tópico!", 400

        num_questions = extract_num_questions(user_prompt)  # Identifica o número de perguntas
        topic = clean_topic(user_prompt)  # Remove a contagem da frase

        qa_content = generate_questions_answers(topic, num_questions)
        questions = qa_content

        return render_template("index.html", questions=questions, qa_content=qa_content)

    return render_template("index.html", questions=questions)

# Rota de download do CSV
@app.route("/download_csv")
def download_csv():
    qa_content = request.args.get("qa_content")
    if qa_content:
        csv_buffer = format_qa_to_csv(qa_content)
        return send_file(csv_buffer, mimetype="text/csv", as_attachment=True, download_name="perguntas_respostas.csv")
    return "Erro: Nenhum conteúdo encontrado", 400

# Rodar a aplicação
if __name__ == "__main__":
    app.run(debug=True)
