import pandas as pd

# Define the file path (adjust this if your file is in a different location)
file_path = 'stu_ad_rec.csv'

# --- The Core Loading Function ---
try:
    # Use pd.read_csv to load the file into a DataFrame object (df)
    df = pd.read_csv(file_path)

    # --- Verification ---
    print(f"Dataset successfully loaded from: {file_path}")
    print("\nFirst 5 Rows (Head of the DataFrame):")
    # The .head() method provides a neat graphical output of the top 5 rows
    print(df.head())

    print(f"\nDataFrame Shape (Rows, Columns): {df.shape}")
    print("\nColumn Data Types:")
    print(df.dtypes)
except FileNotFoundError:
    print(f"ERROR: The file '{file_path}' was not found.")
    print("Please ensure the CSV file is in the correct directory.")



# ---------------------------------------------------

print("--- 1. Displaying the First 5 Rows (.head()) ---")
df.head()

print("DataFrame Head displayed above/below.")
print("\n" + "="*50 + "\n")

print("--- 2. Displaying Column Summaries (.info()) ---")
df.info()
print("\n" + "="*50 + "\n")

print("--- 3. Displaying Descriptive Statistics (.describe()) ---")
print(df.describe(include='all'))

# The output is a statistical summary table.
print("DataFrame Describe displayed above/below.")



#Remove Duplicates 
duplicate_mask = df.duplicated()
print("\n--- Boolean Mask of Duplicates (Marking the Second Occurrence) ---")
print(df[duplicate_mask])

df_preprocessed=df.drop_duplicates()
cleaned='Ass3cleaned.csv'
df_preprocessed.to_csv(
    cleaned,
    index=False,          # CRUCIAL: Do NOT write the Pandas index (row numbers) as a column in the CSV
    sep=',',              # Specify the delimiter (comma for CSV)
    encoding='utf-8'      # Standard encoding for text files
)
print(f"✅ Preprocessed data successfully saved to: {cleaned}")

# --- 3. Verification  ---
df_verification = pd.read_csv(cleaned)
print("\nVerification (First 3 rows of the NEW file):")
print(df_verification.head(3))

#3.	Handle missing values (drop, fill, or impute).
# 1. Calculate the mean of the column (Pandas automatically ignores NaNs)
mean_score = df['Admission Test Score'].mean()

# 2. Use fillna() to replace all NaN values with the calculated mean
# The inplace=True argument modifies the DataFrame directly
fillingnan=df['Admission Test Score'].fillna(mean_score)
fillingnan.to_csv(
    cleaned,
    index=False,          # CRUCIAL: Do NOT write the Pandas index (row numbers) as a column in the CSV
    sep=',',              # Specify the delimiter (comma for CSV)
    encoding='utf-8'      # Standard encoding for text files
)
# Verification step (optional)
print(df.info())

# Change of data type column age float to numeric
import pandas as pd
import numpy as np

# --- 1. Create a simulated DataFrame where 'Age' is a float (as it often is due to NaNs) ---
"""df = pd.DataFrame({
    'StudentId': [101, 102, 103, 104, 105],
    'Age': [22.0, 38.0, 26.0, 35.0, 42.0], # These are floats
    'Test_Score': [1200, 1550, 1300, 1420, 1600]
})

print("--- Data Types BEFORE Conversion ---")
print(df.dtypes)
print("-" * 30)

# --- 2. The Conversion Step ---"""

# Check for missing values first (Crucial!)
if df['Age'].isnull().any():
    # If any NaN exists, use Int64 (capital I) which can handle NaNs
    df['Age'] = df['Age'].astype('Int64')
    print("WARNING: NaN values were present. Converted to Int64 (Pandas' nullable integer).")
else:
    # If no NaNs exist, convert directly to the standard numpy integer type
    df['Age'] = df['Age'].astype('int64')
    print("SUCCESS: Converted Age to standard int64.")

# --- 3. Verification ---

print("\n--- Data Types AFTER Conversion ---")
print(df.dtypes)
print("\n--- Sample Data Head ---")
print(df.head())
df['Age'].to_csv(
    cleaned,
    index=False,          # CRUCIAL: Do NOT write the Pandas index (row numbers) as a column in the CSV
    sep=',',              # Specify the delimiter (comma for CSV)
    encoding='utf-8'      # Standard encoding for text files
)

# Category conversion

# --- Conversion Step ---
# Use the .astype() method to convert the string column to the category Dtype.
df['Admission Status'] = df['Admission Status'].astype('category')

print("--- Dtypes AFTER Category Conversion ---")
print(df.dtypes)

# Benefit Check:
print(f"\nMemory Usage for 'Status' (Original): {df['Admission Status'].memory_usage(deep=True)} bytes")
# If the column were a long string (object), this saving would be significant.
print(f"Memory Usage for 'Status' (Category): {df['Admission Status'].memory_usage()} bytes")
df['Admission Status'].to_csv(
    cleaned,
    index=False,          # CRUCIAL: Do NOT write the Pandas index (row numbers) as a column in the CSV
    sep=',',              # Specify the delimiter (comma for CSV)
    encoding='utf-8'      # Standard encoding for text files
)