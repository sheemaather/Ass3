import numpy as np
import pandas as pd
file_path = "Titanic-Dataset.csv"
# --- 1. Load the data into a Pandas DataFrame ---
df = pd.read_csv('Titanic-Dataset.csv')

# --- 2. Select only the numeric columns ---
# 'number' is a shorthand that includes all int, float, and complex dtypes.
numeric_df = df.select_dtypes(include=['number'])

# --- 3. Convert the resulting numeric DataFrame to a NumPy array ---
data= numeric_df.to_numpy()

#2. Show ArrayProperties
print("Passengers/numerical columns:", data.shape)
print("Data types", data.dtype)
print("Dimenssions of array:", data.ndim)
np.set_printoptions(suppress=True)
#print(data[:10])  # Show first 10 rows
#3. Vectorized Operations
ages = np.genfromtxt(
    file_path,
    delimiter=",",
    skip_header=1,
    max_rows=10,
    usecols=(6,),      # Age column
    dtype=float,
    filling_values=np.nan
)
# Remove NaN values before calculations
ages_clean = ages[~np.isnan(ages)]
print("Mean Of Ages",np.mean(ages_clean))
print("Meadian of it",np.median(ages_clean))
print("Standard Deviation ",np.std(ages_clean))

# 	Element-wise addition/multiplication
#Fare column for the element wise multiplication
fare = np.genfromtxt(
    file_path,
    delimiter=",",
    skip_header=1,
    usecols=(10,),
    max_rows=10,      # Fare column
    dtype=float,
    filling_values=np.nan
)
tax=fare*0.10
print("tax inclusive fare \n",fare+tax)

#4. Demonstrating Indexing
print("Indexing of Elements of an array")
print("Element at Index 1 & 5 ",data[[1,5]])

#4. Demonstrating Slicing 
print(" Slicing of a numpy array")
print("It will show 6 records from the Rec 5 to 11\n",data[4:8])           #It will show 6 records from the Rec 5 to 11
print("It will show 3 records from the Rec 5 and Step 2 Rec till Rec 9\n",data[4:10:2])  

# 4. Create the condition (the Boolean Mask) for bolean filtering
under30 = ages < 30
print(f"\nBoolean Mask where age is less than 30:\n{under30}")

# 4. Filter for passengers between 20 and 40 (inclusive)
# Condition 1: ages >= 20   AND   Condition 2: ages <= 40
Adults = ages[(ages >= 20) & (ages <= 40)]
print(f"\nPassengers between 20 and 40 :\n{Adults}")

#5: Broadcasting
# np.ceil() is broadcast across the entire fares_array
rounded_up_fares = np.floor(data[:, 6])

print("\n--- Rounded Up Fares Array (Using np.ceil) ---")
print(rounded_up_fares)