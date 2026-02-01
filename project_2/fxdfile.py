import pandas as pd
import matplotlib.pyplot as plt

# Load both CSV files
book_df = pd.read_csv(r'C:\Users\aryan\Documents\book_details.csv')
sales_df = pd.read_csv(r'C:\Users\aryan\Documents\sales_details.csv')

# ================= DATA VIEW SECTION =================
def showData():
    while True:
        print("=================================")
        print("|           Data View            |")
        print("---------------------------------")
        print("| 1. Show Book Details           |")
        print("| 2. Show Sales Details          |")
        print("| 3. Search a Book               |")
        print("| 4. Back to Main Menu           |")
        print("=================================")

        user = int(input("Select an option: "))

        if user == 1:
            print("\n--- Book Details ---")
            print(book_df)

        elif user == 2:
            print("\n--- Sales Details ---")
            print(sales_df)

        elif user == 3:
            term = input("Enter book name / author: ").lower()

            merged = pd.merge(book_df, sales_df, on=["Title", "Author"])
            result = merged[
                merged["Title"].str.lower().str.contains(term) |
                merged["Author"].str.lower().str.contains(term)
            ]

            if not result.empty:
                print("\nBook Found:")
                print(result)
            else:
                print("No match found.")

        elif user == 4:
            return
        else:
            print("Invalid option.")


# ================= ANALYSIS SECTION =================
def analysis():
    while True:
        print("=================================")
        print("|          Data Analysis         |")
        print("---------------------------------")
        print("| 1. Top Selling Books           |")
        print("| 2. Least Selling Books         |")
        print("| 3. Highest Priced Books        |")
        print("| 4. Back to Main Menu           |")
        print("=================================")

        userA = int(input("Select an option: "))

        if userA == 1:
            top = sales_df.sort_values(by="Sales", ascending=False).head(5)
            print(top)

        elif userA == 2:
            least = sales_df.sort_values(by="Sales").head(5)
            print(least)

        elif userA == 3:
            high_price = book_df.sort_values(by="Price", ascending=False).head(5)
            print(high_price)

        elif userA == 4:
            return
        else:
            print("Invalid option.")


# ================= DATA ALTERATION =================
def Altration():
    while True:
        print("=================================")
        print("|        Data Alteration         |")
        print("---------------------------------")
        print("| 1. Add New Book                |")
        print("| 2. Add Sales Entry             |")
        print("| 3. Update Book Price           |")
        print("| 4. Back to Main Menu           |")
        print("=================================")

        userB = int(input("Select option: "))

        if userB == 1:
            new_book = []
            for col in book_df.columns:
                value = input(f"Enter {col}: ")
                new_book.append(value)

            book_df.loc[len(book_df)] = new_book
            book_df.to_csv("project_2/book_details.csv", index=False)
            print("Book added successfully!")

        elif userB == 2:
            new_sale = []
            for col in sales_df.columns:
                value = input(f"Enter {col}: ")
                new_sale.append(value)

            sales_df.loc[len(sales_df)] = new_sale
            sales_df.to_csv("project_2/sales_details.csv", index=False)
            print("Sales entry added!")

        elif userB == 3:
            print(book_df)
            row = int(input("Enter row index: "))
            new_price = input("Enter new price: ")
            book_df.at[row, "Price"] = new_price
            book_df.to_csv("project_2/book_details.csv", index=False)
            print("Price updated!")

        elif userB == 4:
            return
        else:
            print("Invalid option.")


# ================= GRAPHS =================
def graphs():
    merged = pd.merge(book_df, sales_df, on=["Title", "Author"])

    while True:
        print("=================================")
        print("|            Graphs              |")
        print("---------------------------------")
        print("| 1. Book vs Sales               |")
        print("| 2. Book vs Rating              |")
        print("| 3. Back to Main Menu           |")
        print("=================================")

        choice = int(input("Select option: "))

        if choice == 1:
            plt.plot(merged["Title"], merged["Sales"])
            plt.xticks(rotation=45)
            plt.title("Book vs Sales")
            plt.show()

        elif choice == 2:
            plt.plot(merged["Title"], merged["Rating"])
            plt.xticks(rotation=45)
            plt.title("Book vs Rating")
            plt.show()

        elif choice == 3:
            return
        else:
            print("Invalid option.")


# ================= MAIN MENU =================
def MainMenue():
    while True:
        print("=================================")
        print("|           Main Menu            |")
        print("---------------------------------")
        print("| 1. Show Data                   |")
        print("| 2. Analysis                    |")
        print("| 3. Alteration                  |")
        print("| 4. Graphs                      |")
        print("| 5. Exit                        |")
        print("=================================")

        choice = int(input("Select option: "))

        if choice == 1:
            showData()
        elif choice == 2:
            analysis()
        elif choice == 3:
            Altration()
        elif choice == 4:
            graphs()
        elif choice == 5:
            print("Exiting program...")
            break
        else:
            print("Invalid option.")


MainMenue()
