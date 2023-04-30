import pandas as pd

# Load the Excel file into a pandas DataFrame
f = pd.read_excel('North_Campus_Only.xlsx')

# Create a dictionary to store the package counts
package_status = {
    'Issued': 0,
    'Forwarded': 0,
    'Returned': 0,
    'Received': 0,
}


# Loop through the 'Parcel Status Description 2' column in the DataFrame
for package_type in f['Parcel Status Description 2']:
    if package_type in package_status:
        package_status[package_type] += 1

# Print the package counts
print(package_status)
