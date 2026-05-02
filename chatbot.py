import tkinter as tk
from tkinter import scrolledtext, ttk
import re
import datetime

# --- Theme Configuration ---
BG_COLOR = "#1e1e1e"     
FG_COLOR = "#e0e0e0"     
ACCENT_COLOR = "#007acc" 
ENTRY_BG = "#2d2d2d"     

# --- Knowledge Base ---
knowledge_base = {
    "what is syntecxhub": "Syntecxhub is a forward-thinking company that bridges learning with practical experience.",
    "what is ai": "AI stands for Artificial Intelligence, which simulates human intelligence in machines.",
    "internship": "We offer internships in Web Dev, UI/UX, Data Science, and more!",
    "how to apply": "You can visit our website or follow our LinkedIn page to stay updated on openings.",
    "contact": "You can reach us at info@syntecxhub.com."
}

intents = {
    r'hello|hi|hey': "Hello there! How can I help you today?", 
    r'how are you': "I'm functioning perfectly!", 
    r'bye|quit|exit': "Goodbye! Have a great day!"
}

# --- Logging ---
def log_conversation(user_input, bot_response):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("chat_history.log", "a") as log_file:
        log_file.write(f"[{timestamp}] User: {user_input} | Bot: {bot_response}\n")

# --- Logic ---
def get_response(user_input):
    user_input = user_input.lower().strip()
    if user_input in knowledge_base: return knowledge_base[user_input]
    for pattern, response in intents.items():
        if re.search(pattern, user_input): return response
    return "I'm not sure I understand. Could you rephrase?"

def process_message(user_text):
    if not user_text: return
    chat_display.config(state=tk.NORMAL)
    chat_display.insert(tk.END, f"You: {user_text}\n\n", "user")
    response = get_response(user_text)
    chat_display.insert(tk.END, f"Bot: {response}\n\n", "bot")
    chat_display.config(state=tk.DISABLED)
    chat_display.yview(tk.END)
    log_conversation(user_text, response)
    entry.delete(0, tk.END)

# --- GUI Build ---
root = tk.Tk()
root.title("Syntecxhub AI Assistant")
root.configure(bg=BG_COLOR)
root.geometry("450x600")

header = tk.Label(root, text="Syntecxhub Assistant", bg=BG_COLOR, fg=ACCENT_COLOR, font=("Segoe UI", 16, "bold"))
header.pack(pady=10)

chat_display = scrolledtext.ScrolledText(root, width=50, height=20, bg=ENTRY_BG, fg=FG_COLOR, font=("Segoe UI", 10), bd=0, padx=10, pady=10, state=tk.DISABLED)
chat_display.tag_config("user", foreground="#81d4fa", justify="right")
chat_display.tag_config("bot", foreground="#a5d6a7")
chat_display.pack(padx=15, pady=5)

entry = tk.Entry(root, width=40, font=("Segoe UI", 12), bg=ENTRY_BG, fg=FG_COLOR, insertbackground="white", bd=0)
entry.pack(padx=15, pady=10, ipady=5)
entry.bind("<Return>", lambda e: process_message(entry.get()))

btn_frame = tk.Frame(root, bg=BG_COLOR)
btn_frame.pack(pady=5)
for key in list(knowledge_base.keys()): 
    tk.Button(btn_frame, text=key.title(), bg=ACCENT_COLOR, fg="white", bd=0, command=lambda k=key: process_message(k)).pack(side=tk.LEFT, padx=5)

root.mainloop()