# 🚀 CV-Intelligence

An AI-powered Resume Intelligence Platform built with FastAPI, Supabase, and Groq LLM.

## ✨ Features

- 🔐 User Authentication (Supabase Auth)
- 🛡️ JWT Authorization
- 📄 Resume Upload (PDF & DOCX)
- 📑 Resume Parsing
- 👁️ OCR Support
- 📊 ATS Score Analysis
- 🤖 AI Resume Analysis
- 🎯 AI Job Matching
- ✨ AI Resume Improvement
- 📜 Resume History
- 🗑️ Resume Management
- 📚 Interactive Swagger API Documentation

---

## 🛠️ Tech Stack

### Backend
- FastAPI
- Python
- Supabase
- PostgreSQL
- Groq LLM

### AI
- Llama 3.3 70B
- Prompt Engineering

### Libraries
- Pydantic
- Uvicorn
- PyMuPDF
- python-docx
- pytesseract

---

## 📂 Project Structure

```
backend/
│
├── app/
│   ├── api/
│   ├── core/
│   ├── dependencies/
│   ├── schemas/
│   ├── services/
│   └── utils/
│
├── requirements.txt
├── .env.example
└── README.md
```

---

## 🚀 Running the Project

```bash
git clone https://github.com/anshujha2304-afk/CV-Intelligence.git

cd CV-Intelligence/backend

python -m venv venv

source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
uvicorn app.main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

## 📌 Future Improvements

- React Frontend
- Docker
- Deployment
- Resume PDF Export
- Dashboard Analytics
- Dark Mode
- Admin Panel

---

## 👨‍💻 Author

**Divyanshu Jha**

Built with ❤️ using FastAPI & AI.