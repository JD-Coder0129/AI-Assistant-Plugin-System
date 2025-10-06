import random
from abc import ABC, abstractmethod


class AIAssistantPlugin(ABC):
    @abstractmethod
    def respond(self, query: str) -> str:
        pass

class WeatherPlugin(AIAssistantPlugin):
    def respond(self, query: str) -> str:
        if "weather" in query.lower():
            temp = random.randint(20, 35)
            return f"The temperature is {temp} degrees Celsius"
        return "Weather module can only handle weather queries"
    

class JokesPlugin(AIAssistantPlugin):
    def respond(self, query: str) -> str:
        joke = [
            "Why did the AI cross the road? To optimize the chicken.",
            "Why did the computer show up late? It had a hard drive!",
            "I told my AI a joke — now it’s training a humor model.",
            "Python programmers wear glasses because they can’t C."
        ]
        if "joke" in query.lower():
            return random.choice(joke)
        return "Jokes module can only handle joke queries"
    
class NewsPlugin(AIAssistantPlugin):
    def respond(self, query: str) -> str:
        headlines = [
            "AI beats humans in logic puzzles again!",
            "New Python update brings performance boost.",
            "Scientists teach robots to write poetry — results are mixed."
        ]
        if "news" in query.lower():
            return f"Today's news: {random.choice(headlines)}"
        return "News module can only handle news queries"
    
class Jarvis:
    def __init__(self):
        self.plugins = [WeatherPlugin(), JokesPlugin(), NewsPlugin()]
    
    def respond(self, query: str) -> str:
        for plugin in self.plugins:
            response = plugin.respond(query)
            if response:
                return response
        return None
    
    def add_plugin(self, plugin: AIAssistantPlugin):
        self.plugins.append(plugin)

    def handle_query(self, query: str):
        print(f"User: {query}")
        response = self.respond(query)
        print(f"Jarvis: {response}")
        
def interactive_loop():
    jarvis = Jarvis()
    while True:
        query = input("User: ")
        if "thank you" in query.lower():
            print("Jarvis: You're welcome!")
            break
        else:
            jarvis.handle_query(query)

if __name__ == "__main__":
    interactive_loop()

# if __name__ == "__main__":
#     jarvis = Jarvis()
#     jarvis.handle_query("What's the weather like today?")
#     jarvis.handle_query("Tell me a joke")
#     jarvis.handle_query("What's the latest news?")
#     jarvis.handle_query("Can you do something else?")