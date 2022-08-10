print("---------- Chào mừng đến với ứng dụng tính toán cơ bản ----------")
print("Ứng dụng này chỉ có thể thực hiện phép tính giữa hai số\nvới nhau, sau đây là các phép tính mà ứng dụng có thể thực hiện")
print("1. Thực hiện phép cộng (nhập +)")
print("2. Thực hiện phép trừ (nhập -)")
print("3. Thực hiện phép nhân (nhập *)")
print("4. Thực hiện phép chia (nhập /)")
print("-----------------------------------------------------------------")

option = input("Vui lòng chọn phép tính mà bạn muốn thực hiện: ")
num1 = input("Vui lòng nhập số thứ nhất: ")
num2 = input("Vui lòng nhập số thứ hai: ")

num1 = int(num1)
num2 = int(num2)

if option == "+":
    print(f"Kết quả: {num1 + num2}")
elif option == "-":
    print(f"Kết quả: {num1 - num2}")
elif option == "*":
    print(f"Kết quả: {num1 * num2}")
elif option == "/":
    print(f"Kết quả: {num1 / num2}")
else:
    print("Phép tính không hợp lệ.")
