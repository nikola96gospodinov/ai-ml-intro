# Create a simulated weather dataset:
# Generate a 30x4 array representing daily weather data for a month (columns: temperature, humidity, wind speed, precipitation)
# Find the hottest and coldest days
# Calculate the average weather conditions for each measure
# Find all days where it was both hot (above average temperature) and rainy (precipitation > 0)
# Normalize each weather measure to a 0-1 scale

import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

NUM_DAYS = 30
TEMP_MIN = 15
TEMP_MAX = 35
HUMIDITY_MIN = 30
HUMIDITY_MAX = 90
WIND_SPEED_MIN = 0
WIND_SPEED_MAX = 30
PRECIPITATION_MIN = 0
PRECIPITATION_MAX = 20

# Columns: temperature (°C), humidity (%), wind speed (km/h), precipitation (mm)
weather_data = np.zeros((NUM_DAYS, 4))
weather_data[:, 0] = np.random.uniform(TEMP_MIN, TEMP_MAX, NUM_DAYS)  # Temperature between 15-35°C
weather_data[:, 1] = np.random.uniform(HUMIDITY_MIN, HUMIDITY_MAX, NUM_DAYS)  # Humidity between 30-90%
weather_data[:, 2] = np.random.uniform(WIND_SPEED_MIN, WIND_SPEED_MAX, NUM_DAYS)   # Wind speed between 0-30 km/h
weather_data[:, 3] = np.random.uniform(PRECIPITATION_MIN, PRECIPITATION_MAX, NUM_DAYS)   # Precipitation between 0-20 mm

# Hottest day
hottest_temp = np.max(weather_data[:, 0])
hottest_day = np.argmax(weather_data[:, 0]) + 1
print(f"Hottest temp: {hottest_temp}")
print(f"Hottest day: {hottest_day}")

# Coldest day
coldest_temp = np.min(weather_data[:, 0])
coldest_day = np.argmin(weather_data[:, 0]) + 1
print(f"Coldest temp: {coldest_temp}")
print(f"Coldest day: {coldest_day}")

# Avg measures
avg_temp = np.mean(weather_data[:, 0])
print(f"Avg temp: {avg_temp}")
avg_humidity = np.mean(weather_data[:, 1])
print(f"Avg humidity: {avg_humidity}")
avg_wind = np.mean(weather_data[:, 2])
print(f"Avg wind: {avg_wind}")
avg_precipitation = np.mean(weather_data[:, 3])
print(f"Avg precipitation: {avg_precipitation}")

# Hot and rainy days
hot_day_mask = weather_data[:, 0] > avg_temp
rainy_days = weather_data[:, 1] > 0
hot_and_rainy_days = weather_data[:, 0][hot_day_mask & rainy_days]
print(f"Hot and rainy days: {hot_and_rainy_days}")

# Normalised data 0 to 1
normalized_temp = (weather_data[:, 0] - TEMP_MIN) / (TEMP_MAX - TEMP_MIN)
print(f"Normalised temperature: {normalized_temp}")

normalised_humidity = (weather_data[:, 1] - HUMIDITY_MIN) / (HUMIDITY_MAX - HUMIDITY_MIN)
print(f"Normalised humidity: {normalised_humidity}")

normalized_wind_speed = (weather_data[:, 2] - WIND_SPEED_MIN) / (WIND_SPEED_MAX - WIND_SPEED_MIN)
print(f"Normalised wind speed: {normalized_wind_speed}")

normalised_precipitation = (weather_data[:, 3] - PRECIPITATION_MIN) / (PRECIPITATION_MAX - PRECIPITATION_MIN)
print(f"Normalised precipitation: {normalised_precipitation}")

normalised_weather_data = np.zeros((NUM_DAYS, 4))
normalised_weather_data[:, 0] = normalized_temp
normalised_weather_data[:, 1] = normalised_humidity
normalised_weather_data[:, 2] = normalized_wind_speed
normalised_weather_data[:, 3] = normalised_precipitation

# Classify each day into weather categories (e.g., "Hot & Dry", "Cool & Rainy", etc.) based on their normalized values
temp_threshold = 0.5
humidity_threshold = 0.5
wind_speed_threshold = 0.4
precipitation_threshold = 0.3

# Create arrays for each condition
is_hot = normalised_weather_data[:, 0] >= temp_threshold
is_cool = normalised_weather_data[:, 0] < temp_threshold
is_humid = normalised_weather_data[:, 1] >= humidity_threshold
is_dry = normalised_weather_data[:, 1] < humidity_threshold
is_windy = normalised_weather_data[:, 2] >= wind_speed_threshold
is_not_windy = normalised_weather_data[:, 2] < wind_speed_threshold
is_rainy = normalised_weather_data[:, 3] >= precipitation_threshold
is_not_rainy = normalised_weather_data[:, 3] < precipitation_threshold

# Create empty array of strings to store weather categories
weather_categories = np.empty(NUM_DAYS, dtype=object)

# Classify each day
weather_categories[is_hot & is_humid & is_rainy & is_windy] = "Hot & Humid & Rainy & Windy"
weather_categories[is_hot & is_humid & is_rainy & is_not_windy] = "Hot & Humid & Rainy"
weather_categories[is_hot & is_humid & is_not_rainy & is_windy] = "Hot & Humid & Windy"
weather_categories[is_hot & is_humid & is_not_rainy & is_not_windy] = "Hot & Humid"
weather_categories[is_hot & is_dry & is_rainy & is_windy] = "Hot & Rainy & Windy"
weather_categories[is_hot & is_dry & is_rainy & is_not_windy] = "Hot & Rainy"
weather_categories[is_hot & is_dry & is_not_rainy & is_windy] = "Hot & Dry & Windy"
weather_categories[is_hot & is_dry & is_not_rainy & is_not_windy] = "Hot & Dry"
weather_categories[is_cool & is_humid & is_rainy & is_windy] = "Cool & Humid & Rainy & Windy"
weather_categories[is_cool & is_humid & is_rainy & is_not_windy] = "Cool & Humid & Rainy"
weather_categories[is_cool & is_humid & is_not_rainy & is_windy] = "Cool & Humid & Windy"
weather_categories[is_cool & is_humid & is_not_rainy & is_not_windy] = "Cool & Humid"
weather_categories[is_cool & is_dry & is_rainy & is_windy] = "Cool & Rainy & Windy"
weather_categories[is_cool & is_dry & is_rainy & is_not_windy] = "Cool & Rainy"
weather_categories[is_cool & is_dry & is_not_rainy & is_windy] = "Cool & Dry & Windy"
weather_categories[is_cool & is_dry & is_not_rainy & is_not_windy] = "Cool & Dry"

for i in range(1, NUM_DAYS):
    print(f"Day {i+1}: {weather_categories[i]} (Temp: {weather_data[i, 0]:.1f}°C, Humidity: {weather_data[i, 1]:.1f}%, Precip: {weather_data[i, 3]:.1f}mm)")

# Count occurrences of each category
unique_categories, category_counts = np.unique(weather_categories, return_counts=True)
for category, count in zip(unique_categories, category_counts):
    print(f"{category}: {count} days")
