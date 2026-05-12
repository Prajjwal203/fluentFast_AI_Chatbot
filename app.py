import streamlit as st
from groq import Groq

# ---------- GROQ CLIENT ----------
client = Groq(
    api_key=st.secrets["GROQ_API_KEY"]
)

# ---------- LOAD ACADEMY INFO ----------
with open("academy_info.txt", "r", encoding="utf-8") as file:
    academy_info = file.read()

# ---------- PAGE TITLE ----------
st.title("Fluent Fast Academy AI Assistant")

st.write("Ask questions about courses, timings, and counseling.")

# ---------- USER INPUT ----------
user_question = st.text_input("Ask your question:")

# ---------- RESPONSE ----------
if user_question:

    prompt = f"""
    You are an AI assistant for Fluent Fast Academy.

    Use the academy information below to answer student questions clearly and professionally.

    Academy Information:
    {academy_info}

    User Question:
    {user_question}

    Give short, accurate, friendly answers.
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    answer = response.choices[0].message.content

    st.write("### Answer")
    st.write(answer)