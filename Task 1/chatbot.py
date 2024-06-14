def chatbot_response(user_input):
    
    user_input = user_input.lower()

    
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm doing great! How about you?"
    elif "your name" in user_input:
        return "I'm ChatBot, your virtual assistant."
    elif "help" in user_input:
        return "Sure, I am here to help! What do you need assistance with?"
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I don't understand that. Can you please rephrase?"


def main():
    print("ChatBot: Hi there! I'm your virtual assistant. Type 'bye' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "goodbye"]:
            print("ChatBot: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input)
        print("ChatBot:", response)

if __name__ == "__main__":
    main()

