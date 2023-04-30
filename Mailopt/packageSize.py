import pandas as pd

# Load the Excel file into a pandas DataFrame
f = pd.read_excel('North_Campus_Only.xlsx')

# Create a dictionary to store the package counts
package_counts = {
    'E': 0,
    'E-XL': 0,
    'E-SM': 0,
    'S': 0,
    'PR': 0,
    'PR-BIG': 0,
    'BR': 0,
    'BR-E': 0,
    'P': 0,
    'T': 0,
    'LG': 0,
    'L': 0,
    'F': 0,
    'M': 0,
    'M-XL': 0,
}
ans=0
# Loop through the 'Package Size' column in the DataFrame
for package_size in f['Description 4']:
    if package_size.upper() in package_counts:
        package_counts[package_size.upper()] += 1
        ans+=1

# Print the package counts
print(package_counts)
print(ans)

