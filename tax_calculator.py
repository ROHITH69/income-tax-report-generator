def calculate_tax(income):
    tax = 0
    if income <= 250000:
        tax = 0
    elif income <= 500000:
        tax = (income - 250000) * 0.05
    elif income <= 1000000:
        tax = 12500 + (income - 500000) * 0.2
    else:
        tax = 112500 + (income - 1000000) * 0.3
    return round(tax, 2)
