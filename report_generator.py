import os

def generate_report(name, income, tax):
    filename = f"{name.lower().replace(' ', '_')}_report.txt"
    content = (
        f"Income Tax Report\n"
        f"------------------\n"
        f"Name          : {name}\n"
        f"Annual Income : ₹{income}\n"
        f"Tax Payable   : ₹{tax}\n"
    )

    with open(filename, "w") as file:
        file.write(content)
    print(f"✅ Report generated for {name}: {filename}")
