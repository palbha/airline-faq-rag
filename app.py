import gradio as gr
import openai
from baseline_code import *

# Qatar Airways-style theme
custom_css = """
body {
    background-color: #f5f5dc;
    margin: 0;
    padding: 0;
}

.gradio-container {
    font-family: 'Lato', sans-serif;
    padding: 20px;
}

h1 {
    color: #5c0a0a;
}

textarea, input, .message {
    background-color: #fff8f0 !important;
    color: #333 !important;
    border-radius: 8px !important;
    border: 1px solid #ddd !important;
}

.message.user {
    border-left: 4px solid #5c0a0a;
    padding-left: 8px;
    margin-bottom: 10px;
}

.message.assistant {
    border-left: 4px solid #d4af37;
    padding-left: 8px;
    margin-bottom: 10px;
}

button {
    background-color: #5c0a0a !important;
    color: white !important;
    border-radius: 10px !important;
    padding: 8px 16px;
    border: none;
}

button:hover {
    background-color: #a01010 !important;
}

.gr-chatbot {
    background-color: #fffdf5 !important;
    border: 1px solid #ddd !important;
    border-radius: 10px !important;
    padding: 10px;
    max-height: 400px;
    overflow-y: auto;
}
"""


# Model-specific response logic
def get_response(message, chat_history, model_choice, api_key):
    chat_history.append({'role':"user","content":message})
    reply =generate_answer(message,model_choice,api_key)

    chat_history.append({"role":"assistant","content": reply})
    print("Chat",chat_history)
    return reply,chat_history
# Gradio app
with gr.Blocks() as app:
    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("## ⚙️ Model Configuration")

            model_choice = gr.Dropdown(
                label="Choose Model",
                choices=["OpenAI GPT-4",    "Gemini 1.5Flash",    "Gemini 2.0Flash",    "Together AI"],
                value= "Gemini 1.5Flash"
            )

            api_key_input = gr.Textbox(
                label="Enter API Key",
                placeholder="Enter your OpenAI API key here...",
                type="password"
            )

        with gr.Column(scale=3):
            gr.Markdown("<h1>✈️ AirlineX Airways Virtual Assistant</h1>")
            chatbot = gr.Chatbot(label="Assistant", height=400,type="messages")
            msg = gr.Textbox(label="Your Message")
            state = gr.State([])

    gr.Markdown("🔒 **Note:** Your API key is used only for this session and is not stored or logged.")

    # Main logic handler
    def respond(message, chat_history, model_choice, api_key):
        reply, chat_history = get_response(message, chat_history, model_choice, api_key)
        return chat_history, chat_history

    msg.submit(
        respond,
        [msg, state, model_choice, api_key_input],
        [chatbot, state]
    )

app.launch()
