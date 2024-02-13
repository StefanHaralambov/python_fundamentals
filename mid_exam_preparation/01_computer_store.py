total_price_without_taxes = 0
taxes = 0
is_special = False

while True:
    command = input()
    if command == "special":
        is_special = True
        break
    elif command == "regular":
        break
    if float(command) < 0:
        print("Invalid price!")
        continue
    total_price_without_taxes += float(command)
    taxes += float(command) * 0.2

total_price_with_taxes = total_price_without_taxes + taxes

if is_special:
    total_price_with_taxes *= 0.9
if total_price_with_taxes == 0:
    print("Invalid order!")
else:
    print(
        f"Congratulations you've just bought a new computer!\n"
        f"Price without taxes: {total_price_without_taxes:.2f}$\n"
        f"Taxes: {taxes:.2f}$\n"
        f"-----------\n"
        f"Total price: {total_price_with_taxes:.2f}$")
