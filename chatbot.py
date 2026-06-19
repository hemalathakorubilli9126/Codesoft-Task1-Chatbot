print("Welcome to the Simple Chatbot!")

while True:
    user = input("You: ").lower()

    if user == "hi" or user == "hello":
        print("Bot: Hello! How can I help you?")
    elif user == "how are you":
        print("Bot: I am fine. Thank you!")
    elif user == "what is your name":
        print("Bot: I am a rule-based chatbot.")
    elif user == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break
    else:
        print("Bot: Sorry, I don't understand that.")