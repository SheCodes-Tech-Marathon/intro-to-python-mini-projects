from random import choice
from engine import find_winner

rock = "đấm"
scissor = "kéo"
paper = "lá"

player_choice = input("Lựa chọn của người chơi (đấm, lá, kéo): ")
if player_choice != rock and player_choice != scissor and player_choice != paper:
    print("Lựa chọn không hợp lệ!")
    exit(1)

computer_choice = choice([rock, paper, scissor])

winner = find_winner(player_choice, computer_choice)
print(f"{winner} thắng")
