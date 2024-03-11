from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot('Peach2.0')

trainer = ListTrainer(chatbot)

trainer.train([
    "Hola. ¿En qué puedo ayudarte el día de hoy?",
    "¡Claro! Recuerda comprar un llavero de recuerdo.",
    "Puedo mostrarte vuelos de avión en tu ciudad. ¿Te parece bien?"
])

# Get a response to the input text 'I would like to book a flight.'
response = chatbot.get_response('quiero ir a la playa')
response = chatbot.get_response('si')

print(response)
