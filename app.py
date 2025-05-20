import gradio as gr
import openai
from baseline_code import *

# Qatar Airways-style theme
custom_css = """
body { background-color: #f5f5dc; }
.gradio-container { font-family: 'Lato', sans-serif; }
h1 { color: #5c0a0a; }
textarea, .message { background-color: #fff8f0; color: #333; }
.message.user { border-left: 4px solid #5c0a0a; }
.message.bot { border-left: 4px solid #d4af37; }
button { background-color: #5c0a0a; color: white; border-radius: 10px; }
button:hover { background-color: #a01010; }
"""

# Model-specific response logic
def get_response(message, chat_history, model_choice, api_key):
    chat_history.append({'role':"user","content":message})
    reply =generate_answer(message,model_choice,api_key)

    chat_history.append({"role":"assistant","content": reply})
    print("Chat",chat_history)
    return chat_history
# Gradio app
with gr.Blocks(theme=gr.themes.Soft()) as app:
    with gr.Row():
        with gr.Column(scale=4):
            chatbot = gr.Chatbot(label="Airline Assistant", height=400, type="messages")
            message_input = gr.Textbox(placeholder="Ask me something...", label="Your question")
            submit_btn = gr.Button("Send")
        
        with gr.Column(scale=1):
            model_choice = gr.Dropdown(["gpt-4", "gemini-1.5-flash"], label="Choose Model")
            api_key_input = gr.Textbox(placeholder="Enter API Key", label="API Key", type="password")

    chat_history_state = gr.State([])

    submit_btn.click(
        fn=get_response,
        inputs=[message_input, chat_history_state, model_choice, api_key_input],
        outputs=[chatbot, chat_history_state]
    )

    # Main logic handler
    def respond(message, chat_history, model_choice, api_key):
        reply, chat_history = get_response(message, chat_history, model_choice, api_key)
        return chat_history, chat_history


app.launch()
