from random import choice

def find_winner(player_choice, computer_choice):
    if (player_choice == "đấm" and computer_choice == "kéo") or (player_choice == "kéo" and computer_choice == "lá") or (player_choice == "lá" and computer_choice == "đấm"):
        return "Người chơi"
    elif (player_choice == "kéo" and computer_choice == "đấm") or (player_choice == "lá" and computer_choice == "kéo") or (player_choice == "đấm" and computer_choice == "lá"):
        return "Máy"
    else:
        return "Không ai"

player_choice = input("Lựa chọn của người chơi (đấm, lá, kéo): ")
computer_choice = choice(["đấm", "lá", "kéo"])

winner = find_winner(player_choice, computer_choice)
print(f"{winner} thắng")
