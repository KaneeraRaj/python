import pygame
import sys
import random

pygame.init()
WIDTH,HEIGHT=600,400
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Rock,Paper,Scissor")
font=pygame.font.SysFont(None,40)

choices=["Rock","Paper","Scissors"]
buttons=[pygame.Rect(80+i*160,280,130,60)for i in range(3)]

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

    for i,button in enumerate(buttons):
        pygame.draw.rect(screen,(200,200,200),button)

        choice_text=font.render(choices[i].capitalize(),True,(0,0,0))
        screen.blit(choice_text,(button.x +15, button.y + 15))

    if player_choice:
            pc_text=font.render(f"you:{player_choice}",True,(0,0,128))
            cc_text=font.render(f"computer:{computer_choice}",True,(128,0,0))     

            result_text=font.render(result,True,(0,0,0))

            screen.blit(pc_text(50,150))
            screen.blit(cc_text(50,190))
            screen.blit(result_text(50,230))

pygame.display.flip()