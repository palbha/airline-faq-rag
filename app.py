import gradio as gr
import openai
from baseline_code import *



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
            chatbot = gr.Chatbot(label="Assistant", height=700,type="messages")
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
