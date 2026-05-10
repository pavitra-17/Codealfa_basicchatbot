def chatbot():

    print("🤖 Simple Chatbot")
    print("Type 'bye' to exit.\n")

    while True:

        user_input = input("You: ").lower()

        if user_input == "hello":
            print("Bot: Hi! Nice to meet you.")

        elif user_input == "how are you":
            print("Bot: I am fine, thanks!")

        elif user_input == "what is your name":
            print("Bot: I am a Python chatbot.")

        elif user_input == "help":
            print("Bot: You can say hello, ask my name, or say bye.")

        elif user_input == "bye":
            print("Bot: Goodbye!")
            break

        else:
            print("Bot: Sorry, I don't understand that.")

chatbot()
