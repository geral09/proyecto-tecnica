from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = "secret_key"

# Array de preguntas y respuestas correctas
questions = [
    {"question": "What is the capital of England?", "answers": ["London", "Paris", "Rome", "Berlin"], "correct": 0},
    {"question": "What is the past tense of 'go'?", "answers": ["go", "went", "goes", "going"], "correct": 1},
    {"question": "What is the meaning of 'hello' in Spanish?", "answers": ["hola", "adiós", "gracias", "¿cómo estás?"], "correct": 0},
    # ...
]

# Inicializar sesión para almacenar respuestas del usuario
@app.before_request
def init_session():
    if "user_answers" not in session:
        session["user_answers"] = []

# Ruta para mostrar la pregunta actual
@app.route("/", methods=["GET"])
def show_question():
    if len(session["user_answers"]) < len(questions):
        question = questions[len(session["user_answers"])]
        return render_template("question.html", question=question)
    else:
        return redirect(url_for("show_results"))

# Ruta para procesar la respuesta del usuario
@app.route("/answer", methods=["POST"])
def process_answer():
    answer = int(request.form["answer"])
    session["user_answers"].append(answer)
    return redirect(url_for("show_question"))

# Ruta para mostrar los resultados
@app.route("/results", methods=["GET"])
def show_results():
    user_answers = session["user_answers"]
    correct_answers = [q["correct"] for q in questions]
    score = sum([1 for i in range(len(user_answers)) if user_answers[i] == correct_answers[i]])
    correct_count = sum([1 for i in range(len(user_answers)) if user_answers[i] == correct_answers[i]])
    incorrect_count = len(user_answers) - correct_count
    return render_template("results.html", score=score, correct_count=correct_count, incorrect_count=incorrect_count)

if __name__ == "__main__":
    app.run(debug=True)