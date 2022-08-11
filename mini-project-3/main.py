from random import choice

rock = "đấm"
scissor = "kéo"
paper = "lá"


def find_winner(player_choice, computer_choice):
    if (player_choice == rock and computer_choice == scissor) or (player_choice == scissor and computer_choice == paper) or (player_choice == paper and computer_choice == rock):
        return "Người chơi"
    elif (player_choice == scissor and computer_choice == rock) or (player_choice == paper and computer_choice == scissor) or (player_choice == rock and computer_choice == paper):
        return "Máy"
    else:
        return "Không ai"


player_choice = input("Lựa chọn của người chơi (đấm, lá, kéo): ")
if player_choice != rock and player_choice != scissor and player_choice != paper:
    print("Lựa chọn không hợp lệ!")
    exit(1)

computer_choice = choice([rock, paper, scissor])

winner = find_winner(player_choice, computer_choice)
print(f"{winner} thắng")
