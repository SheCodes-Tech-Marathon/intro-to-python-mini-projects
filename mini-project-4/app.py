from engine import Engine


class App:
    def __init__(self):
        print("Chào mừng đến với trò chơi đoán số trong phạm vi từ 1 đến 100!")
        self.engine = Engine()

    def run(self):
        while True:
            guessed_number = int(input("Số bạn muốn đoán: "))
            if self.engine.is_right(guessed_number):
                print(f"Chúc mừng bạn đã đoán đúng số {guessed_number}")
                break
            else:
                print("Bạn chưa đoán chính xác!")
                did_continue_playing = input("Bạn có muốn tiếp tục chơi (y/n): ")
                if did_continue_playing == "y":
                    continue
                else:
                    break
