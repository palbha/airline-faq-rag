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
    reply =generate_answer(message,model_choice,api_key)

    chat_history.append([message, reply])
    return reply, chat_history
# Gradio app
with gr.Blocks(css=custom_css) as app:
    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("## ⚙️ Model Configuration")
            
            model_choice = gr.Dropdown(
                label="Choose Model",
                choices=["OpenAI GPT-4", "Gemini Pro", "Together AI"],
                value="OpenAI GPT-4"
            )
            
            api_key_input = gr.Textbox(
                label="Enter API Key",
                placeholder="Enter your OpenAI API key here...",
                type="password"
            )

        with gr.Column(scale=3):
            gr.Markdown("<h1>✈️ Qatar Airways Virtual Assistant</h1>")
            chatbot = gr.Chatbot(label="Assistant", height=400,type="messages")
            msg = gr.Textbox(label="Your Message")
            state = gr.State([])

    # Main logic handler
    def respond(message, chat_history, model_choice, api_key):
        reply, chat_history = get_response(message, chat_history, model_choice, api_key)
        return reply, chat_history

    msg.submit(
        respond,
        [msg, state, model_choice, api_key_input],
        [chatbot, state]
    )

app.launch()
