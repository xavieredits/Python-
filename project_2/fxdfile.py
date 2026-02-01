import pandas as pd
import matplotlib.pyplot as plt

# ================= FILE PATHS (WINDOWS SAFE) =================
BOOK_PATH = r"C:\Users\aryan\Documents\book_details.csv"
SALES_PATH = r"C:\Users\aryan\Documents\sales_details.csv"

book_df = pd.read_csv(BOOK_PATH)
sales_df = pd.read_csv(SALES_PATH)


# ================= DATA VIEW =================
def showData():
    while True:
        print("=================================")
        print("|           Data View            |")
        print("---------------------------------")
        print("| 1. Show Book Details           |")
        print("| 2. Show Sales Details          |")
        print("| 3. Back to Main Menu           |")
        print("=================================")

        ch = int(input("Select option: "))

        if ch == 1:
            print(book_df)
        elif ch == 2:
            print(sales_df)
        elif ch == 3:
            return
        else:
            print("Invalid option.")


# ================= ANALYSIS =================
def analysis():
    while True:
        print("=================================")
        print("|          Data Analysis         |")
        print("---------------------------------")
        print("| 1. Top Selling Books           |")
        print("| 2. Least Selling Books         |")
        print("| 3. Most Rated Books            |")
        print("| 4. Least Rated Books           |")
        print("| 5. Back to Main Menu           |")
        print("=================================")

        ch = int(input("Select option: "))

        if ch == 1:
            print(sales_df.sort_values(by="Sales", ascending=False)[["Title", "Author", "Sales"]])

        elif ch == 2:
            print(sales_df.sort_values(by="Sales")[["Title", "Author", "Sales"]])

        elif ch == 3:
            print(book_df.sort_values(by="Rating", ascending=False)[["Title", "Author", "Rating"]])

        elif ch == 4:
            print(book_df.sort_values(by="Rating")[["Title", "Author", "Rating"]])

        elif ch == 5:
            return
        else:
            print("Invalid option.")


# ================= DATA ALTERATION =================
def Altration():
    while True:
        print("=================================")
        print("|        Data Alteration         |")
        print("---------------------------------")
        print("| 1. Add Book Row                |")
        print("| 2. Add Sales Row               |")
        print("| 3. Delete Book Row             |")
        print("| 4. Delete Sales Row            |")
        print("| 5. Add Book Column             |")
        print("| 6. Add Sales Column            |")
        print("| 7. Delete Book Column          |")
        print("| 8. Delete Sales Column         |")
        print("| 9. Update Book Value           |")
        print("|10. Update Sales Value          |")
        print("|11. Back to Main Menu           |")
        print("=================================")

        ch = int(input("Select option: "))

        # ADD BOOK ROW
        if ch == 1:
            row = []
            for col in book_df.columns:
                row.append(input(f"Enter {col}: "))
            book_df.loc[len(book_df)] = row
            book_df.to_csv(BOOK_PATH, index=False)
            print("Book row added!")

        # ADD SALES ROW
        elif ch == 2:
            row = []
            for col in sales_df.columns:
                row.append(input(f"Enter {col}: "))
            sales_df.loc[len(sales_df)] = row
            sales_df.to_csv(SALES_PATH, index=False)
            print("Sales row added!")

        # DELETE BOOK ROW
        elif ch == 3:
            print(book_df)
            idx = int(input("Enter row index: "))
            book_df.drop(idx, inplace=True)
            book_df.to_csv(BOOK_PATH, index=False)
            print("Book row deleted!")

        # DELETE SALES ROW
        elif ch == 4:
            print(sales_df)
            idx = int(input("Enter row index: "))
            sales_df.drop(idx, inplace=True)
            sales_df.to_csv(SALES_PATH, index=False)
            print("Sales row deleted!")

        # ADD BOOK COLUMN
        elif ch == 5:
            col = input("Enter new column name: ")
            val = input("Enter default value: ")
            book_df[col] = val
            book_df.to_csv(BOOK_PATH, index=False)
            print("Book column added!")

        # ADD SALES COLUMN
        elif ch == 6:
            col = input("Enter new column name: ")
            val = input("Enter default value: ")
            sales_df[col] = val
            sales_df.to_csv(SALES_PATH, index=False)
            print("Sales column added!")

        # DELETE BOOK COLUMN
        elif ch == 7:
            print(list(book_df.columns))
            col = input("Enter column name: ")
            book_df.drop(columns=col, inplace=True)
            book_df.to_csv(BOOK_PATH, index=False)
            print("Book column deleted!")

        # DELETE SALES COLUMN
        elif ch == 8:
            print(list(sales_df.columns))
            col = input("Enter column name: ")
            sales_df.drop(columns=col, inplace=True)
            sales_df.to_csv(SALES_PATH, index=False)
            print("Sales column deleted!")

        # UPDATE BOOK VALUE
        elif ch == 9:
            print(book_df)
            r = int(input("Row index: "))
            c = input("Column name: ")
            v = input("New value: ")
            book_df.at[r, c] = v
            book_df.to_csv(BOOK_PATH, index=False)
            print("Book value updated!")

        # UPDATE SALES VALUE
        elif ch == 10:
            print(sales_df)
            r = int(input("Row index: "))
            c = input("Column name: ")
            v = input("New value: ")
            sales_df.at[r, c] = v
            sales_df.to_csv(SALES_PATH, index=False)
            print("Sales value updated!")

        elif ch == 11:
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

        ch = int(input("Select option: "))

        if ch == 1:
            plt.plot(merged["Title"], merged["Sales"])
            plt.xticks(rotation=45)
            plt.title("Book vs Sales")
            plt.show()

        elif ch == 2:
            plt.plot(merged["Title"], merged["Rating"])
            plt.xticks(rotation=45)
            plt.title("Book vs Rating")
            plt.show()

        elif ch == 3:
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

        ch = int(input("Select option: "))

        if ch == 1:
            showData()
        elif ch == 2:
            analysis()
        elif ch == 3:
            Altration()
        elif ch == 4:
            graphs()
        elif ch == 5:
            print("Exiting...")
            break
        else:
            print("Invalid option.")


MainMenue()
