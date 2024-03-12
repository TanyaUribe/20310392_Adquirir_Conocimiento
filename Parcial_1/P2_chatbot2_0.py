class ModuloAdquisicionConocimiento:
    def __init__(self):
        self.base_conocimiento = {}

    def agregar_conocimiento(self, pregunta, respuesta):
        self.base_conocimiento[pregunta.lower()] = respuesta

    def buscar_respuesta(self, pregunta):
        pregunta = pregunta.lower()
        return self.base_conocimiento.get(pregunta, "Lo siento, no tengo información sobre eso.")

class ChatSencillo:
    def __init__(self):
        self.adquisicion_conocimiento = ModuloAdquisicionConocimiento()

    def cargar_conocimiento_inicial(self):
        conocimiento_inicial = {
            "hola": "¡Hola! ¿Cómo te va?",
            "como estas": "Estoy bien, gracias. ¿Y tú?",
            "bien": "Me alegro.",
            "dime un dato curioso": "En francés, la palabra papa o patata es traducida como -pomme de terre, que traducido de manera literal al español, sería manzana de tierra, o terrestre.",
            "de que podemos hablar": "Puedo hablar sobre varios temas. ¿Hay algo en particular que te interese?"
        }
        for pregunta, respuesta in conocimiento_inicial.items():
            self.adquisicion_conocimiento.agregar_conocimiento(pregunta, respuesta)

    def iniciar_conversacion(self):
        print("... ¿Hay alguien ahí?")
        while True:
            input_usuario = input("Usuario: ")
            if input_usuario.lower() == "salir":
                print("¡Hasta luego!")
                break
            respuesta_chat = self.adquisicion_conocimiento.buscar_respuesta(input_usuario)
            if "Lo siento" in respuesta_chat:  # Si el bot no tiene información
                print("Bot:", respuesta_chat)
                respuesta_usuario = input("Bot: ¿Cuál es tu respuesta a esa pregunta? ")
                self.adquisicion_conocimiento.agregar_conocimiento(input_usuario, respuesta_usuario)
                print("Bot: ¡Gracias por enseñarme sobre más temas!")
            else:
                print("Bot:", respuesta_chat)

# Crear una instancia del chat sencillo
chat = ChatSencillo()

# Cargar conocimiento inicial
chat.cargar_conocimiento_inicial()

# Iniciar la conversación
chat.iniciar_conversacion()

