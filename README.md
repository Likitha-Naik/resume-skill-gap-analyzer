# 📄 Resume Skill Gap Analyzer

A **Flask-based web application** that analyzes a user's resume against a target job role and identifies **skill gaps**, **matching skills**, and **recommendations for upskilling**. This project is ideal for students and freshers preparing for technical roles and interviews.

---

## 🚀 Project Overview

The **Resume Skill Gap Analyzer** helps users:

* Upload or input resume content
* Select or define a target job role
* Compare resume skills with required job skills
* Identify missing skills (skill gaps)
* Get actionable recommendations for improvement

This project demonstrates practical usage of **Python, Flask, NLP (spaCy), databases, and frontend integration**.

---

## 🛠️ Technologies Used

### Backend

* **Python 3.10+**
* **Flask** – Web framework
* **spaCy** – Natural Language Processing
* **SQLite** – Database

### Frontend

* **HTML5**
* **CSS3**
* **Jinja2 Templates**

### Tools & Libraries

* `pandas`
* `sqlite3`
* `werkzeug`

---

## 📁 Project Structure

```text
resume_skill_gap_analyzer/
│
├── app.py                 # Main Flask application
├── database.db            # SQLite database
├── skills.csv             # Job role & skill mapping dataset
├── requirements.txt       # Python dependencies
│
├── templates/
│   ├── login.html         # User login page
│   ├── register.html      # User registration page
│   ├── dashboard.html     # User dashboard
│   └── analyze.html       # Skill analysis results
│
└── static/
    └── style.css          # Styling file
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/resume_skill_gap_analyzer.git
cd resume_skill_gap_analyzer
```

### 2️⃣ Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Install spaCy Language Model

```bash
python -m spacy download en_core_web_sm
```

### 4️⃣ Run the Application

```bash
python app.py
```

### 5️⃣ Open in Browser

```
http://127.0.0.1:5000/
```

## 🔐 Application Features

### 👤 User Authentication

* User registration
* Secure login system
* Session-based authentication

### 📊 Skill Gap Analysis

* Resume text processing using NLP
* Skill extraction from resume
* Comparison with job-specific skills
* Identification of:

  * Matching skills
  * Missing skills
  * Skill gap percentage

### 📈 Dashboard

* Displays analyzed results
* Easy-to-understand skill insights
* Helps users focus on improvement areas


## 📄 skills.csv Format

Example structure:

```csv
JobRole,Skills
Data Scientist,Python;Machine Learning;SQL;Statistics
Web Developer,HTML;CSS;JavaScript;Flask
Cloud Engineer,AWS;Linux;Docker;Networking
```

## 🧠 How Skill Analysis Works

1. User inputs resume text
2. NLP extracts keywords and skills
3. Selected job role skills are fetched from CSV
4. Resume skills are compared with job skills
5. Missing skills are identified as **skill gaps**


## ✅ Use Cases

* Students preparing for placements
* Freshers identifying skill gaps
* Resume self-evaluation
* Career guidance projects


## ⚠️ Limitations

* Skill extraction depends on keyword matching
* Resume upload as PDF/DOCX not included (text-based input only)
* No live job portal integration


## 🔮 Future Enhancements

* Resume upload (PDF/DOCX)
* ML-based skill weighting
* Job description scraping
* Personalized learning roadmap
* Admin panel for skill management
* Deployment on cloud (AWS / Render)


## 📜 License

This project is developed for **educational and academic purposes**. Free to use and modify.


## ⭐ Acknowledgements

* Python & Flask community
* spaCy NLP library
* Open-source contributors

