# 1. Define value of Euro and Dollar in Mexican Pesos

eur_to_mxn = 20.0  # 1 EUR = 20 MXN
usd_to_mxn = 18.0  # 1 USD = 18 MXN

# 2. Ask the user the choice of currency

print("Choose the currency you want to convert to Mexican Pesos:")
print("1. Euro (EUR)")
print("2. Dollar (USD)")
choice = input("Enter your choice (1 or 2): ")

# 3. Ask the user the amount of money they want to convert

amount_convert = float(input("Enter the amount of money you want to convert: "))

# 4. Convert the amount to Mexican Pesos based on the user's choice
# 5. Display the converted amount in Mexican Pesos

if choice == '1':
    # Convert Euro to Mexican Pesos
    converted_amount = amount_convert * eur_to_mxn
    print(f"{amount_convert} EUR is equal to {converted_amount} MXN.")
elif choice == '2':
    # Convert Dollar to Mexican Pesos
    converted_amount = amount_convert * usd_to_mxn
    print(f"{amount_convert} USD is equal to {converted_amount} MXN.")
else:
    # Invalid choice
    print("This conversion is not available.")





