import datetime
import re

# 1. Knowledge Base
knowledge_base = {
    "what is syntecxhub": "Syntecxhub is a forward-thinking company that bridges learning with practical experience.",
    "what is ai": "AI stands for Artificial Intelligence.",
}

intents = {
    r'hello|hi': "Hello! How can I help you?",
    r'bye|exit': "Goodbye!"
}

# 2. Logging Functionality
def log_conversation(user_input, bot_response):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("chat_history.log", "a") as log_file:
        log_file.write(f"[{timestamp}] User: {user_input} | Bot: {bot_response}\n")

# 3. Console Interaction
def main():
    print("--- Syntecxhub Console Chatbot ---")
    print("Type 'exit' to quit.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Bot: Goodbye!")
            log_conversation(user_input, "Goodbye!")
            break
            
        # Basic matching logic
        response = "I'm not sure."
        if user_input.lower() in knowledge_base:
            response = knowledge_base[user_input.lower()]
        else:
            for pattern, r in intents.items():
                if re.search(pattern, user_input.lower()):
                    response = r
        
        print(f"Bot: {response}")
        log_conversation(user_input, response)

if __name__ == "__main__":
    main()