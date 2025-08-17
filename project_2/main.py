import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV once here
df = pd.read_csv("project_2/books.csv")

# dataview or review seciton 
def showData():
    while True:
        print("=================================")
        print("|           Option 1            |")
        print("---------------------------------")
        print("|      1. Show all Data         |")
        print("|      2. Find a book           |")
        print("|      3. Back to main menu     |")
        print("=================================")

        user = int(input("Select an option to continue: "))
        
        if user == 1:
            print("Displaying...")
            print("=================================")
            # Calculate Revenue (Price * Sales) and add/update column
            df["Revenue"] = df["Price"] * df["Sales"]
            print(df)
            print("=================================")
            # Save back to CSV with Revenue column
            df.to_csv("project_2/books.csv", index=False)
        
        elif user == 2:
            search_term = input("Enter a book name / book id / author name: ").lower()
            results = df[df.apply(lambda row: row.astype(str).str.lower().str.contains(search_term).any(), axis=1)]
            
            if not results.empty:
                print("Found the following matches:")
                print(results)
            else:
                print("No matching book found.")
        
        elif user == 3:
            print("Getting you back...")
            MainMenue()
        else:
            print("Oops!.. looks like an error occurred with keyboard...")
            MainMenue()
# Analysis section [data analysis and quries]
def analysis():
    while True:
        print("=================================")
        print("|          Data Analysis        |")
        print("---------------------------------")
        print("|      1. TOP Selling books     |")
        print("|      2. LEAST Selling books   |")
        print("|      3. Most Rated books      |")
        print("|      4. Highest priced        |")
        print("|      5. Lowest priced         |")
        print("|      6. Back to main menu     |")
        print("=================================")
        
        userA = int(input("Select an option: "))
        
        if userA == 1:
            top_selling = df.sort_values(by="Sales", ascending=False).head(5)
            print("Top Selling Books:")
            print(top_selling)
        
        elif userA == 2:
            least_selling = df.sort_values(by="Sales", ascending=True).head(5)
            print("Least Selling Books:")
            print(least_selling)
        
        elif userA == 3:
            most_rated = df.sort_values(by="Rating", ascending=False).head(5)
            print("Most Rated Books:")
            print(most_rated)
        
        elif userA == 4:
            highest_priced = df.sort_values(by="Price", ascending=False).head(5)
            print("Highest Priced Books:")
            print(highest_priced)
        
        elif userA == 5:
            lowest_priced = df.sort_values(by="Price", ascending=True).head(5)
            print("Lowest Priced Books:")
            print(lowest_priced)
        
        elif userA == 6:
            print("Returning to main menu...")
            MainMenue()
        
        else:
            print("Invalid option, please try again.")
            MainMenue()

# data manipulation 
def Altration():
    while True:
        print("=================================")
        print("|         Data Altration        |")
        print("---------------------------------")
        print("|      1. Add a row             |")
        print("|      2. Insert a column       |")
        print("|      3. Delete a row          |")
        print("|      4. Delete a column       |")
        print("|      5. Update a cell value   |")
        print("|      6. Back to main menu     |")
        print("=================================")

        UserB = int(input("Select an Option: "))

        if UserB == 1:
            print("Current Columns:", list(df.columns))
            new_data = [] # empty list to store data entered 
            for col in df.columns:
                value = input(f"Enter value for {col}: ") # entering value accessing col for ref
                new_data.append(value) #adding value to empty list 
            new_row = pd.DataFrame([new_data], columns=df.columns)# adding value of data to dataframe
            df.loc[len(df)] = new_data
            df.to_csv("project_2/books.csv", index=False)
            print("Row added successfully!")

        elif UserB == 2:
            col_name = input("Enter new column name: ") # for column name 
            default_value = input("Enter default value for all rows: ") # entering values 
            df[col_name] = default_value
            df.to_csv("project_2/books.csv", index=False)
            print("Column added successfully!")

        elif UserB == 3:
            print(df)
            row_index = int(input("Enter row index to delete: "))
            df.drop(index=row_index, inplace=True)
            df.to_csv("project_2/books.csv", index=False)
            print("Row deleted successfully!")

        elif UserB == 4:
            print("Columns:", list(df.columns))
            col_name = input("Enter column name to delete: ")
            df.drop(columns=col_name, inplace=True)
            df.to_csv("project_2/books.csv", index=False)
            print("Column deleted successfully!")

        elif UserB == 5:
            print(df)
            row_index = int(input("Enter row index to update: "))
            col_name = input("Enter column name to update: ")
            new_value = input("Enter new value: ")
            df.at[row_index, col_name] = new_value
            df.to_csv("project_2/books.csv", index=False)
            print("Value updated successfully!")

        elif UserB == 6:
            print("Returning to main menu...")
            MainMenue()

        else:
            print("Invalid option, try again.")


# Example of how to run

def MainMenue():
    while True:
        print("=================================")
        print("|           Main Menue          |")
        print("---------------------------------")
        print("|      1. showData              |")
        print("|      2. Analysis              |")
        print("|      3. Altration             |")
        print("|      4. Graphs                |")
        print("|      5. exit                  |")
        print("=================================")

        UserC = int(input("Select an Option: "))
        if UserC ==1:
            print("Loading....")
            showData()
        elif UserC ==2:
            print("Loading....")
            analysis()
        elif UserC ==3:
            print("Loading....")
            Altration()
        elif UserC == 4:
            #  graphs()
            break
        elif UserC == 5:
            print("Exiting")
            break;
        else:
            print("Invalid option, try again.")
            break;

MainMenue()