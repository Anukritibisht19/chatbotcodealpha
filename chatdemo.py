
import nltk
from nltk.chat.util import Chat, reflections


pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello!", "Hi there!", "Greetings!","hey! How can i help you ?",]
    ],
    [
        r"how are you",
        ["I'm just a program, but thanks for asking!", "Doing well, how about you?",]
    ],
    [
        r"what is your name",
        ["I am a chatbot created to assist you.","I am a chatbox you can call me leo",]
    ],
    [   r"what is your age",
        ["I am a new born chatbot"," I am age less","I am just a code",]
    ],
    [
        r"quit",
        ["Bye! Take care.", "Goodbye! Have a great day!","It was nice talking to you",]
    ],
    [
        r"(.*)",
        ["I'm sorry, I didn't understand that.", "Could you please rephrase it","sorry ","ask any other thing",]
    ]
]
chatbot = Chat(pairs, reflections)


def start_chat():
  
    print("Hello! I am a chatbot. Type 'quit' to exit.")
    chatbot.converse()

if __name__ == "__main__":
    start_chat()

