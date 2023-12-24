import csv
import random
import math
from faker import Faker

fake = Faker()


def calculate_pressure(power_rating):
    base_pressure_rating = 80 + power_rating * 2
    variability = random.uniform(-10, 10)
    return max(80, round(base_pressure_rating + variability), round(550 + variability))


def calculate_unit_price(power_rating):
    return int(8000 + power_rating * 300)


def calculate_capacity(power_rating):
    base_capacity = 30 + power_rating * 5
    variability = random.uniform(-50, 50)
    return max(10, round(base_capacity + variability), round(500 + variability))


def calculate_energy_consumption(power_rating, capacity):
    base_consumption = 2.5 + power_rating * 0.1 + capacity * 0.02
    randomness = random.uniform(-10, 10)
    return round(max(1, base_consumption + randomness), 1)


def calculate_energy_efficiency(capacity, energy_consumption):
    efficiency_variation = random.uniform(0.8, 1.2)
    return round(
        min(
            (capacity / energy_consumption) * efficiency_variation,
            0.75 * efficiency_variation,
        ),
        2,
    )


def categorize_product():
    product_category = random.choice(
        [
            "OIL LUBRICATED SCREW AIR COMPRESSORS",
            "OIL LUBRICATED PISTON AIR COMPRESSORS",
        ]
    )

    if product_category == "OIL LUBRICATED SCREW AIR COMPRESSORS":
        product = random.choice(
            [
                {
                    "name": "ELECTRIC LUBRICATED EN SERIES SCREW AIR COMPRESSOR",
                    "power_rating_range": [5, 10, 20, 30, 40, 60],
                },
                {
                    "name": "ELECTRIC LUBRICATED EG SERIES SCREW AIR COMPRESSOR",
                    "power_rating_range": [15, 30, 50, 75, 90, 100],
                },
                {
                    "name": "ELECTRIC LUBRICATED EG SERIES SCREW AIR COMPRESSOR",
                    "power_rating_range": [120, 150, 200, 250, 300, 335],
                },
            ]
        )
        industries = random.choice(
            [
                "Textile",
                "Automotive",
                "Paper",
                "Food Processing",
                "Small Machining",
                "Fabrication Workshops",
            ]
        )
    else:
        product = random.choice(
            [
                {
                    "name": "ALUMINIUM COAXIAL PISTON COMPRESSORS",
                    "power_rating_range": [1, 2, 3],
                },
                {
                    "name": "LD SERIES PISTON COMPRESSOR",
                    "power_rating_range": [5, 7, 10],
                },
                {
                    "name": "HIGH PRESSURE PISTON COMPRESSORS",
                    "power_rating_range": [5, 10, 15, 20],
                },
                {
                    "name": "CUSTOM BUILT COMPRESSORS",
                    "power_rating_range": [20, 50, 100, 150, 250],
                },
            ]
        )
        industries = random.choice(
            [
                "General Engineering",
                "Automotive",
                "Automobile",
                "Textile",
                "Food & Beverages",
                "Paint Shop",
                "Plastic Manufacturing",
                "CNC Operation",
                "Metal Fabrication",
                "Pet Blowing",
                "Engine Starting",
                "Circuit Breakers",
                "Marine",
                "Mining",
                "Diesel Engine Starting",
                "Hydel",
                "Concrete Pumps",
            ]
        )

    if product["power_rating_range"] is not None:
        power_rating = random.choice(product["power_rating_range"])
        pressure_rating = calculate_pressure(power_rating)
        unit_price = calculate_unit_price(power_rating)
        capacity = calculate_capacity(power_rating)
        energy_consumption = calculate_energy_consumption(power_rating, capacity)
        energy_efficiency = calculate_energy_efficiency(capacity, energy_consumption)
    else:
        power_rating = None
        pressure_rating = None
        unit_price = None
        capacity = None
        energy_consumption = None
        energy_efficiency = None

    return (
        product_category,
        product["name"],
        industries,
        power_rating,
        unit_price,
        pressure_rating,
        capacity,
        energy_consumption,
        energy_efficiency,
    )


def generate_data():
    data = []

    for i in range(15000):
        (
            product_category,
            product_name,
            industries,
            power_rating,
            unit_price,
            pressure_rating,
            capacity,
            energy_consumption,
            energy_efficiency,
        ) = categorize_product()

        product_id = i + 1000
        date_of_sale = fake.date_between(start_date="-1y", end_date="today")
        sales_channel = random.choice(
            ["Direct Sales", "Distributor", "Online Platform"]
        )
        sales_region = fake.random_element(
            elements=("East Region", "West Region", "South Region", "North Region")
        )
        quantity_sold = random.randint(1, 10)
        total_sales_revenue = quantity_sold * unit_price
        customer_id = i + 101
        company_name = fake.company()
        contact_person = fake.name()
        contact_email = fake.email()
        contact_phone = fake.phone_number()
        installation_date = fake.date_between(start_date=date_of_sale, end_date="today")
        service_contracts = random.choice(["Yes", "No"])
        maintenance_history = fake.random_element(
            elements=(
                "Regular maintenance every 6 months",
                "Annual service contract",
                "Quarterly Maintenance",
            )
        )
        warranty_information = fake.random_element(
            elements=(
                "1 year warranty",
                "2 years warranty",
                "3 years warranty",
                "5 years warranty",
            )
        )
        operating_cost = round(
            random.uniform(0.9, 1.2)
            * random.uniform(0.65 * unit_price, 0.92 * unit_price),
            2,
        )
        environmental_impact = fake.random_element(
            elements=(
                "Low emissions",
                "Environmentally friendly design",
                "Minimal environmental impact",
            )
        )
        market_trends = fake.random_element(elements=("Stable", "Growing", "Declining"))
        customer_satisfaction_ratings = round(random.uniform(3.5, 5), 1)
        marketing_campaigns = fake.random_element(
            elements=("Email Campaign", "Social Media Ads", "Trade Shows")
        )
        promotional_discounts = fake.random_element(
            elements=(
                "10% off for bulk orders",
                "Free shipping for orders above rs.10,000",
                "15% off for first-time buyers",
            )
        )
        industry_regulations = fake.random_element(
            elements=("No specific regulations", "Compliance with industry standards")
        )

        data.append(
            [
                product_id,
                product_category,
                product_name,
                power_rating,
                capacity,
                pressure_rating,
                date_of_sale,
                sales_channel,
                sales_region,
                unit_price,
                quantity_sold,
                total_sales_revenue,
                customer_id,
                company_name,
                contact_person,
                contact_email,
                contact_phone,
                installation_date,
                service_contracts,
                maintenance_history,
                warranty_information,
                energy_consumption,
                energy_efficiency,
                operating_cost,
                environmental_impact,
                market_trends,
                customer_satisfaction_ratings,
                marketing_campaigns,
                promotional_discounts,
                industry_regulations,
                industries,
            ]
        )

    return data


def save_to_csv(data, filename="air_compressor_sales_data.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        header = [
            "Product_ID",
            "Compressor_Type",
            "Product_Name",
            "Power_Rating(HP)",
            "Capacity(CFM)",
            "Pressure_Rating(PSI)",
            "Date_of_Sale",
            "Sales_Channel",
            "Sales_Region",
            "Unit_Price",
            "Quantity_Sold",
            "Total_Sales_Revenue",
            "Customer_ID",
            "Company_Name",
            "Contact_Person",
            "Contact_Email",
            "Contact_Phone",
            "Installation_Date",
            "Service_Contracts",
            "Maintenance_History",
            "Warranty_Information",
            "Energy_Consumption(kWh)",
            "Energy_Efficiency",
            "Operating_Cost",
            "Environmental_Impact",
            "Market_Trends",
            "Customer_Satisfaction_Ratings",
            "Marketing_Campaigns",
            "Promotional_Discounts",
            "Industry_Regulations",
            "industries",
        ]
        writer.writerow(header)
        writer.writerows(data)


if __name__ == "__main__":
    air_compressor_data = generate_data()
    save_to_csv(air_compressor_data)
