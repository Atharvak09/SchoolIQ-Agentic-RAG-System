from chatbot import chatbot

while True:
    question = input("\nAsk a question (or type exit): ")
    if question.lower() == "exit":
        break

    answer = chatbot(question)
    print("\n🤖 Answer:\n", answer)
