import pandas as pd


data = [
    ('1989', 5.8), ('1989', 5.8), ('1989', 5.6), ('1989', 5.7),
    ('1990', 6.1), ('1990', 8), ('1990', 8.8), ('1990', 9.2),
    ('1991', 8.4), ('1991', 7.7), ('1991', 7.3), ('1991', 6.5),
    ('1992', 6.3), ('1992', 5), ('1992', 4), ('1992', 3.3),
    ('1993', 3.1), ('1993', 2.3), ('1993', 2.5), ('1993', 2.2),
    ('1994', 2.4), ('1994', 2.4), ('1994', 2.1), ('1994', 2.1),
    ('1995', 2.4), ('1995', 2.5), ('1995', 2.9), ('1995', 3),
    ('1996', 3), ('1996', 2.8), ('1996', 2.7), ('1996', 2.9),
    ('1997', 2.4), ('1997', 2.1), ('1997', 2.3), ('1997', 2.1),
    ('1998', 1.8), ('1998', 2), ('1998', 1.7), ('1998', 1.7),
    ('1999', 2), ('1999', 1.8), ('1999', 1.6), ('1999', 1.5),
    ('2000', 1.1), ('2000', 1), ('2000', 1.2), ('2000', 1.4),
    ('2001', 1.3), ('2001', 1.8), ('2001', 1.8), ('2001', 1.4),
    ('2002', 1.7), ('2002', 1.3), ('2002', 1.3), ('2002', 1.6),
    ('2003', 1.5), ('2003', 1.3), ('2003', 1.4), ('2003', 1.3),
    ('2004', 1.3), ('2004', 1.3), ('2004', 1.3), ('2004', 1.5),
    ('2005', 1.8), ('2005', 1.9), ('2005', 2.4), ('2005', 2.2),
    ('2006', 2.1), ('2006', 2.4), ('2006', 2.5), ('2006', 2.7),
    ('2007', 2.8), ('2007', 2.6), ('2007', 2), ('2007', 2.3),
    ('2008', 2.5), ('2008', 3.3), ('2008', 4.5), ('2008', 3.7),
    ('2009', 2.9), ('2009', 2), ('2009', 1.4), ('2009', 1.6),
    ('2010', 2.4), ('2010', 2.5), ('2010', 2.3), ('2010', 2.7),
    ('2011', 3.5), ('2011', 3.8), ('2011', 4), ('2011', 4),
    ('2012', 3.1), ('2012', 2.5), ('2012', 2.2), ('2012', 2.4),
    ('2013', 2.5), ('2013', 2.4), ('2013', 2.4), ('2013', 1.9),
    ('2014', 1.6), ('2014', 1.6), ('2014', 1.5), ('2014', 1.1),
    ('2015', 0.4), ('2015', 0.3), ('2015', 0.4), ('2015', 0.4),
    ('2016', 0.7), ('2016', 0.7), ('2016', 1), ('2016', 1.5),
    ('2017', 2.2), ('2017', 2.6), ('2017', 2.7), ('2017', 2.8),
    ('2018', 2.5), ('2018', 2.2), ('2018', 2.3), ('2018', 2.1),
    ('2019', 1.8), ('2019', 2), ('2019', 1.8), ('2019', 1.4),
    ('2020', 1.7), ('2020', 0.8), ('2020', 0.8), ('2020', 0.8),
    ('2021', 0.9), ('2021', 2.1), ('2021', 2.7), ('2021', 4.4),
    ('2022', 5.5), ('2022', 7.9), ('2022', 8.7), ('2022', 9.4),
    ('2023', 9), ('2023', 7.7), ('2023', 6.3), ('2023', 4.4),
    ('2024', 3.9), ('2024', 2.9), ('2024', 2.9)
]

# Convert the data into a DataFrame
df = pd.DataFrame(data, columns=["Year", "GDP"])

# Save the DataFrame to an Excel file without the header
df.to_excel("cleaned_gdp_per_cap.xlsx", index=False, header=False)
