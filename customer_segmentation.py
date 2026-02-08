# Gaming Customer Segmentation Project
# Rule-Based Classification for Revenue Prediction

"""
PROJECT GOAL:
A gaming company wants to create customer personas based on demographics
and predict how much revenue new customers will bring.

For example: How much will a 25-year-old Turkish male iOS user spend?
"""

#############################################
# DATASET INFORMATION
#############################################
"""
persona.csv contains:
- PRICE: Customer spending amount
- SOURCE: Device type (android/ios)
- SEX: Customer gender (male/female)
- COUNTRY: Customer country (usa/bra/deu/tur/fra/can)
- AGE: Customer age (15-66)

NOTE: Same customer can appear multiple times (multiple purchases)
"""

#############################################
# IMPORT LIBRARIES
#############################################
import pandas as pd
import numpy as np

# Display settings for better readability
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)
pd.set_option('display.float_format', lambda x: '%.2f' % x)


#############################################
# TASK 1: EXPLORATORY DATA ANALYSIS
#############################################
print("="*60)
print("TASK 1: EXPLORATORY DATA ANALYSIS")
print("="*60)

# Question 1: Read persona.csv and show general information
print("\n--- Question 1: General Information ---")
df = pd.read_csv('persona.csv')

print("\nFirst 5 rows:")
print(df.head())

print(f"\nDataset shape: {df.shape}")
print(f"Total rows: {df.shape[0]}")
print(f"Total columns: {df.shape[1]}")

print("\nDataset info:")
print(df.info())

print("\nStatistical summary:")
print(df.describe().T)

# FINDING: 5,000 transactions, no missing values, prices range from $9-59

# Question 2: How many unique SOURCE? What are their frequencies?
print("\n--- Question 2: Unique SOURCE ---")
print(f"Number of unique platforms: {df['SOURCE'].nunique()}")
print("\nPlatform frequencies:")
print(df['SOURCE'].value_counts())
print("\nPlatform percentages:")
print(df['SOURCE'].value_counts(normalize=True) * 100)

# FINDING: Android 59.5%, iOS 40.5%
# More balanced than expected

# Question 3: How many unique PRICE values?
print("\n--- Question 3: Unique PRICE ---")
print(f"Number of unique prices: {df['PRICE'].nunique()}")
print(f"Unique prices: {sorted(df['PRICE'].unique())}")

# FINDING: 6 price points (9, 19, 29, 39, 49, 59)

# Question 4: How many sales from each PRICE?
print("\n--- Question 4: Sales by PRICE ---")
print(df['PRICE'].value_counts().sort_index())

# FINDING: $29 is most popular with 1,305 sales

# Question 5: How many sales from each country?
print("\n--- Question 5: Sales by Country ---")
print(df['COUNTRY'].value_counts())
print("\nCountry percentages:")
print((df['COUNTRY'].value_counts() / len(df) * 100).round(2))

# FINDING: USA leads with 41.3%, followed by Brazil 29.9%

# Question 6: Total revenue from each country?
print("\n--- Question 6: Total Revenue by Country ---")
country_revenue = df.groupby("COUNTRY")["PRICE"].sum().sort_values(ascending=False)
print(country_revenue)

# Alternative methods:
# Method 2: Using agg
# df.groupby("COUNTRY").agg({"PRICE": "sum"})


# FINDING: USA generates $70,225 total revenue (highest)

# Question 7: Sales numbers by SOURCE type?
print("\n--- Question 7: Sales by Platform ---")
print(df["SOURCE"].value_counts())

# FINDING: Android 2,974 (59.5%), iOS 2,026 (40.5%)

# Question 8: Average PRICE by country?
print("\n--- Question 8: Average Price by Country ---")
avg_by_country = df.groupby("COUNTRY").agg({"PRICE": "mean"}).sort_values("PRICE", ascending=False)
print(avg_by_country)

# FINDING: Turkey highest ($34.79), France lowest ($33.59)
# All countries within $1.20 range - very similar!

# Question 9: Average PRICE by SOURCE?
print("\n--- Question 9: Average Price by Platform ---")
avg_by_source = df.groupby("SOURCE").agg({"PRICE": "mean"}).sort_values("PRICE", ascending=False)
print(avg_by_source)

# Calculate difference
ios_avg = avg_by_source.loc['ios', 'PRICE']
android_avg = avg_by_source.loc['android', 'PRICE']
difference = ios_avg - android_avg
percentage_diff = (difference / android_avg) * 100

print(f"\nDifference: ${abs(difference):.2f} {'more' if difference > 0 else 'less'}")
print(f"Percentage difference: {abs(percentage_diff):.1f}%")

# FINDING: Android $34.17, iOS $34.07
# Platforms are essentially equal in spending (0.3% difference)

# Question 10: Average PRICE in COUNTRY-SOURCE breakdown?
print("\n--- Question 10: Average Price by Country-Platform ---")
country_source_avg = df.groupby(["COUNTRY", 'SOURCE']).agg({"PRICE": "mean"})
print(country_source_avg)

print("\nPivot table format:")
pivot = df.pivot_table(values='PRICE', index='COUNTRY', columns='SOURCE', aggfunc='mean')
print(pivot)

# FINDING: Platform preference varies by country - no consistent pattern
# Turkey: Android higher ($36.23 vs $33.27)
# France: Android higher ($34.31 vs $32.78)
# USA: iOS higher ($34.37 vs $33.76)


#############################################
# TASK 2: GROUP BY ALL DEMOGRAPHICS
#############################################
print("\n" + "="*60)
print("TASK 2: AVERAGE REVENUE BY CUSTOMER SEGMENTS")
print("="*60)

# Calculate average revenue for each demographic combination
agg_df = df.groupby(["COUNTRY", 'SOURCE', "SEX", "AGE"]).agg({"PRICE": "mean"})
print("\nFirst 10 customer segments:")
print(agg_df.head(10))

# FINDING: We now have average spending for each unique demographic combination


#############################################
# TASK 3: SORT BY PRICE
#############################################
print("\n" + "="*60)
print("TASK 3: SORT BY PRICE")
print("="*60)

# Sort to see highest and lowest spending segments
agg_df = agg_df.sort_values("PRICE", ascending=False)

print("\nTop 10 highest spending segments:")
print(agg_df.head(10))

print("\nBottom 10 lowest spending segments:")
print(agg_df.tail(10))

# FINDING: We can identify which demographics spend most/least


#############################################
# TASK 4: CONVERT INDEX TO COLUMNS
#############################################
print("\n" + "="*60)
print("TASK 4: RESET INDEX")
print("="*60)

# Index names need to become regular columns for easier manipulation
agg_df = agg_df.reset_index()

print("\nData structure after reset_index:")
print(agg_df.head())
print(f"\nNew shape: {agg_df.shape}")

# FINDING: Now all variables are regular columns, easier to work with


#############################################
# TASK 5: CREATE AGE CATEGORIES
#############################################
print("\n" + "="*60)
print("TASK 5: AGE CATEGORIZATION")
print("="*60)

# Check age range first
print(f"Age range: {agg_df['AGE'].min()} to {agg_df['AGE'].max()}")

# Define age bins and labels
bins = [0, 18, 23, 30, 40, agg_df["AGE"].max()]
labels = ['0_18', '19_23', '24_30', '31_40', '41_' + str(int(agg_df["AGE"].max()))]

print(f"\nAge bins: {bins}")
print(f"Age labels: {labels}")

# Create age categories
agg_df["age_cat"] = pd.cut(agg_df["AGE"], bins=bins, labels=labels)

print("\nSample with age categories:")
print(agg_df[['COUNTRY', 'SOURCE', 'SEX', 'AGE', 'age_cat', 'PRICE']].head(10))

print("\nAge category distribution:")
print(agg_df['age_cat'].value_counts().sort_index())

# Analyze spending by age group (using original data)
print("\n--- Spending Analysis by Age Group ---")
df_temp = df.copy()
df_temp['age_cat'] = pd.cut(df_temp['AGE'], bins=bins, labels=labels)
age_analysis = df_temp.groupby('age_cat')['PRICE'].agg(['mean', 'count']).sort_values('mean', ascending=False)
print(age_analysis)

# FINDING: Age 41-66 spends most ($34.48), followed by 0-18 ($34.34)
# Surprising: Older customers are top spenders!
# 31-40 age group spends least ($33.51)


#############################################
# TASK 6: CREATE CUSTOMER PERSONAS
#############################################
print("\n" + "="*60)
print("TASK 6: CREATE CUSTOMER PERSONAS")
print("="*60)

# Combine demographics into unique persona codes
# Method 1: Using list comprehension with .values
agg_df['customers_level_based'] = [
    '_'.join([str(val) for val in row]).upper() 
    for row in agg_df[['COUNTRY', 'SOURCE', 'SEX', 'age_cat']].values
]

# Alternative Method 2: Using agg with lambda
# agg_df['customers_level_based'] = agg_df[['COUNTRY', 'SOURCE', 'SEX', 'age_cat']].agg(lambda x: '_'.join(x).upper(), axis=1)

# Alternative Method 3: Using string concatenation
# agg_df['customers_level_based'] = (agg_df['COUNTRY'] + '_' + agg_df['SOURCE'] + '_' + 
#                                     agg_df['SEX'] + '_' + agg_df['age_cat']).str.upper()

print("\nSample personas created:")
print(agg_df[['customers_level_based', 'PRICE']].head(10))

# Check for duplicates
print(f"\nTotal rows before grouping: {len(agg_df)}")
print(f"Unique personas: {agg_df['customers_level_based'].nunique()}")

print("\nSample duplicate check:")
print(agg_df['customers_level_based'].value_counts().head())

# IMPORTANT: Group by persona to remove duplicates and get average
# Keep only necessary columns
agg_df = agg_df[["customers_level_based", "PRICE"]]

# Group by persona and calculate mean price
agg_df = agg_df.groupby("customers_level_based").agg({"PRICE": "mean"})
agg_df = agg_df.reset_index()

print(f"\nFinal persona count: {len(agg_df)}")
print("\nFinal dataset structure:")
print(agg_df.head(10))

# Verify uniqueness
print("\nVerification - each persona should appear once:")
print(f"Unique check: {agg_df['customers_level_based'].value_counts().max()} (should be 1)")

# FINDING: Created 109 unique customer personas


#############################################
# TASK 7: SEGMENT CUSTOMERS BY REVENUE
#############################################
print("\n" + "="*60)
print("TASK 7: REVENUE-BASED SEGMENTATION")
print("="*60)

# Create 4 segments using quartiles (25%, 50%, 75%)
# Segment D = lowest 25%, C = 25-50%, B = 50-75%, A = top 25%
agg_df["SEGMENT"] = pd.qcut(agg_df["PRICE"], q=4, labels=["D", "C", "B", "A"])

print("\nSegmentation complete!")
print("\nSegment distribution:")
print(agg_df['SEGMENT'].value_counts().sort_index())

# Analyze each segment in detail
print("\n--- Detailed Segment Analysis ---")
segment_analysis = agg_df.groupby("SEGMENT", observed=True).agg({
    "PRICE": ["count", "mean", "min", "max", "std"]
}).round(2)
print(segment_analysis)

# Show sample personas from each segment
print("\n--- Sample Personas by Segment ---")
for segment in ['A', 'B', 'C', 'D']:
    print(f"\n{segment} Segment (Top 3):")
    print(agg_df[agg_df['SEGMENT'] == segment][['customers_level_based', 'PRICE', 'SEGMENT']].head(3))

print("\n--- Segment Descriptions ---")
print("""
Segment A (Premium): $36.06 - $45.43, Average: $38.69
→ VIP programs, exclusive content, early access

Segment B (High-Value): $34.10 - $36.00, Average: $35.00
→ Loyalty rewards, upselling campaigns

Segment C (Mid-Value): $32.50 - $34.08, Average: $33.51
→ Email marketing, bundle deals, limited offers

Segment D (Budget): $19.00 - $32.33, Average: $29.21
→ Discounts, flash sales, micro-transactions
""")

# FINDING: 4 clear segments with different revenue levels
# Each segment has ~27 personas (balanced distribution)


#############################################
# TASK 8: PREDICT REVENUE FOR NEW CUSTOMERS
#############################################
print("\n" + "="*60)
print("TASK 8: REVENUE PREDICTION")
print("="*60)

# Example 1: 33-year-old Turkish woman using Android
print("\n--- Example 1: Turkish Android Female, 33 years old ---")
new_user = "TUR_ANDROID_FEMALE_31_40"
result = agg_df[agg_df["customers_level_based"] == new_user]

if len(result) > 0:
    print(f"Persona Code: {new_user}")
    print(f"Expected Revenue: ${result.iloc[0]['PRICE']:.2f}")
    print(f"Segment: {result.iloc[0]['SEGMENT']}")
    
    segment = result.iloc[0]['SEGMENT']
    print("\nMarketing Recommendation:")
    if segment == 'A':
        print("→ Premium customer! Offer VIP treatment and exclusive features.")
    elif segment == 'B':
        print("→ High-value customer! Use upselling campaigns to move to Segment A.")
    elif segment == 'C':
        print("→ Mid-value customer! Focus on engagement with value packages.")
    else:
        print("→ Budget customer! Offer discounts and volume deals.")
else:
    print("Persona not found in database")

# Example 2: 35-year-old French woman using iOS
print("\n--- Example 2: French iOS Female, 35 years old ---")
new_user = "FRA_IOS_FEMALE_31_40"
result = agg_df[agg_df["customers_level_based"] == new_user]

if len(result) > 0:
    print(f"Persona Code: {new_user}")
    print(f"Expected Revenue: ${result.iloc[0]['PRICE']:.2f}")
    print(f"Segment: {result.iloc[0]['SEGMENT']}")
    
    segment = result.iloc[0]['SEGMENT']
    print("\nMarketing Recommendation:")
    if segment == 'A':
        print("→ Premium customer! Offer VIP treatment and exclusive features.")
    elif segment == 'B':
        print("→ High-value customer! Use upselling campaigns to move to Segment A.")
    elif segment == 'C':
        print("→ Mid-value customer! Focus on engagement with value packages.")
    else:
        print("→ Budget customer! Offer discounts and volume deals.")
else:
    print("Persona not found in database")


#############################################
# SAVE RESULTS
#############################################
print("\n" + "="*60)
print("SAVING RESULTS")
print("="*60)

# Save final segmentation results
agg_df.to_csv('customer_segments.csv', index=False)
print("\n✓ Results saved to 'customer_segments.csv'")

print("\n" + "="*60)
print("ANALYSIS COMPLETE!")
print("="*60)

print("""
**KEY FINDINGS:**
1. Platforms are nearly equal: Android $34.17 vs iOS $34.07 (0.3% difference)
2. Age group 41-66 spends most ($34.48 average) - older customers are valuable!
3. Countries show similar spending (all within $1.20)
4. Created 109 unique customer personas
5. 4 segments: A (Premium), B (High-value), C (Mid-value), D (Budget)

BUSINESS IMPACT:
- Better targeting based on customer segments
- Revenue prediction for new users
- Customized marketing strategies per segment
- Improved ROI on marketing spend
""")
