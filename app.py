import pygame
import random
import sys

# Inicializa o Pygame
pygame.init()

# Configurações da tela
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pedra, Papel e Tesoura")

# Cores
white = (255, 255, 255)
black = (0, 0, 0)

# Carregar imagens
rock_img = pygame.image.load('rock.png')
paper_img = pygame.image.load('paper.png')
scissors_img = pygame.image.load('scissors.png')

# Redimensionar imagens
rock_img = pygame.transform.scale(rock_img, (150, 150))
paper_img = pygame.transform.scale(paper_img, (150, 150))
scissors_img = pygame.transform.scale(scissors_img, (150, 150))

# Fonte
font = pygame.font.Font(None, 74)

# Função para exibir texto na tela
def display_message(message, color, y_offset=0):
    text = font.render(message, True, color)
    text_rect = text.get_rect(center=(screen_width/2, screen_height/2 + y_offset))
    screen.blit(text, text_rect)

# Função principal do jogo
def game():
    running = True
    player_choice = None
    computer_choice = None
    result = None

    # Tradução das escolhas para exibição
    choices_translation = {
        "rock": "Pedra",
        "paper": "Papel",
        "scissors": "Tesoura"
    }

    while running:
        screen.fill(white)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if 100 < mouse_x < 250 and 400 < mouse_y < 550:
                    player_choice = "rock"
                elif 325 < mouse_x < 475 and 400 < mouse_y < 550:
                    player_choice = "paper"
                elif 550 < mouse_x < 700 and 400 < mouse_y < 550:
                    player_choice = "scissors"

                if player_choice:
                    computer_choice = random.choice(["rock", "paper", "scissors"])
                    if player_choice == computer_choice:
                        result = "Empate!"
                    elif (player_choice == "rock" and computer_choice == "scissors") or \
                         (player_choice == "paper" and computer_choice == "rock") or \
                         (player_choice == "scissors" and computer_choice == "paper"):
                        result = "Você ganhou!"
                    else:
                        result = "Você perdeu!"

        # Desenhar opções
        screen.blit(rock_img, (100, 400))
        screen.blit(paper_img, (325, 400))
        screen.blit(scissors_img, (550, 400))

        # Exibir escolhas e resultado
        if player_choice:
            display_message(f"Você escolheu: {choices_translation[player_choice]}", black, -100)
            display_message(f"Computador escolheu: {choices_translation[computer_choice]}", black, 0)
            display_message(result, black, 100)

        pygame.display.flip()

# Iniciar o jogo
game()
