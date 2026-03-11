decimals = [10, 25, 42]

for num in decimals:
    binary = ""
    temp_num = num
    
    
    while temp_num > 0:
        remainder = temp_num % 2
        binary = str(remainder) + binary
        temp_num //= 2
        
    print(f"Decimal: {num} -> Binary: {binary if binary else '0'}")
