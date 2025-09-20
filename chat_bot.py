import streamlit as st
import os
from dotenv import load_dotenv   # ✅ added
from langchain_groq import ChatGroq
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

# load api key
load_dotenv()
# ✅ use correct casing
groq_api_key = os.getenv("GROQ_API_KEY")

## Streamlit
st.set_page_config(page_title=" 💬 Conversational Chatbot")
st.title("💬 Conversational Chatbot with Message History")

# sidebar
model_name = st.sidebar.selectbox(
    "Select Groq Model",
    ["gemma2-9b-it","deepseek-r1-distill-llama-70b","openai/gpt-oss-120b"]
)

temperature = st.sidebar.slider("Temperature",0.0,1.0,0.7)
max_tokens = st.sidebar.slider("Max Tokens", 50,300,150)

if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory(return_messages=True)

if "history" not in st.session_state:
    st.session_state.history=[]

# user input
user_input = st.chat_input("You: ")

if user_input:
    st.session_state.history.append(("user", user_input))

    llm = ChatGroq(
        model_name=model_name,
        temperature=temperature,
        max_tokens=max_tokens,
        api_key=groq_api_key   # ✅ pass api key
    )

    conv = ConversationChain(llm=llm, memory=st.session_state.memory, verbose=True)
    ai_response = conv.predict(input=user_input)

    st.session_state.history.append(("assistant", ai_response))

# render chat bubble
for role, text in st.session_state.history:
    if role == "user":
        st.chat_message("user").write(text)
    else:
        st.chat_message("assistant").write(text)
