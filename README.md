# 🎓 Fluent Fast Academy AI Assistant

An AI-powered multilingual chatbot built for educational and coaching businesses.

This project allows users to:
- Ask questions about courses, fees, timings, certifications, and counseling
- Upload PDF brochures for dynamic AI knowledge
- Chat conversationally with memory
- Interact in English or Spanish
- Submit lead information directly into Google Sheets

Built using Python, Streamlit, Groq LLM APIs, and Google Sheets integration.

---

# 🚀 Features

## 🤖 AI Conversational Chatbot
- Natural conversational responses
- Context-aware conversations
- Chat history support

## 🌍 Bilingual Support
- Detects English and Spanish automatically
- Replies in the same language as the user

## 📄 PDF Knowledge Upload
- Upload academy brochures or PDFs
- AI extracts and uses document content dynamically

## 📞 Lead Capture System
Users can submit:
- Name
- Email
- Interested Course

## ☁️ Google Sheets Integration
Leads are automatically stored in Google Sheets using Google Cloud APIs.

## 🎨 Improved User Interface
- Sidebar navigation
- Quick question buttons
- Professional chat layout
- Chat bubbles and assistant roles

---

# 🛠 Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend Logic |
| Streamlit | Frontend UI |
| Groq API | LLM Inference |
| Llama 3.3 70B | AI Model |
| pypdf | PDF Text Extraction |
| Google Sheets API | Lead Storage |
| gspread | Google Sheets Integration |
| OAuth2 Service Account | Authentication |

---

# 📂 Project Structure

```bash
fluentfast-ai-chatbot/
│
├── .streamlit/
├── .gitignore
├── academy_info.txt
├── app.py
├── requirements.txt
├── service_account.json   # ignored in git
├── leads.csv              # ignored in git
└── README.md
```

---

# ⚙️ Setup Instructions

## 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/fluentfast-ai-chatbot.git
```

## 2. Install Requirements

```bash
pip install -r requirements.txt
```

## 3. Add Secrets

Create:

```bash
.streamlit/secrets.toml
```

Add:

```toml
GROQ_API_KEY = "your_api_key_here"
```

---

# 🔑 Google Sheets Setup

1. Create Google Cloud Project
2. Enable:
   - Google Sheets API
   - Google Drive API
3. Create Service Account
4. Download JSON credentials
5. Rename file to:

```bash
service_account.json
```

6. Share Google Sheet with service account email

---

# ▶️ Run Application

```bash
streamlit run app.py
```

OR

```bash
py -m streamlit run app.py
```

---

# 📈 Future Improvements

- WhatsApp integration
- Voice assistant support
- Admin dashboard
- Database integration
- Multi-business onboarding
- Authentication system
- RAG/vector database integration
- Deployment on Streamlit Cloud

---

# 💡 Project Goal

This project was built as an AI automation portfolio project focused on:
- educational businesses
- multilingual AI assistants
- lead automation
- document-based AI systems

---

# 👨‍💻 Author

Prajjwal 

Built while learning practical AI automation engineering using real-world integrations and LLM workflows.
