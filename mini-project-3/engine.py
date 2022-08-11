def find_winner(player_choice, computer_choice):
    if (player_choice == rock and computer_choice == scissor) or (player_choice == scissor and computer_choice == paper) or (player_choice == paper and computer_choice == rock):
        return "Người chơi"
    elif (player_choice == scissor and computer_choice == rock) or (player_choice == paper and computer_choice == scissor) or (player_choice == rock and computer_choice == paper):
        return "Máy"
    else:
        return "Không ai"
