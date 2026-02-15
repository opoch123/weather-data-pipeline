import pandas as pd

# 1. Create some dummy data (Imagine this was a huge CSV file)
data = {
    'city': ['Toronto', 'Miami', 'London', 'Tokyo'],
    'temp_c': [15, 28, 12, 20],
    'humidity': [65, 80, 75, None] # Note the 'None' (Missing data!)
}

df = pd.DataFrame(data)

# 2. Cleaning: Fill missing values with the average humidity
avg_humidity = df['humidity'].mean()
df['humidity'] = df['humidity'].fillna(avg_humidity)

# 3. Transformation: Create a 'is_hot' boolean column
df['is_hot'] = df['temp_c'] > 25

print(df)

# 4. Save to CSV for the next stage of the pipeline
df.to_csv('cleaned_weather.csv', index=False)