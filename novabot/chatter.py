from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create chatbot instance
chatbot = ChatBot("NovaBot")

# Train with English corpus
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

def get_chitchat_response(user_input):
    response = chatbot.get_response(user_input)
    return str(response)
