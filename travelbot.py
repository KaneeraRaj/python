import re,random
from colorama import Fore,init
init(autoreset=True)

destinations={
    "beaches":["Maldives","Bali","Hawaii"],
    "hill stations":["Ooty","Mussorie","Gangtok"],
    "adventures":["Rishikesh","Delhi","California"],
}
jokes=[
    "Why dont programmers like nature? Too many bugs!"
    "Why did the computer go to the doctor? Because it has virus!"
    "Why do travellers always feel warm? Because they have hot spots!"
]
normalize = lambda t: re.sub(r"\s+", " ", t.strip().lower())
def recommend():
    pref = normalize(input(f"{Fore.CYAN}Beaches, mountains, or cities?\n{Fore.YELLOW}You: "))
    if pref not in destinations: return print(f"{Fore.RED}Sorry, no such option.")
    while True:
        s = random.choice(destinations[pref])
        print(f"{Fore.GREEN}How about {s}?")
        a = input(f"{Fore.YELLOW}You (yes/no): ").lower()
        if a == "yes": return print(f"{Fore.GREEN}Awesome! Enjoy {s}!")
        if a != "no": return

def packing():
    loc = normalize(input(f"{Fore.CYAN}Where to?\n{Fore.YELLOW}You: "))
    days = input(f"{Fore.CYAN}How many days?\n{Fore.YELLOW}You: ")
    print(f"{Fore.GREEN}Packing tips for {days} days in {loc}:\n- Clothes\n- Chargers\n- Check weather")

tell_joke = lambda: print(f"{Fore.GREEN}{random.choice(jokes)}")
show_help = lambda: print(f"""{Fore.MAGENTA}
I can:
{Fore.GREEN}- Suggest spots ('recommend')
- Packing tips ('packing')
- Tell a joke ('joke')
- Show help ('help')
- Exit ('exit')\n""")

def chat():
    print(f"{Fore.CYAN}Hello! I’m TravelBot.")
    name = input(f"{Fore.YELLOW}Your name? ")
    print(f"{Fore.GREEN}Nice to meet you, {name}!")
    show_help()

    cmds = {"recommend": recommend, "suggest": recommend, "pack": packing,
            "joke": tell_joke, "funny": tell_joke, "help": show_help}
    
    while True:
        u = normalize(input(f"{Fore.YELLOW}{name}: "))
        if any(x in u for x in ["exit","bye"]): return print(f"{Fore.CYAN}Safe travels, goodbye!")
        for k,f in cmds.items():
            if k in u: f(); break
        else: print(f"{Fore.RED}Could you rephrase?")

if __name__ == "__main__": chat()

                                   
