import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('TkAgg')  # Tkinter as the backend for interactivity
import matplotlib.pyplot as plt

# Create DataFrame
data = {
    'Car': ['Toyota', 'Honda', 'Ford', 'Chevrolet', 'BMW'],
    'Price': [25000, 30000, 27000, 22000, 40000],
    'Mileage': [40000, 30000, 60000, 50000, 20000]
}
df = pd.DataFrame(data)

# Calculate average price and mileage
avg_price = df['Price'].mean()
avg_mileage = df['Mileage'].mean()

print("Original DataFrame:")
print(df)
print("\nAverage Price:", avg_price)
print("Average Mileage:", avg_mileage)

# Data Visualization
plt.figure(figsize=(10, 5))

# Bar plot for Price
plt.subplot(1, 2, 1)
plt.bar(df['Car'], df['Price'], color='skyblue')
plt.title('Car Prices')
plt.xlabel('Car')
plt.ylabel('Price')

# Bar plot for Mileage
plt.subplot(1, 2, 2)
plt.bar(df['Car'], df['Mileage'], color='salmon')
plt.title('Car Mileage')
plt.xlabel('Car')
plt.ylabel('Mileage')

# Show plots
plt.tight_layout()
plt.show()
