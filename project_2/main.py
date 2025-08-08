import pandas as pd 
import matplotlib.pyplot as plt

def showData():
    df=pd.read_csv('project_2/books.csv')
    while True:
        print("=================================")
        print("|           Option 1            |")
        print("---------------------------------")
        print("|      1. Show all Data         |")
        print("|      2.  Find a book          |")
        print("|      3.Back to main menue     |")
        print("=================================")

        user = int(input("Select an option to continue :"))
        if user == 1:
            print("Displaying...")
            print("=================================")
            print(df)
            print("=================================")
        elif user == 2:
         print("Finding...")
         search_query = input("Enter a book name, book ID (ISBN), or author name: ").strip().lower()

    # Check across multiple columns for a match (case-insensitive)
         results = df[
         df.apply(lambda row: 
            search_query in str(row['Title']).lower() or
            search_query in str(row['Author']).lower() or
            search_query in str(row['ISBN']).lower(),axis=1)]

         if not results.empty:
           print("=================================")
           print(results)
           print("=================================")
         else:
          print("No matching books found.")
        elif user == 3:
            print("getting you back...")
            break
            
        else:
            print("opps!.. looks like a error occoured with keyboard...")
            break

showData()
