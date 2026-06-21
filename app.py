from utils.translator import translate_text
import streamlit as st
import os

from utils.pdf_loader import load_pdf
from utils.text_splitter import split_text
from utils.vector_store import create_vectorstore
from agents.answer_agent import generate_answer

# =========================
# TRANSLATIONS
# =========================

translations = {
    "English": {
        "title": "📚 BookMind RAG Chatbot",
        "upload": "Upload a PDF",
        "process": "Process PDF",
        "question": "Ask a question from the uploaded PDF",
        "answer": "Answer",
        "success": "✅ PDF uploaded successfully!",
        "processed": "✅ PDF processed successfully!",
        "provider": "Choose AI Provider",
        "apikey": "Gemini API Key",
        "ui_language": "UI Language",
        "answer_language": "Answer Language",
        "generate": "Get Answer",
        "processing": "Processing PDF...",
        "generating": "Generating answer...",
        "preview": "PDF Preview",
        "api_error": "Please enter your Gemini API Key.",
        "ask_warning": "Please enter a question",
    },
    "Telugu": {
        "title": "📚 బుక్‌మైండ్ RAG చాట్‌బాట్",
        "upload": "PDF అప్లోడ్ చేయండి",
        "process": "PDF ప్రాసెస్ చేయండి",
        "question": "PDF నుండి ప్రశ్న అడగండి",
        "answer": "సమాధానం",
        "success": "✅ PDF విజయవంతంగా అప్లోడ్ చేయబడింది!",
        "processed": "✅ PDF విజయవంతంగా ప్రాసెస్ చేయబడింది!",
        "provider": "AI ప్రొవైడర్ ఎంచుకోండి",
        "apikey": "జెమిని API కీ",
        "ui_language": "UI భాష",
        "answer_language": "సమాధాన భాష",
        "generate": "సమాధానం పొందండి",
        "processing": "PDF ప్రాసెస్ అవుతోంది...",
        "generating": "సమాధానం రూపొందుతోంది...",
        "preview": "PDF ప్రివ్యూ",
        "api_error": "దయచేసి మీ Gemini API కీని నమోదు చేయండి.",
        "ask_warning": "దయచేసి ప్రశ్నను నమోదు చేయండి",
    },
    "Hindi": {
        "title": "📚 बुकमाइंड RAG चैटबॉट",
        "upload": "PDF अपलोड करें",
        "process": "PDF प्रोसेस करें",
        "question": "PDF से प्रश्न पूछें",
        "answer": "उत्तर",
        "success": "✅ PDF सफलतापूर्वक अपलोड हो गई!",
        "processed": "✅ PDF सफलतापूर्वक प्रोसेस हो गई!",
        "provider": "AI प्रदाता चुनें",
        "apikey": "Gemini API Key",
        "ui_language": "UI भाषा",
        "answer_language": "उत्तर भाषा",
        "generate": "उत्तर प्राप्त करें",
        "processing": "PDF प्रोसेस हो रही है...",
        "generating": "उत्तर बनाया जा रहा है...",
        "preview": "PDF पूर्वावलोकन",
        "api_error": "कृपया अपना Gemini API Key दर्ज करें।",
        "ask_warning": "कृपया प्रश्न दर्ज करें",
    },
}


# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="BookMind RAG",
    page_icon="📚",
    layout="wide",
)


# =========================
# UI LANGUAGE
# =========================

ui_language = st.sidebar.selectbox(
    "UI Language",
    ["English", "Telugu", "Hindi"],
)

t = translations[ui_language]


# =========================
# TITLE
# =========================

st.title(t["title"])


# =========================
# AI SETTINGS
# =========================

st.sidebar.title("🤖 AI Settings")

provider = st.sidebar.radio(
    t["provider"],
    ["Ollama", "Gemini"],
)

gemini_api_key = ""

if provider == "Gemini":
    gemini_api_key = st.sidebar.text_input(
        t["apikey"],
        type="password",
        help="Paste your Gemini API Key here",
    )


# =========================
# PDF UPLOAD
# =========================

uploaded_file = st.file_uploader(
    t["upload"],
    type=["pdf"],
)

if uploaded_file is not None:

    os.makedirs("uploads", exist_ok=True)

    file_path = os.path.join(
        "uploads",
        uploaded_file.name,
    )

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success(t["success"])

    if st.button(t["process"]):

        with st.spinner(t["processing"]):

            text = load_pdf(file_path)

            st.write(f"### {t['preview']}")
            st.write(text[:2000])

            chunks = split_text(text)
            create_vectorstore(chunks)

        st.success(t["processed"])


# =========================
# ANSWER LANGUAGE
# =========================

language = st.selectbox(
    t["answer_language"],
    ["English", "Telugu", "Hindi"],
)


# =========================
# QUESTION INPUT
# =========================

question = st.text_input(t["question"])


# =========================
# GENERATE ANSWER
# =========================

if st.button(t["generate"]):

    if not question:
        st.warning(t["ask_warning"])
        st.stop()

    if provider == "Gemini" and not gemini_api_key:
        st.error(t["api_error"])
        st.stop()

    with st.spinner(t["generating"]):

        english_question = translate_text(question, "en")

        answer = generate_answer(
            english_question,
            provider,
            gemini_api_key,
        )

        if language == "Telugu":
            answer = translate_text(answer, "te")

        elif language == "Hindi":
            answer = translate_text(answer, "hi")

    st.subheader(t["answer"])
    st.write(answer)
