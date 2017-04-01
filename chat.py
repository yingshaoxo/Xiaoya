from chatterbot import ChatBot
chatbot = ChatBot('Xiaoya', read_only=True)

# Get a response to an input statement
def main(text):
    return chatbot.get_response(text)
