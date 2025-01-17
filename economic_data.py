import sqlite3
import pandas as pd

#Define connection and cursor
connection = sqlite3.connect("economic_data.db")
cursor = connection.cursor()

#Create Indicators table
command1 = """
CREATE TABLE IF NOT EXISTS Indicators (
    IndicatorID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL
);
"""
cursor.execute(command1)

# cursor.execute("DELETE FROM Indicators")
# cursor.execute("INSERT INTO Indicators VALUES (1, 'GDP')")
# cursor.execute("INSERT INTO Indicators VALUES (2, 'Unemployment Rate')")
# cursor.execute("INSERT INTO Indicators VALUES (3, 'Inflation Rate')")

cursor.execute("SELECT * FROM Indicators")
results = cursor.fetchall()
print(results)

#Create Users table
command2 = """
CREATE TABLE IF NOT EXISTS Users (
    UserID INTEGER PRIMARY KEY AUTOINCREMENT,
    Username TEXT NOT NULL,
    Email TEXT NOT NULL UNIQUE
);
"""
cursor.execute(command2)

#Create EconomicData table
command3 = """
CREATE TABLE IF NOT EXISTS EconomicData (
    DataID INTEGER PRIMARY KEY AUTOINCREMENT,
    IndicatorID INTEGER NOT NULL,
    Date DATE NOT NULL,
    Value DECIMAL(15, 2) NOT NULL,
    FOREIGN KEY (IndicatorID) REFERENCES Indicators(IndicatorID)
);
"""
cursor.execute(command3)

#Create UserInputs table
command4 = """
CREATE TABLE IF NOT EXISTS UserInputs (
    InputID INTEGER PRIMARY KEY AUTOINCREMENT,
    UserID INTEGER NOT NULL,
    IndicatorID INTEGER NOT NULL,
    CustomValue DECIMAL(15, 2) NOT NULL,
    InputDate DATE NOT NULL,
    FOREIGN KEY (UserID) REFERENCES Users(UserID),
    FOREIGN KEY (IndicatorID) REFERENCES Indicators(IndicatorID)
);
"""
cursor.execute(command4)

#Create Graphs table
command5 = """
CREATE TABLE IF NOT EXISTS Graphs (
    GraphID INTEGER PRIMARY KEY AUTOINCREMENT,
    UserID INTEGER NOT NULL,
    IndicatorID INTEGER NOT NULL,
    GraphType TEXT NOT NULL,
    Parameters TEXT,
    CreateTime DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (UserID) REFERENCES Users(UserID),
    FOREIGN KEY (IndicatorID) REFERENCES Indicators(IndicatorID)
);
"""
cursor.execute(command5)

#Commit changes and close connection
connection.commit()
connection.close()
