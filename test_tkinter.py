import tkinter as tk
import csv


class Expense:

    def __init__(self, amount, category):
        self.amount = amount
        self.category = category


expenses = []


# LOAD OLD EXPENSES
try:

    with open("expenses.csv", "r") as file:

        reader = csv.reader(file)

        for row in reader:

            amount = row[0]
            category = row[1]

            expense = Expense(
                amount,
                category
            )

            expenses.append(expense)

except FileNotFoundError:
    pass


# WINDOW
window = tk.Tk()

window.title("💸 Varnika's Expense Tracker 💸")
window.geometry("600x700")

window.configure(
    bg="#FFF5E4"
)


# TITLE
title = tk.Label(
    window,
    text="💸 Expense Tracker 💸",
    font=("Arial", 24, "bold"),
    bg="#FFF5E4",
    fg="#FF6600"
)

title.pack(pady=15)


# AMOUNT
amount_label = tk.Label(
    window,
    text="💵 Amount",
    bg="#FFF5E4",
    font=("Arial", 12)
)

amount_label.pack()

amount_entry = tk.Entry(
    window,
    font=("Arial", 12)
)

amount_entry.pack(pady=5)


# CATEGORY
category_label = tk.Label(
    window,
    text="🏷️ Category",
    bg="#FFF5E4",
    font=("Arial", 12)
)

category_label.pack()

category_entry = tk.Entry(
    window,
    font=("Arial", 12)
)

category_entry.pack(pady=5)


# LISTBOX
expense_listbox = tk.Listbox(
    window,
    width=40,
    height=15,
    font=("Arial", 12)
)

expense_listbox.pack(pady=15)


# TOTAL

total_label = tk.Label(
    window,
    text="💰 Total: ₹0",
    font=("Arial", 18)
)

total_label.pack()
summary_label = tk.Label(
    window,
    text="",
    bg="#F5EBDD",
    fg="blue",
    font=("Arial", 11)
)

summary_label.pack(pady=10)


def update_display():

    expense_listbox.delete(0, tk.END)

    for expense in expenses:

        expense_listbox.insert(
            tk.END,
            f"{expense.category} - ₹{expense.amount}"
        )

    total = 0

    for expense in expenses:
        total += float(expense.amount)

    total_label.config(
        text=f"💰 Total: ₹{total}"
    )
categories = {}

for expense in expenses:

    if expense.category not in categories:
        categories[expense.category] = 0

    categories[expense.category] += float(
        expense.amount
    )

summary_text = "📊 Category Summary\n\n"

for category, amount in categories.items():

    summary_text += (
        f"{category}: ₹{amount}\n"
    )

summary_label.config(
    text=summary_text
)


def add_expense():
      

    amount = amount_entry.get()
    category = category_entry.get()

    if amount == "" or category == "":
        return

    expense = Expense(
        amount,
        category
    )

    expenses.append(expense)
    update_display()

    with open(
        "expenses.csv",
        "a",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            expense.amount,
            expense.category
        ])

    update_display()

    amount_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)

def delete_expense():

    if len(expenses) > 0:
        expenses.pop()

        
# BUTTON
add_button = tk.Button(
    window,
    text="➕ Add Expense",
    command=add_expense,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 12, "bold")
)

add_button.pack(pady=10)


delete_button = tk.Button(
    window,
    text="🗑 Delete Last",
    command=delete_expense
)

delete_button.pack()





# SHOW OLD DATA
update_display()


window.mainloop()