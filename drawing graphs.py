from scipy.misc import derivative
import matplotlib.pyplot as plt
import numpy as np
import time

class EconomicGraph:
    def __init__(self):
        self.choice = None

    def display_options(self):
        print("Which graph would you like to draw and take information from:")
        time.sleep(1)
        print("Option (1): GDP")
        print("Option (2): Inflation Rate")
        print("Option (3): Exchange Rate")
        print("Option (4): GDP per capita")
        print("Option (5): Unemployment Rate")
        print("Option (6): Demand/Supply Curves")
        print("Option (7): Aggregate Demand and Aggregate Supply")
        print("Option (8): Phillips Curve")
        print("Option (9): Price and Income Elasticity")
        print(" ")
        self.choice = input("Pick your option: \n")

    def draw_graph(self):
        while True:
            graph_methods = {
                '1': self.gdp,
                '2': self.inflation_rate,
                '3': self.exchange_rate,
                '4': self.gdp_per_cap,
                '5': self.unemployment_rate,
                '6': self.demand_supply_curves,
                '7': self.aggdemand_aggsupply_curves,
                '8': self.phillips_curve,
                '9': self.price_income_elasticity
            }

            if self.choice in graph_methods:
                graph_methods[self.choice]()
            else:
                print("Invalid option")

            # Ask the user if they want to continue
            continue_choice = input("Do you want to draw another graph? (yes/no): ").strip().lower()
            if continue_choice != 'yes':
                break

            # Display options again for the next choice
            self.display_options()

    def get_user_color_choice(self):
        """
        Prompts the user to select a color and returns the corresponding color code.
        """
        # Display colour options
        print("Provide a colour you want the line to be, the available colours are:")
        print("(1) Blue")
        print("(2) Orange")
        print("(3) Green")
        print("(4) Black")
        print("(5) Yellow")
        print("(6) Purple")
        print("(7) Red")
        
        # Define color mapping
        colours = {
            1: 'blue',
            2: 'orange',
            3: 'green',
            4: 'black',
            5: 'yellow',
            6: 'purple',
            7: 'red'
        }
        
        # Get user input for colour choice
        while True:
            try:
                colour_choice = int(input("Choose a colour: "))
                if colour_choice in colours:
                    return colours[colour_choice]  # Return the selected color
                else:
                    print("Invalid option. Please choose a number between 1 and 6.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def gdp(self):
        years = np.arange(2000, 2024)
        gdp_values = np.random.uniform(1.0, 3.0, len(years)) * 1000  # Once real GDP data is found, replace this
        
        # Get user's colour choice
        selected_color = self.get_user_color_choice()
        
        # Plot the GDP graph
        plt.plot(years, gdp_values, label="GDP (in billions)", color=selected_color)
        plt.xlabel("Year")
        plt.ylabel("GDP")
        plt.title("Gross Domestic Product over Time")
        plt.legend()
        plt.show()


    def inflation_rate(self):
        years = np.arange(2000, 2024)
        inflation = np.random.uniform(0, 10, len(years))

        def find_peak(data, i=0, max_value=0):
            if i == len(data): return max_value
            return find_peak(data, i + 1, max(data[i], max_value))

        peak_inflation = find_peak(inflation)
        
        # Get user's colour choice
        selected_color = self.get_user_color_choice()
        
        plt.plot(years, inflation, label="Inflation Rate", color=selected_color)
        plt.axhline(peak_inflation, linestyle='--', color='red', label="Peak Inflation")
        plt.xlabel("Year")
        plt.ylabel("Inflation Rate (%)")
        plt.title("Inflation Rate Over Time")
        plt.legend()
        plt.show()



    def exchange_rate(self):
        years = np.arange(2000, 2024)
        exchange_rates = { 'USD': np.random.uniform(1.0, 1.5, len(years)),
                        'EUR': np.random.uniform(0.8, 1.2, len(years)) }

        # Get user's colour choice for USD
        usd_color = self.get_user_color_choice()
        
        # Get user's colour choice for EUR
        eur_color = self.get_user_color_choice()
        
        plt.plot(years, exchange_rates['USD'], label="GBP to USD", color=usd_color)
        plt.plot(years, exchange_rates['EUR'], label="GBP to EUR", color=eur_color)
        plt.xlabel("Year")
        plt.ylabel("Exchange Rate")
        plt.title("Exchange Rates Over Time")
        plt.legend()
        plt.show()


    def gdp_per_cap(self):
        years = np.arange(2000, 2024)
        gdp_per_cap = np.random.uniform(20000, 50000, len(years))

        # Get user's colour choice
        selected_color = self.get_user_color_choice()
        
        plt.plot(years, gdp_per_cap, label="GDP per Capita", color=selected_color)
        plt.xlabel("Year")
        plt.ylabel("GDP per Capita (USD)")
        plt.title("GDP per Capita over Time")
        plt.legend()
        plt.show()


    def unemployment_rate(self):
        years = np.arange(2000, 2024)
        unemployment = np.random.uniform(3, 10, len(years))

        # Get user's colour choice
        selected_color = self.get_user_color_choice()
        
        plt.plot(years, unemployment, label="Unemployment Rate", color=selected_color)
        plt.xlabel("Year")
        plt.ylabel("Unemployment Rate (%)")
        plt.title("Unemployment Rate over Time")
        plt.legend()
        plt.show()


    def demand_supply_curves(self):
        quantities = np.linspace(1, 100, 100)
        demand = 150 - 2 * quantities #Demand
        supply = 20 + 1.5 * quantities #Supply

        #Finding equilibrium (intersection)
        equilibrium_idx = np.argwhere(np.isclose(demand, supply, atol=0.5)).flatten()
        equilibrium_quantity = quantities[equilibrium_idx[0]]
        equilibrium_price = demand[equilibrium_idx[0]]

        # Get user's colour choice for demand
        demand_color = self.get_user_color_choice()
        
        # Get user's colour choice for supply
        supply_color = self.get_user_color_choice()
        
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
        ad_color = self.get_user_color_choice()
        
        # Get user's colour choice for AS
        as_color = self.get_user_color_choice()
        
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
        selected_colour = self.get_user_color_choice()
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
        selected_color = self.get_user_color_choice()
        
        plt.plot(prices, elasticities, label="Price Elasticity", color=selected_color)
        plt.xlabel("Price")
        plt.ylabel("Elasticity")
        plt.title("Price Elasticity of Demand")
        plt.legend()
        plt.show()



class EconomicIndicator:
    def __init__(self, indicator_id, name, description, data_source, update_freq):
        self.indicator_id = indicator_id
        self.name = name
        self.description = description
        self.data_source = data_source
        self.update_freq = update_freq

    def retrieve_data(self):
        pass

    def clean_data(self, raw_data):
        pass

class EconomicData:
    def __init__(self, data_id, indicator_id, date, value):
        self.data_id = data_id
        self.indicator_id = indicator_id
        self.date = date
        self.value = value

    def save_data(self):#will be used to insert data to database
        pass  

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

class RealTimeData:
    def __init__(self, api_url):
        self.api_url = api_url


    def fetch_real_time_data(self):
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
    pass #fetch data from the database for use
#save user and graph data

class DataExplanation:
    def __init__(self, explanation_id, graph_id, explanation_text):
        self.explanation_id = explanation_id
        self.graph_id = graph_id
        self.explanation_text = explanation_text

    def generate_explanation(self):
        pass 

if __name__ == "__main__":
    economic_graph = EconomicGraph()
    
    while True:
        economic_graph.display_options()
        economic_graph.draw_graph()
        
        #Ask the user if they want to continue
        continue_choice = input("Do you want to draw another graph? (yes/no): ").strip().lower()
        if continue_choice != 'yes':
            break