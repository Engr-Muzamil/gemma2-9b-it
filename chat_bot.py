import streamlit as st
import os
from langchain_groq import ChatGroq # groq llm integration
from langchain.memory import ConversationBufferMemory # memory backend for chat
from langchain.chains import ConversationChain # it wires LLM + memory

# load api key

load_dotenv() # read .env file

os.environ["Groq_api_key"] = os.getenv("Groq_api_key")

## Streamlit
st.set_page_config(page_title=" 💬 Conversational Chatbot") # title in browser tab 

st.title("💬 Conversational Chatbot with Message History") # app header

# sidebar control

model_name = st.sidebar.selectbox( 
    "Select Groq Model",
    ["gemma2-9b-it","deepseek-r1-distill-llama-70b","openai/gpt-oss-120b"]
    )

temperature = st.sidebar.slider( # fix the randomness of the response
    "Temperture",0.0,1.0,0.7
)

max_tokens = st.sidebar.slider( # max response length
    "Max Tokens", 50,300,150
)

if "memory" not in st.session_state:
    # perssist memory across reruns
    st.session_state.memory = ConversationBufferMemory(
        return_messages=True # return as list of memory, not in one big string.
    )

if "history" not in st.session_state:
    st.session_state.history=[]

# user input

user_input = st.chat_input("You: ") # clears itself on enter

if user_input:
    st.session_state.history.append(("user", user_input))

    # initialized a fresh llm for this turn
    llm= ChatGroq(
        model_name=model_name,
        temperature= temperature,
        max_tokens= max_tokens
    )

    # build conversation chain in our memory
    conv =  ConversationChain(
        llm=llm,
        memory= st.session_state.memory,
        verbose= True
    )

    ## get ai response ( memory is updted internally)
    ai_response = conv.predict(input=user_input)

    # append assitant to history
    st.session_state.history.append(("assistant",ai_response))

# render  chat bubble
for role, text in st.session_state.history:
    if role == "user":
        st.chat_message("user").write(text) # user style
    else:
        st.chat_message("assistant").write(text) # assistant style






