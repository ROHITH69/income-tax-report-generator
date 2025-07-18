from tax_calculator import calculate_tax
from report_generator import generate_report
import json

def load_user_data():
    with open("data.json", "r") as file:
        return json.load(file)

def main():
    users = load_user_data()
    for user in users:
        name = user["name"]
        income = user["annual_income"]
        tax = calculate_tax(income)
        generate_report(name, income, tax)

if __name__ == "__main__":
    main()
