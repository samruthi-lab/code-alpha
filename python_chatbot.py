
def chatbot_reply(user_input):
   
    user_input = user_input.lower().strip()

    
    if user_input == "hello":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "bye":
        return "Goodbye!"
    else:
        return "I don't understand that."


print("Chatbot: Hello! Type 'bye' to exit.")

while True:
    user_message = input("You: ")  # Get user input
    reply = chatbot_reply(user_message)  # Get chatbot's reply
    print("Chatbot:", reply)  # Show reply

    if user_message.lower().strip() == "bye":  # Exit condition
        break
