import pandas as pd
import openpyxl

# Load the datasets
city_regions = pd.read_excel('city_regions.xlsx')
county_to_gea = pd.read_csv('county_to_gea_mapping_cambium23.csv')

# Print column names to debug
print("City Regions Columns: ", city_regions.columns)
print("County to GEA Columns: ", county_to_gea.columns)

# Create a combined 'County, State' column in county_to_gea for merging
county_to_gea['CountyState'] = county_to_gea['County'] + ' County, ' + county_to_gea['State']

# Merge the datasets on the county columns
city_regions_merged = city_regions.merge(county_to_gea, left_on='County', right_on='CountyState', how='left')

# Update the "GEA Region" column in the city_regions dataset
city_regions_merged['GEA Region'] = city_regions_merged['Cambium GEA']

# Select the relevant columns to keep (adjust the column names as necessary)
columns_to_keep = ['EPW', 'County', 'Region', 'IECC Climate Zone', 'County Population', 'Regional Population Weight', 'GEA Region']
city_regions_updated = city_regions_merged[columns_to_keep]

# If needed, rename any columns to their original names
city_regions_updated = city_regions_updated.rename(columns={'County_x': 'County'})

# Display the updated dataset
print(city_regions_updated.head())

city_regions_updated.to_excel('updated_city_regions.xlsx', index=False)