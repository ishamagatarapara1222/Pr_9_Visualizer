import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


class SalesDataAnalyzer:

    def __init__(self):
        self.df = None

    # Load CSV file
    def load_data(self):
        try:
            self.df = pd.read_csv("data/sales_data.csv")
            print("\nDataset loaded successfully!")
            print(self.df.head())
        except FileNotFoundError:
            print("CSV file not found. Please check the data folder.")
        except Exception as e:
            print("Error:", e)

    # Show basic information about data
    def explore_data(self):
        if self.df is None:
            print("First load the dataset.")
            return

        print("\n1. First 5 rows")
        print("2. Dataset information")
        print("3. Dataset description")

        choice = input("Enter choice: ")

        if choice == "1":
            print(self.df.head())
        elif choice == "2":
            self.df.info()
        elif choice == "3":
            print(self.df.describe())
        else:
            print("Wrong choice.")

    # Search, sort and filter data
    def data_operations(self):
        if self.df is None:
            print("First load the dataset.")
            return

        print("\n1. Search product")
        print("2. Sort sales")
        print("3. Show sales above a value")
        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter product name: ")
            result = self.df[self.df["Product"].str.contains(name, case=False, na=False)]
            print(result)

        elif choice == "2":
            result = self.df.sort_values(by="Sales")
            print(result)

        elif choice == "3":
            try:
                amount = float(input("Enter sales amount: "))
                result = self.df[self.df["Sales"] > amount]
                print(result)
            except ValueError:
                print("Please enter a number.")

        else:
            print("Wrong choice.")

    # Find and handle missing values
    def missing_data(self):
        if self.df is None:
            print("First load the dataset.")
            return

        print("\nMissing values:")
        print(self.df.isnull().sum())

        print("\n1. Remove rows with missing values")
        print("2. Fill missing values with 0")
        choice = input("Enter choice: ")

        if choice == "1":
            self.df = self.df.dropna()
            print("Missing rows removed.")
        elif choice == "2":
            self.df = self.df.fillna(0)
            print("Missing values filled with 0.")
        else:
            print("No changes made.")

    # Calculate basic statistics
    def statistics(self):
        if self.df is None:
            print("First load the dataset.")
            return

        print("\nSales Statistics")
        print("Total Sales:", self.df["Sales"].sum())
        print("Average Sales:", self.df["Sales"].mean())
        print("Highest Sales:", self.df["Sales"].max())
        print("Lowest Sales:", self.df["Sales"].min())

        print("\nComplete description:")
        print(self.df.describe())

    # Create charts using Matplotlib
    def matplotlib_graph(self):
        if self.df is None:
            print("First load the dataset.")
            return

        print("\n1. Bar Chart")
        print("2. Line Chart")
        print("3. Scatter Plot")
        print("4. Histogram")
        choice = input("Enter choice: ")

        if choice == "1":
            plt.bar(self.df["Product"], self.df["Sales"])
            plt.xticks(rotation=45)
            plt.xlabel("Product")
            plt.ylabel("Sales")
            plt.title("Product Sales")
        elif choice == "2":
            plt.plot(self.df["Date"], self.df["Sales"], marker="o")
            plt.xticks(rotation=45)
            plt.xlabel("Date")
            plt.ylabel("Sales")
            plt.title("Sales Over Time")
        elif choice == "3":
            plt.scatter(self.df["Quantity"], self.df["Sales"])
            plt.xlabel("Quantity")
            plt.ylabel("Sales")
            plt.title("Quantity vs Sales")
        elif choice == "4":
            plt.hist(self.df["Sales"], bins=5, edgecolor="black")
            plt.xlabel("Sales")
            plt.ylabel("Frequency")
            plt.title("Sales Distribution")
        else:
            print("Wrong choice.")
            return

        plt.tight_layout()
        plt.show()

        save = input("Do you want to save this chart? (y/n): ")
        if save.lower() == "y":
            if not os.path.exists("outputs"):
                os.makedirs("outputs")
            plt.savefig("outputs/sales_chart.png")
            print("Chart saved in outputs folder.")

        plt.close()

    # Create charts using Seaborn
    def seaborn_graph(self):
        if self.df is None:
            print("First load the dataset.")
            return

        print("\n1. Heatmap")
        print("2. Box Plot")
        choice = input("Enter choice: ")

        if choice == "1":
            sns.heatmap(self.df[["Quantity", "Unit_Price", "Sales", "Profit"]].corr(),
                        annot=True, cmap="coolwarm")
            plt.title("Sales Data Heatmap")
        elif choice == "2":
            sns.boxplot(x=self.df["Sales"])
            plt.title("Sales Box Plot")
        else:
            print("Wrong choice.")
            return

        plt.show()
        plt.close()

    # Save updated data
    def save_data(self):
        if self.df is None:
            print("First load the dataset.")
            return

        if not os.path.exists("outputs"):
            os.makedirs("outputs")

        self.df.to_csv("outputs/updated_sales_data.csv", index=False)
        print("Data saved in outputs folder.")

    # Main menu
    def menu(self):
        while True:
            print("\n===== PANDAS ANALYZER & DATA VISUALIZATION =====")
            print("1. Load Dataset")
            print("2. Explore Data")
            print("3. Data Operations")
            print("4. Handle Missing Data")
            print("5. Generate Statistics")
            print("6. Matplotlib Visualization")
            print("7. Seaborn Visualization")
            print("8. Save Dataset")
            print("9. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.load_data()
            elif choice == "2":
                self.explore_data()
            elif choice == "3":
                self.data_operations()
            elif choice == "4":
                self.missing_data()
            elif choice == "5":
                self.statistics()
            elif choice == "6":
                self.matplotlib_graph()
            elif choice == "7":
                self.seaborn_graph()
            elif choice == "8":
                self.save_data()
            elif choice == "9":
                print("Thank you!")
                break
            else:
                print("Invalid choice. Try again.")


obj = SalesDataAnalyzer()
obj.menu()
