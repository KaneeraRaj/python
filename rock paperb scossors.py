import pygame,random,sys

pygame.init()
WIDTH,HEIGHT=600,400
screen=pygame.display.set_mode(WIDTH,HEIGHT)
pygame.display.set_caption("Rock,Paper,Scissor")
font=pygame.font.Sysfont(None,40)

choices=["Rock","Paper","Scissors"]
buttons=[pygame.Recct(80+i*160,280,130,60)for i in range(3)]

player_choice=""
computer_choice=""
result=""

def get_winner(player,computer):
    if player==computer:
        return "Its a tie!"
    rules={"Rock":"Sissors","Scissors":"paper","paper":"Rock"}

    return "You win!" if rules[player]==computer else "Computer wins"

while True:
    screen.fill((245,245,245))

    title=font.render("Rock,Paper,Scissors",True,(0,0,128))

    screen.blit(title,(WIDTH//2-title.get_width()//2,40))
           