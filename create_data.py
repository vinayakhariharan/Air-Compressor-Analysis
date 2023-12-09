import csv
import random
import math
from faker import Faker

fake = Faker()

def categorize_product():
    product_category = random.choice(['OIL LUBRICATED SCREW AIR COMPRESSORS', 'OIL LUBRICATED PISTON AIR COMPRESSORS'])
    
    if product_category == 'OIL LUBRICATED SCREW AIR COMPRESSORS':
        product = random.choice([
            {'name': 'ELECTRIC LUBRICATED EN SERIES SCREW AIR COMPRESSOR', 'power_rating_range': (3, 60), 'price_range': (10000, 20000), 'pressure_range': (100, 175), 'capacity_range': (10, 300), 'consumption_range': (2.5, 50)},
            {'name': 'ELECTRIC LUBRICATED EG SERIES SCREW AIR COMPRESSOR', 'power_rating_range': (15, 100), 'price_range': (15000, 25000), 'pressure_range': (100, 200), 'capacity_range': (30, 500), 'consumption_range': (40, 75)},
            {'name': 'ELECTRIC LUBRICATED EG SERIES SCREW AIR COMPRESSOR', 'power_rating_range': (120, 335),'price_range': (30000, 100000), 'pressure_range': (125, 250), 'capacity_range': (400, 1200), 'consumption_range': (70, 250)}
        ])
        industries = random.choice([
            'Textile', 'Automotive', 'Paper', 'Food Processing', 'Small Machining', 'Fabrication Workshops'
        ])
    else:
        product = random.choice([
            {'name': 'ALUMINIUM COAXIAL PISTON COMPRESSORS', 'power_rating_range': (1, 3), 'price_range': (8000, 12000), 'pressure_range': (90, 125),'capacity_range': (1, 15), 'consumption_range': (0.5, 3)},
            {'name': 'LD SERIES PISTON COMPRESSOR', 'power_rating_range': (3, 10),'price_range': (12000, 15000), 'pressure_range': (90, 150),'capacity_range': (10, 20), 'consumption_range': (2.5, 7)},
            {'name': 'HIGH PRESSURE PISTON COMPRESSORS', 'power_rating_range': (3, 20),'price_range': (10000, 20000), 'pressure_range': (90, 200),'capacity_range': (10, 30), 'consumption_range': (2.5, 8)},
            {'name': 'CUSTOM BUILT COMPRESSORS', 'power_rating_range': (3, 250),'price_range': (10000, 150000), 'pressure_range': (90, 300),'capacity_range': (10, 1500), 'consumption_range': (2.5, 110)}  
        ])
        industries = random.choice([
            'General Engineering', 'Automotive', 'Automobile', 'Textile', 'Food & Beverages', 'Paint Shot',
            'Plastic Manufacturing', 'CNC Operation', 'Metal Fabrication', 'Pet Blowing', 'Engine Starting',
            'Circuit Breakers', 'Marine', 'Mining', 'Diesel Engine Starting', 'Hydel', 'Concrete Pumps'
        ])

    if product['power_rating_range'] is not None:
        power_rating = random.randint(product['power_rating_range'][0], product['power_rating_range'][1])
    else:
        power_rating = None

    if product['price_range'] is not None:
        unit_price = random.randint(product['price_range'][0], product['price_range'][1])
    else:
        unit_price = None

    if product['pressure_range'] is not None:
        pressure_rating = random.randint(product['pressure_range'][0], product['pressure_range'][1])
    else:
        pressure_rating = None

    if product['capacity_range'] is not None:
        capacity = random.randint(product['capacity_range'][0], product['capacity_range'][1])
    else:
        capacity = None

    if product['consumption_range'] is not None:
        energy_consumption = round(random.uniform(product['consumption_range'][0], product['consumption_range'][1]),1)
    else:
        energy_consumption = None

    return product_category, product['name'], industries, power_rating, unit_price, pressure_rating, capacity, energy_consumption

def generate_data():
    
    data = []

    for i in range(1000):

        product_category, product_name, industries, power_rating, unit_price, pressure_rating, capacity, energy_consumption = categorize_product()

        product_id = i + 1000
        date_of_sale = fake.date_between(start_date='-1y', end_date='today')
        sales_channel = random.choice(['Direct Sales', 'Distributor', 'Online Platform'])
        sales_region = fake.random_element(elements=('East Region', 'West Region', 'South Region', 'North Region'))
        quantity_sold = random.randint(1, 10)
        total_sales_revenue = quantity_sold * unit_price 
        customer_id = i + 101
        company_name = fake.company()
        contact_person = fake.name()
        contact_email = fake.email()
        contact_phone = fake.phone_number()
        installation_date = fake.date_between(start_date=date_of_sale, end_date='today')
        service_contracts = random.choice(['Yes', 'No'])
        maintenance_history = fake.random_element(elements=('Regular maintenance every 6 months', 'Annual service contract', 'Quarterly Maintenance'))
        warranty_information = fake.random_element(elements=('1 year warranty', '2 years warranty', '3 years warranty', '5 years warranty'))
        efficiency_rating = round(random.uniform(70, 95),2)
        operating_cost = round(random.uniform(0.5* unit_price, 0.8 * unit_price),2)
        environmental_impact = fake.random_element(elements=('Low emissions', 'Environmentally friendly design', 'Minimal environmental impact'))
        market_trends = fake.random_element(elements=('Stable', 'Growing', 'Declining'))
        customer_satisfaction_ratings = round(random.uniform(3.5, 5),1)
        marketing_campaigns = fake.random_element(elements=('Email Campaign', 'Online Ads', 'Trade Shows'))
        promotional_discounts = fake.random_element(elements=('10% off for bulk orders', 'Free shipping for orders above $10,000', '15% off for first-time buyers'))
        advertising_channels = fake.random_element(elements=('Industry magazines', 'Social media campaigns', 'Mobile app for remote monitoring'))
        industry_regulations = fake.random_element(elements=('No specific regulations', 'Compliance with industry standards'))

        data.append([
            product_id, product_category, product_name, power_rating, capacity, pressure_rating,
            date_of_sale, sales_channel, sales_region, unit_price, quantity_sold, total_sales_revenue, 
            customer_id, company_name, contact_person, contact_email, contact_phone,
            installation_date, service_contracts, maintenance_history, warranty_information,
            energy_consumption, efficiency_rating, operating_cost, environmental_impact,
            market_trends, customer_satisfaction_ratings, marketing_campaigns, promotional_discounts, advertising_channels,
            industry_regulations, industries
        ])

    return data

def save_to_csv(data, filename='air_compressor_sales_data_with_nan.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        header = [
            'Product_ID', 'Compressor_Type', 'Product_Name', 'Power_Rating(HP)', 'Capacity(CFM)', 'Pressure_Rating(PSI)',
            'Date_of_Sale', 'Sales_Channel', 'Sales_Region', 'Unit_Price', 'Quantity_Sold', 'Total_Sales_Revenue', 
            'Customer_ID', 'Company_Name', 'Contact_Person', 'Contact_Email', 'Contact_Phone',
            'Installation_Date', 'Service_Contracts', 'Maintenance_History', 'Warranty_Information',
            'Energy_Consumption(kWh)', 'Efficiency_Rating(%)', 'Operating_Cost', 'Environmental_Impact',
            'Market_Trends',  'Customer_Satisfaction_Ratings', 'Marketing_Campaigns', 'Promotional_Discounts', 'Advertising_Channels',
            'Industry_Regulations',  'industries'
        ]
        writer.writerow(header)
        writer.writerows(data)

if __name__ == '__main__':
    air_compressor_data = generate_data()
    save_to_csv(air_compressor_data)