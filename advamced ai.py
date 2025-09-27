import colorama
from colorama import Fore,Style
from textblob import TextBlob

colorama.init()

print(f"{Fore.CYAN}⭐Welcome to Sentiment Spy⭐{Style.RESET_ALL}")
user_name=input(f"{Fore.MAGENTA}Enter your Name:{Style.RESET_ALL}").strip()or "Friendly Agent"
print(f"{Fore.CYAN}Hello Agent{user_name}!Type "exit" to quit 'reset'to clear or 'history' to view chats")
history=[]

while True:
    text=input(f"{Fore.Green}You:{Style.RESET_ALL}").strip()
    if not text:
        print(f"{Fore.RED}Please entervalid text or command {Style.RESET_ALL}")
        continue
    if text.lower()=="exit":
        print(f"{Fore.BLUE}Exciting...Goodbye agent{user_name}")
        {user_name}
        {Style.RESET_ALL}

        break

    if text.lower()=="reset":
       history.clear()
       print(f"{Fore.CYAN}Conversation history cleared!{Style.RESET_ALL}")
       continue