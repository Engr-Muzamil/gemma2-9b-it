📌 Project Overview

This project is an AI-powered chatbot built using a pre-trained model from GroqCloud.
It leverages LangChain, ChatGroq, and other LangChain utilities to handle conversations effectively.

⚡ Features

Uses GroqCloud pre-trained model for intelligent responses

Integrated with LangChain & ChatGroq

Session-based chat history for smooth interaction

API keys are securely managed using a .env file

Runs inside Jupyter Notebook (.ipynb) for experimentation

🛠️ Tech Stack

Python 🐍

LangChain

ChatGroq

GroqCloud API

dotenv

🚀 How It Works

Store your GroqCloud API key in a .env file

Load the API key inside your notebook

📂 Repository Structure
├── chatbot.ipynb       # Main notebook  
├── .env                # API key storage (not uploaded)  
├── requirements.txt    # Dependencies  
└── README.md           # Project description  

📌 Example Usage
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

model = ChatGroq(model="gemma2-9b-it", groq_api_key=api_key)
response = model.invoke([HumanMessage(content="Hello, chatbot!")])
print(response.content)

🔐 Security

⚠️ Do not share your .env file or API key publicly.

🌟 Future Enhancements

Add a Streamlit UI for interactive chatbot

Deploy on cloud platforms

Support voice-based interaction

Initialize the ChatGroq model via LangChain

Start chatting with your AI assistant 🎉
