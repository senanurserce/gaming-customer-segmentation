# Gaming Customer Segmentation

**Customer Segmentation and Revenue Prediction for a Gaming Company**

This project uses rule-based classification to predict customer value and create marketing strategies.

---

## About This Project

A gaming company wants to understand their customers better. They need to answer:
- Who are their most valuable customers?
- How much revenue can they expect from new users?
- What marketing strategy should they use for different customer groups?

I analyzed 5,000 transactions and created customer segments to answer these questions.

---

## What I Did

### Analysis Steps:
1. **Explored the data** - Answered 10 questions about customer behavior
2. **Analyzed spending patterns** - Looked at differences by country, platform, gender, and age
3. **Created customer personas** - Combined demographics into 109 unique profiles
4. **Built revenue segments** - Divided customers into 4 groups: A (Premium), B (High-value), C (Mid-value), D (Budget)
5. **Made revenue predictions** - Can now predict spending for new customers

### Business Value:
- Smarter budget allocation for marketing
- Revenue predictions for new users
- Clear understanding of which customer groups are most valuable

---

## Dataset Information

**File:** `persona.csv` (5,000 transactions)

**Variables:**
- **PRICE** - Customer spending amount (\$9 - \$59)
- **SOURCE** - Device type (android or ios)
- **SEX** - Customer gender (male or female)
- **COUNTRY** - Customer country (usa, bra, deu, tur, fra, can)
- **AGE** - Customer age (15 - 66 years)

**Important Note:** The same customer can appear multiple times because they made multiple purchases.

---

## Key Findings

### 1. Platform Comparison: Android vs iOS

**Transaction Volume:**
- Android: 59.5% of all sales (2,974 transactions)
- iOS: 40.5% of all sales (2,026 transactions)

**Average Spending:**
- Android: \$34.17 per transaction
- iOS: \$34.07 per transaction
- Difference: Only 0.3% - almost the same!

**What This Means:**
- Android has more transactions but both platforms spend equally
- No need for different pricing strategies
- Both platforms are equally valuable to the business

**Business Recommendation:**
- Treat both platforms equally in terms of pricing
- Focus on improving user experience for both
- Allocate marketing budget based on user numbers (60% Android, 40% iOS)

---

### 2. Age Group Spending Patterns

**Average Spending by Age:**
- **41-66 years:** \$34.48 (highest spenders!)
- **0-18 years:** \$34.34
- **19-23 years:** \$34.31
- **24-30 years:** \$33.72
- **31-40 years:** \$33.51 (lowest spenders)

**Surprising Discovery:**
- Older customers (41+) spend the most money
- Young users (0-18) spend almost as much as older users
- 31-40 actually spends the least
- All age groups are very similar (within \$1 of each other)

**Business Recommendation:**
- **Don't ignore older customers** - they are your most valuable group
- **Youth market is strong** - invest in features they enjoy
- **Create content for all ages** - everyone spends similarly
- **Research the 31-40 group** - understand why they spend less

---

### 3. Country Analysis

**Average Spending by Country:**
- Turkey (TUR): \$34.79 (highest)
- Brazil (BRA): \$34.33
- Germany (DEU): \$34.03
- USA: \$34.01
- Canada (CAN): \$33.61
- France (FRA): \$33.59 (lowest)

**Transaction Volume by Country:**
- USA: 2,065 sales (41.3%)
- Brazil: 1,496 sales (29.9%)
- Germany: 455 sales (9.1%)
- Turkey: 451 sales (9.0%)
- France: 303 sales (6.1%)
- Canada: 230 sales (4.6%)

**What This Means:**
- All countries spend within \$1.20 of each other
- USA has the most transactions but not the highest average spending
- Turkey shows the highest average despite fewer transactions
- Standard global pricing works well - no major differences between countries

**Business Recommendation:**
- **Keep the same prices globally** - spending patterns are similar
- **Focus on USA and Brazil** for volume (they make up 70% of sales)
- **Turkey is valuable** - good spending despite lower volume

---

### 4. Customer Segments

I created **109 unique customer personas** from all combinations of country, platform, gender, and age groups. Then I divided them into 4 segments based on their spending:

#### Segment A - Premium Customers
- **Price Range:** \$36.06 - \$45.43
- **Average Spending:** \$38.69
- **Number of Personas:** 27
- **Description:** Highest-value customers


---

#### Segment B - High-Value Customers
- **Price Range:** \$34.10 - \$36.00
- **Average Spending:** \$35.00
- **Number of Personas:** 27
- **Description:** Strong spenders with potential to upgrade

---

#### Segment C - Mid-Value Customers
- **Price Range:** \$32.50 - \$34.08
- **Average Spending:** \$33.51
- **Number of Personas:** 27
- **Description:** Regular spenders who need more engagement

---

#### Segment D - Budget Customers
- **Price Range:** \$19.00 - \$32.33
- **Average Spending:** \$29.21
- **Number of Personas:** 28
- **Description:** Price-sensitive users

---

##  How to Use This Project

### Requirements

Install the required libraries:

```bash
pip install pandas numpy matplotlib seaborn jupyter
```

Or use the requirements file:

```bash
pip install -r requirements.txt
```

---

### Run the Analysis

**Option 1: Jupyter Notebook (Recommended for Learning)**

```bash
jupyter notebook analysis.ipynb
```

This option shows all steps with visualizations.

---

**Option 2: Python Script (For Quick Results)**

```bash
python customer_segmentation.py
```

This option runs the complete analysis and prints results to the console.

---

### Make Predictions for New Customers

The analysis can predict revenue for new customers based on their demographics.

**Example 1:** 33-year-old Turkish woman using Android

```
Persona Code: TUR_ANDROID_FEMALE_31_40
Expected Revenue: \$41.83
Segment: A (Premium)
Recommendation: Offer VIP treatment and exclusive features
```

**Example 2:** 35-year-old French woman using iOS

```
Persona Code: FRA_IOS_FEMALE_31_40
Expected Revenue: \$32.82
Segment: C (Mid-value)
Recommendation: Focus on engagement with value packages
```

---

## Technologies Used

- **Python 3.8+**
- **Pandas** - Data analysis and manipulation
- **NumPy** - Numerical calculations
- **Matplotlib** - Data visualization
- **Seaborn** - Statistical visualizations
- **Jupyter Notebook** - Interactive analysis

---

## Analysis Process Explained

### Task 1: Exploratory Data Analysis

I answered 10 important questions:

1. Read data and check basic information
2. Count unique platforms 
3. Count unique prices 
4. Count sales by price 
5. Count sales by country 
6. Calculate total revenue by country 
7. Count sales by platform 
8. Calculate average price by country 
9. Calculate average price by platform 
10. Calculate average price by country-platform combination

---

### Task 2: Group by Demographics

- Combined all demographic variables
- Calculated average revenue for each combination
- Found patterns in spending behavior

---

### Task 3: Sort by Revenue

- Sorted customers by spending amount
- Identified highest and lowest spending groups
- Found opportunities for targeting

---

### Task 4: Clean the Data

- Converted index to columns
- Made data easier to work with
- Prepared for next steps

---

### Task 5: Create Age Categories

Created 5 age groups:
- 0-18 years
- 19-23 years
- 24-30 years
- 31-40 years
- 41-66 years

**Finding:** The 41-66 group spends the most (\$34.48 average)!

---

### Task 6: Build Customer Personas

- Combined country + platform + gender + age group
- Created unique codes like `USA_IOS_MALE_31_40`
- Built 109 unique customer personas

---

### Task 7: Create Revenue Segments

- Used quartiles to divide personas into 4 groups
- Each segment represents 25% of the personas
- Groups are labeled A (highest) to D (lowest)

---

### Task 8: Make Predictions

- Can now predict revenue for any new customer
- Just need their demographics
- Instant segment assignment for marketing strategy

---

##  What I Learned

### Technical Skills:
- **Data analysis** with Pandas (groupby, pivot tables, aggregations)
- **Customer segmentation** using quartiles
- **Feature engineering** (creating age categories)
- **Data visualization** with Matplotlib and Seaborn
- **Converting analysis into business insights**

### Business Skills:
- How to turn data into actionable strategies
- Understanding customer behavior patterns

---



## Data Insights Summary

### Platform Performance
- **Android total revenue:** ~\$101,590 (2,974 × \$34.17)
- **iOS total revenue:** ~\$69,026 (2,026 × \$34.07)
- Despite similar average spending, Android generates more total revenue due to higher volume

### Segment Distribution
- Each segment contains about 25% of personas
- Segment A customers spend 32% more than Segment D customers
- Moving customers from D to C could increase revenue by 15%

### Age Patterns
- The 31-40 age group spends only \$0.97 less than 0-18 group
- This shows the product appeals to all ages
- Opportunity to create age-specific content

---

## Key Takeaways

1. **Platforms are equal** - Android and iOS users spend almost the same (0.3% difference)
2. **Age surprise** - Older customers (41-66) spend the most, not the 30s group
3. **Countries are similar** - All within \$1.20 - global pricing works well
4. **Segmentation works** - Clear separation into 4 meaningful groups
5. **Predictions are accurate** - Can estimate revenue for new customers based on demographics

---

## Acknowledgments
This project is for educational purposes.
- **Miuul Data Science Bootcamp** for the project framework, the analysis methodology and insights are my own work
---
