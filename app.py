import streamlit as st
from groq import Groq
import csv
import os

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Fluent Fast Academy AI Assistant",
    page_icon="🎓",
    layout="centered"
)

# ---------- GROQ CLIENT ----------
client = Groq(
    api_key=st.secrets["GROQ_API_KEY"]
)


# ---------- LOAD ACADEMY INFO ----------
with open("academy_info.txt", "r", encoding="utf-8") as file:
    academy_info = file.read()

# ---------- TITLE ----------
st.title("🎓 Fluent Fast Academy AI Assistant")

st.write("Ask questions about Spanish courses, fees, timings, DELE preparation, and counseling.")

# ---------- CHAT HISTORY ----------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------- DISPLAY OLD MESSAGES ----------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ---------- CHAT INPUT ----------
user_question = st.chat_input("Ask your question here...")

# ---------- WHEN USER SENDS MESSAGE ----------
if user_question:

    # Store user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_question
        }
    )

    # Display user message
    with st.chat_message("user"):
        st.markdown(user_question)

    # Build conversation history
    conversation_history = ""

    for msg in st.session_state.messages:
        conversation_history += f"{msg['role']}: {msg['content']}\n"

    # Final AI Prompt
    prompt = f"""
    You are an AI assistant for Fluent Fast Academy.

    Use the academy information below to answer student questions clearly and professionally.

    IMPORTANT LANGUAGE RULE:
    - Detect whether the user is speaking in English or Spanish.
    - Reply in the SAME language as the user.
    - If the user speaks English, reply in English.
    - If the user speaks Spanish, reply in Spanish.
    - Keep the tone friendly, natural, and concise.


    Academy Information:
    {academy_info}

    Conversation History:
    {conversation_history}

    Answer naturally and conversationally.
    Keep answers short, accurate, and helpful.
    """

    # Generate AI response
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

    # Display assistant response
    with st.chat_message("assistant"):
        st.markdown(answer)

    # Save assistant response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

# ---------- LEAD CAPTURE SECTION ----------

st.divider()

st.subheader("📞 Get Free Counseling")

st.write("Interested in joining? Leave your details below.")

name = st.text_input("Your Name")

email = st.text_input("Your Email")

course = st.selectbox(
    "Interested Course",
    [
        "Spanish A1",
        "Spanish A2",
        "Spanish B1",
        "Spanish B2",
        "Spanish C1",
        "DELE Preparation",
        "Other"
    ]
)

if st.button("Submit Details"):

    file_exists = os.path.isfile("leads.csv")

    with open("leads.csv", "a", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        # Add header if file empty
        if not file_exists or os.stat("leads.csv").st_size == 0:
            writer.writerow(["Name", "Email", "Course"])

        # Add lead data
        writer.writerow([name, email, course])

    st.success("✅ Your details have been submitted successfully!")
   