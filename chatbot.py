print("🤖 Sam: Hello! My name is Sam.")

while True:
    user_input=input("You: ").lower().strip()
    #exit commands
    if user_input in["bye","goodby","exit","quite"]:
        print("Sam: Goodbye, friend! Have a great day.🖐️")
        break

    #Greetings
    elif user_input in["hello","hii","hey","good morning","good afternoon","good evening"]:
        print("Sam: Hello! Nice to meet you.😊 ")

    # Asking how the bot is doing 
    elif "how" in user_input.split():
        print("Sam: I'm doing greate! Thanks for asking.")

    # Asking the bot name
    elif "your name" in user_input:
        print("Sam: My name is chatbot")

     # Asking what the bot can do
    elif "help" in user_input:
        print("Sam: I can respond to greetings and simple questions.")

    # Asking the what is python
    elif user_input in["what is python"]:
        print(" Sam: Python is a beginner-friendly programming language.")

     # Unknown input
    else:
        print("Sam: I don't understand that yet. Try another question.")
