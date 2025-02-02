from scipy.misc import derivative
import matplotlib.pyplot as plt
import numpy as np
import time
import sqlite3
import pandas as pd
import os
from datetime import datetime

connection = sqlite3.connect("economic_data.db")
cursor = connection.cursor()

class EconomicGraph:
    def __init__(self, db):
        """
        Initialize the EconomicGraph class.

        :param db: An instance of the Database class.
        """
        self.db = db
        self.choice = None

    def display_options(self):
        print("Which graph would you like to draw and take information from:")
        time.sleep(1)
        print("Option (1): GDP")
        print("Option (2): Unemployment Rate")
        print("Option (3): Inflation Rate")
        print("Option (4): GDP per capita")
        print("Option (5): Demand/Supply Curves")
        print("Option (6): Aggregate Demand and Aggregate Supply")
        print("Option (7): Phillips Curve")
        print("Option (8): Price and Income Elasticity")
        print(" ")
        self.choice = input("Pick your option: \n")

    def draw_graph(self):
        while True:
            graph_methods = {
                '1': self.gdp,
                '2': self.unemployment_rate,
                '3': self.inflation_rate,
                '4': self.gdp_per_cap,
            }

            if self.choice in graph_methods:
                graph_methods[self.choice]()
            else:
                print("Invalid option")

            continue_choice = input("Do you want to draw another graph? (yes/no): ").strip().lower()
            if continue_choice != 'yes':
                break

            self.display_options()

    def get_user_colour_choice(self):
        print("Provide a colour you want the line to be, the available colours are:")
        print("(1) Blue")
        print("(2) Orange")
        print("(3) Green")
        print("(4) Black")
        print("(5) Yellow")
        print("(6) Purple")
        print("(7) Red")

        colours = {
            1: 'blue',
            2: 'orange',
            3: 'green',
            4: 'black',
            5: 'yellow',
            6: 'purple',
            7: 'red'
        }

        while True:
            try:
                colour_choice = int(input("Choose a colour: "))
                if colour_choice in colours:
                    return colours[colour_choice]
                else:
                    print("Invalid option. Please choose a number between 1 and 7.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def fetch_data_and_plot(self, indicator_id, title, ylabel):
        query = "SELECT Date, Value FROM EconomicData WHERE IndicatorID = ? ORDER BY Date"
        data = self.db.fetch_data(query, (indicator_id,))

        yearly_data = {}
        for record in data:
            year = record[0][:4]
            value = record[1]
            if year not in yearly_data:
                yearly_data[year] = []
            yearly_data[year].append(value)

        years = sorted(yearly_data.keys())
        avg_values = [sum(values) / len(values) for values in sorted(yearly_data.values())]

        selected_colour = self.get_user_colour_choice()

        plt.figure(figsize=(10, 6))

        # Line Graph
        plt.plot(years, avg_values, marker='o', linestyle='-', color=selected_colour, label=f'{title} (Line)')

        # Bar Graph
        plt.bar(years, avg_values, color=selected_colour, alpha=0.6, label=f'{title} (Bar)')

        plt.xlabel('Year')
        plt.ylabel(ylabel)
        plt.title(title)
        plt.legend()
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    def gdp(self):
        self.fetch_data_and_plot(1, 'GDP Over Time', 'GDP')

    def unemployment_rate(self):
        self.fetch_data_and_plot(2, 'Unemployment Rate Over Time', 'Unemployment Rate (%)')

    def inflation_rate(self):
        self.fetch_data_and_plot(3, 'Inflation Rate Over Time', 'Inflation Rate (%)')

    def gdp_per_cap(self):
        self.fetch_data_and_plot(4, 'GDP per Capita Over Time', 'GDP per Capita')

    def demand_supply_curves(self):
        quantities = np.linspace(1, 100, 100)
        demand = 150 - 2 * quantities #Demand
        supply = 20 + 1.5 * quantities #Supply

        #Finding equilibrium (intersection)
        equilibrium_idx = np.argwhere(np.isclose(demand, supply, atol=0.5)).flatten()
        equilibrium_quantity = quantities[equilibrium_idx[0]]
        equilibrium_price = demand[equilibrium_idx[0]]

        # Get user's colour choice for demand
        demand_color = self.get_user_colour_choice()
        
        # Get user's colour choice for supply
        supply_color = self.get_user_colour_choice()
        
        plt.plot(quantities, demand, label="Demand Curve", color=demand_color)
        plt.plot(quantities, supply, label="Supply Curve", color=supply_color)
        plt.plot(equilibrium_quantity, equilibrium_price, 'ro', label="Equilibrium")
        plt.xlabel("Quantity")
        plt.ylabel("Price")
        plt.title("Demand and Supply Curves with Equilibrium")
        plt.legend()
        plt.show()



    def aggdemand_aggsupply_curves(self):
        price_levels = np.linspace(1, 100, 100)
        ad = 300 - 2 * price_levels 
        as_ = 50 + 1.5 * price_levels 

        #Shifting AD and AS for simulation
        ad_shifted = ad - 30  #Example of rightward AD shift (e.g., expansionary policy)
        as_shifted = as_ + 20  #Example of leftward AS shift (e ```python
        #Example of supply shock)

        # Get user's colour choice for AD
        ad_color = self.get_user_colour_choice()
        
        # Get user's colour choice for AS
        as_color = self.get_user_colour_choice()
        
        plt.plot(price_levels, ad, label="Aggregate Demand (AD)", color=ad_color)
        plt.plot(price_levels, as_, label="Aggregate Supply (AS)", color=as_color)
        plt.plot(price_levels, ad_shifted, '--', label="AD Shifted Downward", color=ad_color)
        plt.plot(price_levels, as_shifted, '--', label="AS Shifted Left", color=as_color)
        plt.xlabel("Price Level")
        plt.ylabel("Real GDP")
        plt.title("Aggregate Demand and Aggregate Supply Curves")
        plt.legend()
        plt.show()




    def phillips_curve(self):
        a = 25         # Scaling constant (max inflation)
        b = 1          # Curvature parameter

        # Unemployment range (limits)
        u = np.linspace(1, 11, 500)

        y = a * u**-b
        selected_colour = self.get_user_colour_choice()
        plt.figure(figsize=(8, 6))
        plt.plot(u, y, label='Phillips Curve', color=selected_colour)
        plt.title("The Phillips Curve", fontsize=14)
        plt.xlabel("Unemployment Rate (%)", fontsize=12)
        plt.ylabel("Inflation Rate (%)", fontsize=12)
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.axhline(0, color='black', linewidth=0.8, linestyle='--')  # Mark zero inflation line
        plt.legend()
        plt.ylim(-5, 30)  # Match the y-axis range in the image
        plt.xlim(1, 11) 
        plt.show()

    def price_income_elasticity(self):
        prices = np.linspace(1, 100, 100)
        demand = (150-2) * prices  #Linear demand function Q(P)

        # Define elasticity function using calculus
        def elasticity(p):
            dq_dp = derivative(lambda p: (150-2)*p, p, dx=1e-6)  # Differentiating demand function
            q = (150-2) * p

            if q != 0:
                return (dq_dp * p) / q 
            else:
                return 0

        # Calculate elasticity values
        elasticities = []
        for p in prices:
            elasticities.append(elasticity(p))

        # Get user's colour choice
        selected_colour = self.get_user_coluor_choice()
        
        plt.plot(prices, elasticities, label="Price Elasticity", color=selected_colour)
        plt.xlabel("Price")
        plt.ylabel("Elasticity")
        plt.title("Price Elasticity of Demand")
        plt.legend()
        plt.show()


class UserInput:
    def __init__(self, user_id, indicator_id, custom_value, date):
        self.user_id = user_id
        self.indicator_id = indicator_id
        self.custom_value = custom_value
        self.date = date

    #validate user inputs, is input in range
    def validate_input(self):
        pass

    def draw_own_graph(self):
        pass

class User:
    def __init__(self, user_id, username, email, created_time):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.created_time = created_time


    def register(self):
        pass 


    def login(self):
        pass


class Database:
    def __init__(self, db_path):
        """
        Initialize the Database class.

        :param db_path: Path to the SQLite database file.
        """
        self.db_path = db_path
        self.connection = None
        self.cursor = None

    def connect(self):
        """Connect to the SQLite database."""
        try:
            self.connection = sqlite3.connect(self.db_path)
            self.cursor = self.connection.cursor()
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")

    def close(self):
        """Close the database connection."""
        if self.connection:
            try:
                self.connection.close()
            except sqlite3.Error as e:
                print(f"Error closing the database: {e}")

    def fetch_data(self, query, params=None):
        """
        Fetch data from the database.

        :param query: SQL query to execute.
        :param params: Optional parameters for the query.
        :return: Query results as a list of tuples.
        """
        if not self.connection or not self.cursor:
            print("Database connection is not established. Call connect() first.")
            return []

        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error fetching data: {e}")
            return []

# Usage in the EconomicGraph class remains the same:
# - Create a Database instance
# - Use `db.fetch_data` to get data for plotting graphs


class DataExplanation:
    def __init__(self, explanation_id, graph_id, explanation_text):
        self.explanation_id = explanation_id
        self.graph_id = graph_id
        self.explanation_text = explanation_text

    def generate_explanation(self):
        pass 

if __name__ == "__main__":
    db = Database("economic_data.db")
    db.connect()
    economic_graph = EconomicGraph(db)
    
    while True:
        economic_graph.display_options()
        economic_graph.draw_graph()

        continue_choice = input("Do you want to draw another graph? (yes/no): ").strip().lower()
        if continue_choice != 'yes':
            break