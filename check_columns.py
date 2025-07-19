import pandas as pd

# Load the dataset
df = pd.read_csv("fifa_players.csv")  # Ensure this file exists in the same folder

# Print all column names
print("✅ Columns in the dataset:")
for col in df.columns:
    print(col)

# Optional: check for specific columns you're using in your project
expected_columns = [
    'Acceleration', 'SprintSpeed', 'Finishing', 'ShortPassing', 'Vision',
    'Strength', 'ShotPower', 'Stamina', 'Dribbling', 'BallControl'
]

print("\n🔍 Checking if required columns are present:")
missing_columns = [col for col in expected_columns if col not in df.columns]

if missing_columns:
    print(f"❌ Missing columns: {missing_columns}")
else:
    print("✅ All expected columns are present.")
