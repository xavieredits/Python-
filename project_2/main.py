import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV once here
df = pd.read_csv("project_2/books.csv")

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
            print(df)
            print("=================================")
        
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
            break
        else:
            print("Oops!.. looks like an error occurred with keyboard...")
            break

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
            break
        
        else:
            print("Invalid option, please try again.")
            break

# Example of how to run
showData()
analysis()
