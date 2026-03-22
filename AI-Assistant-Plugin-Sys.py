import random
from abc import ABC, abstractmethod

# Try to import colorama for cross-platform terminal colors.
# If it's not available, provide no-op fallbacks so the script still runs.
try:
    from colorama import init, Fore, Style
    init(autoreset=True)
except Exception:
    class _NoColor:
        pass
    Fore = _NoColor()
    Style = _NoColor()
    for name in ("RED", "GREEN", "YELLOW", "BLUE", "MAGENTA", "CYAN", "WHITE"):
        setattr(Fore, name, "")
    Style.RESET_ALL = ""

class AIAssistantPlugin(ABC):
    @abstractmethod
    def respond(self, query: str) -> str:
        pass

class WeatherPlugin(AIAssistantPlugin):
    def respond(self, query: str) -> str:
        if "weather" in query.lower():
            temp = random.randint(20, 35)
            return f"{Fore.CYAN}The temperature is {temp} degrees Celsius{Style.RESET_ALL}"
        elif "only" in query.lower():
            return f"{Fore.CYAN}Weather module can only handle weather queries{Style.RESET_ALL}"
        else:
            return None

class JokesPlugin(AIAssistantPlugin):
    def respond(self, query: str) -> str:
        joke = [
            "Why did the AI cross the road? To optimize the chicken.",
            "Why did the computer show up late? It had a hard drive!",
            "I told my AI a joke — now it’s training a humor model.",
            "Python programmers wear glasses because they can’t C."
        ]

        if "joke" in query.lower():
            return f"{Fore.YELLOW}{random.choice(joke)}{Style.RESET_ALL}"
        elif "only" in query.lower():
            return f"{Fore.YELLOW}Jokes module can only handle joke queries{Style.RESET_ALL}"
        else:
            return None

class NewsPlugin(AIAssistantPlugin):
    def respond(self, query: str) -> str:
        headlines = [
            "AI beats humans in logic puzzles again!",
            "New Python update brings performance boost.",
            "Scientists teach robots to write poetry — results are mixed."
        ]

        if "news" in query.lower():
            return f"{Fore.MAGENTA}Today's news: {random.choice(headlines)}{Style.RESET_ALL}"
        elif "only" in query.lower():
            return f"{Fore.MAGENTA}News module can only handle news queries{Style.RESET_ALL}"
        else:
            return None

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
        response = self.respond(query)
        if response:
            print(f"{Fore.GREEN}Jarvis:{Style.RESET_ALL} {response}")
        else:
            print(f"{Fore.RED}Jarvis:{Style.RESET_ALL} I don't understand that query.")

def interactive_loop():
    jarvis = Jarvis()
    while True:
        # Color the user prompt
        query = input(f"{Fore.BLUE}User: {Style.RESET_ALL}")
        if "thank you" in query.lower():
            print(f"{Fore.GREEN}Jarvis:{Style.RESET_ALL} You're welcome!")
            break
        else:
            jarvis.handle_query(query)

if __name__ == "__main__":
    interactive_loop()
