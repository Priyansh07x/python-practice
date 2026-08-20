income = 45000
payable_tax = 0
print(f"Given income: {income}")

if income <= 10000:
    payable_tax = 0
elif income <= 20000:
    payable_tax = (income - 10000) * 10 / 100
else:
    # 10,000 × 0%  = 0
    # 10,000 × 10% = 1,000
    # payable_tax = 0 + 1000
    # payable_tax = 1000
    payable_tax = 0 + (10000 * 10 / 100)
    # Remaining income → 20% tax
    # First 10,000 → 0%
    # Next  10,000 → 10%
    # -------------------
    # Already handled = 20,000
    # So we need to find what remains:
    # income - 20000
    payable_tax += (income - 20000) * 20 / 100

    print("Total income tax to pay is", payable_tax)
