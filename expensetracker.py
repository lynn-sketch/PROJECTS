from expenses import Expense
def main():
    print(f"Running expense tracker")
    expense_file_path = "expense.csv"

##Get user input for expense
    expense = get_user_expense()
    

##write their expense to a file
    Saving_expense_to_file(expense,expense_file_path)

##Read the file and summarize the expense
    summarize_expense(expense_file_path)

##Getting user expense
def get_user_expense():
    print(f"Getting a user expense")
    expense_name = input("Please enter the expense_name:")
    expense_amount = float(input("Please enter the expense_amount:"))
    print(f"You have entered {expense_name}, which costs {expense_amount}")

##Creating a list of categories
    expense_categories = [
    "🎂Food",
    "🐱‍🚀Home",
    "👨‍✈️Work",
    "👓Fun",
    "👑Misc"
]

##We use a while loop since we need the user to choose from the list
    while True:
        print("Select category")
        for i, category_name in enumerate(expense_categories):
            print(f" {i+1}.{category_name}")

        ##Creating a range users should choose from
        value_range = f"[1 - {len(expense_categories)}]"
        selected_index = int(input(f"Enter a category number {value_range}: ")) - 1
        
         ##Using an if loop to check if user put the right index
        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(name = expense_name,category= selected_category,amount=expense_amount)
            return new_expense
        else:
            print("please input between the range of 0 to 5")

def Saving_expense_to_file(expense:Expense, expense_file_path):
    print(f"Saving expenses to a file : {expense} to {expense_file_path}")
    with open(expense_file_path,"a",encoding="utf-8") as f :
        f.write(f"{expense.name},{expense.amount},{expense.category}")

def summarize_expense(expense_file_Path):
    print(f"Summarizing user expense")


if __name__ == "__main__":
    main()