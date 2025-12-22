from flask import Flask, render_template, request, redirect, session
import sqlite3
import pandas as pd
import spacy
from PyPDF2 import PdfReader
from werkzeug.security import generate_password_hash, check_password_hash
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

# ---------------- APP CONFIG ----------------
app = Flask(__name__)
app.secret_key = "secretkey"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ---------------- NLP ----------------
nlp = spacy.load("en_core_web_sm")

# ---------------- DATA ----------------
skills_df = pd.read_csv(os.path.join(BASE_DIR, "skills.csv"))
skill_weights = dict(zip(skills_df.skill, skills_df.weight))
skill_list = skills_df.skill.str.lower().tolist()

# ---------------- DATABASE ----------------
def get_db():
    return sqlite3.connect('database.db')

# ---------------- UTIL FUNCTIONS ----------------
def extract_text(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()
    return text.lower()

def extract_skills(text):
    doc = nlp(text)
    return {token.text.lower() for token in doc if token.text.lower() in skill_list}

def similarity_score(resume, jd):
    vec = TfidfVectorizer()
    mat = vec.fit_transform([resume, jd])
    return round(cosine_similarity(mat[0], mat[1])[0][0] * 100, 2)

def weighted_score(skills):
    return sum(skill_weights.get(skill, 1) for skill in skills)

# ---------------- ROUTES ----------------

@app.route("/", methods=["GET", "POST"])
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        pwd = request.form['password']

        conn = sqlite3.connect('database.db')
        cur = conn.cursor()

        cur.execute("SELECT password FROM users WHERE username=?", (user,))
        data = cur.fetchone()

        conn.close()

        if data and data[0] == pwd:
            session['user'] = user
            return redirect('/dashboard')
        else:
            return "Invalid credentials"

    return render_template('login.html')

@app.route("/register", methods=["GET", "POST"])
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user = request.form['username']
        pwd = request.form['password']

        conn = sqlite3.connect('database.db')
        cur = conn.cursor()

        cur.execute("INSERT INTO users (username, password) VALUES (?,?)",
                    (user, pwd))
        conn.commit()
        conn.close()

        return redirect('/')

    return render_template('register.html')


@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if "user" not in session:
        return redirect("/")

    if request.method == "POST":
        resume = extract_text(request.files["resume"])
        jd = request.form["jd"].lower()

        r_skills = extract_skills(resume)
        jd_skills = extract_skills(jd)

        sim = similarity_score(resume, jd)
        weight = weighted_score(r_skills & jd_skills)

        match_pct = 0
        ats = 0
        warning = None

        if len(jd_skills) == 0:
            warning = "⚠️ No recognizable skills found in Job Description."
        else:
            match_pct = (len(r_skills & jd_skills) / len(jd_skills)) * 100
            ats = round(min(0.4 * match_pct + 0.3 * weight + 0.2 * sim, 100), 2)

        return render_template(
            "dashboard.html",
            ats=ats,
            matched=len(r_skills & jd_skills),
            missing=len(jd_skills - r_skills),
            missing_skills=jd_skills - r_skills,
            warning=warning
        )

    return render_template("analyze.html")

import os

if __name__ == "__main__":
    app.run(debug=True, port=5000)
