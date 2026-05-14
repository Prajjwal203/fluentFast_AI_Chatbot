import streamlit as st
from groq import Groq
import csv
import os
from pypdf import PdfReader

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
# with open("academy_info.txt", "r", encoding="utf-8") as file:
#     academy_info = file.read()

# ---------- PDF UPLOAD ----------

uploaded_file = st.sidebar.file_uploader(
    "📄 Upload Academy Brochure PDF",
    type="pdf"
)

academy_info = ""

if uploaded_file is not None:

    pdf_reader = PdfReader(uploaded_file)

    for page in pdf_reader.pages:
        academy_info += page.extract_text()
        
    st.sidebar.success("📘 PDF Uploaded Successfully")

else:

    academy_info = """
    Fluent Fast Academy offers Spanish language courses,
    DELE preparation, online and offline classes,
    certification, and counseling support.
    """

# if uploaded_file:
#     st.sidebar.success("📘 PDF Uploaded Successfully")


# ---------- TITLE ----------
# st.title("🎓 Fluent Fast Academy AI Assistant")

# st.write("Ask questions about Spanish courses, fees, timings, DELE preparation, and counseling.")

# ---------- HEADER ----------
st.title("🎓 Fluent Fast Academy AI Assistant")

st.markdown("""
Your bilingual AI assistant for Spanish courses, DELE preparation, fees, timings, and counseling.
""")
st.markdown("""
### 🇪🇸 Learn Spanish With Confidence

Ask questions about:
- Courses
- Fees
- Timings
- DELE Preparation
- Online Classes
- Certifications
""")

# ---------- SIDEBAR ----------
with st.sidebar:

    st.success("✅ AI Assistant Ready") # line added here
    st.header("📚 About Academy")

    st.write("""
    Fluent Fast Academy offers:
    - Spanish courses A1 to C2
    - Online & Offline classes
    - DELE preparation
    - Flexible batches
    - Certification after each level
    """)

    st.divider()

    st.subheader("📞 Contact")

    st.write("🌐 www.fluentfastacademy.com")
    st.write("📱 +91-7834806482")

    st.divider()

    st.subheader("💡 Try Asking")

    st.write("""
    - What are the B1 fees?
    - Do you provide online classes?
    - ¿Ofrecen preparación DELE?
    """)



# ---------- CHAT HISTORY ----------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------- DISPLAY OLD MESSAGES ----------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ---------- CHAT INPUT ----------
# user_question = st.chat_input("Ask your question here...")

# ---------- QUICK QUESTION BUTTONS ----------

st.subheader("⚡ Quick Questions")

col1, col2, col3 = st.columns(3)

quick_question = None

with col1:
    if st.button("💰 Course Fees"):
        quick_question = "What are the fees for Spanish courses?"

with col2:
    if st.button("🖥 Online Classes"):
        quick_question = "Do you provide online classes?"

with col3:
    if st.button("📘 DELE Prep"):
        quick_question = "Do you provide DELE preparation?"

# ---------- CHAT INPUT ----------
user_question = st.chat_input("Ask your question here...")

# Use button question if clicked
if quick_question:
    user_question = quick_question



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
   