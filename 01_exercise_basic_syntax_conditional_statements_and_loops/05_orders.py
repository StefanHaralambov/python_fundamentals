number_of_orders = int(input())
total_price = 0

for orders in range(number_of_orders):
    current_order_price = float(input())
    days = int(input())
    capsules_per_day = int(input())

    if 0.01 > current_order_price or current_order_price > 100:
        continue
    elif 0 > days or days > 31:
        continue
    elif 1 > capsules_per_day or capsules_per_day > 2000:
        continue

    price_for_coffe = days * capsules_per_day * current_order_price
    total_price += price_for_coffe
    print(f"The price for the coffee is: ${price_for_coffe:.2f}")

print(f"Total: ${total_price:.2f}")
