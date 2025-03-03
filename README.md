# Zomato-Scraping-Analysis
# 📊 Zomato Restaurant Data Analysis & Dashboard

## 🔥 Project Overview
This project involves web scraping restaurant data from **Zomato**, cleaning and analyzing the dataset, and visualizing key insights through an interactive **Power BI dashboard**.

## 📌 Workflow
1. **Web Scraping**: Extract restaurant details using Python (BeautifulSoup/Selenium).
2. **Data Cleaning**: Preprocess data in Pandas (handling missing values, transforming data types, etc.).
3. **Data Analysis**: Generate insights from restaurant ratings, delivery times, costs, and offers.
4. **Power BI Dashboard**: Create interactive visuals and slicers for easy exploration.

---

## 📥 Data Collection (Web Scraping)
### 🔧 Tools Used:
- `BeautifulSoup` & `Selenium` (for dynamic page scraping)
- `Pandas` (for storing and processing data)

### 📌 Scraped Attributes:
- **Restaurant Name**
- **Rating**
- **Cuisine Type**
- **Cost for One**
- **Delivery Time**
- **Discount Offers**
- **Zomato URL**

---

## 🛠️ Data Cleaning & Preprocessing
### 📌 Steps Taken:
✅ Removed missing values from `Rating` and `Cost for One`
✅ Extracted numerical values from discount offers
✅ Converted cost values into numerical format
✅ Created `Cost for One (Bins)` for grouped analysis

---

## 📊 Power BI Dashboard
### 🔥 Key Visuals & Insights
- **Avg. Delivery Time (min) vs. Rating** (Line Chart)
- **Restaurant Count by Cost for One (Binned)** (Bar Chart)
- **Top-Rated Restaurants** (Card Visualization)
- **Delivery Time Distribution** (Histogram)
- **Delivery Time Distribution** (Histogram)
- 

### 📌 Theme Customization
- **Background**: Light gray to muted pink
- **Chart Transparency**: 86%
- **Text & Borders**: Black (0% darker)

### 🖼️ Dashboard Preview:
![Power BI Dashboard](dashboard_image.png)

---

## 📊 Charts Included
| Chart Name | Type |
|------------|----------------------|
| Avg. Delivery Time vs. Rating | Line Chart |
| Restaurant Count by Rating | Column Chart |
| Count of Restaurants by Cost for One (Bins) | Bar Chart |
| Avg. Cost for One by Rating | Column Chart |

---

## 🎯 Final Insights
📌 **Most restaurants have a rating between 4.0 - 4.5**
📌 **Higher-rated restaurants tend to have faster delivery times**
📌 **Most restaurants charge between ₹100 - ₹500 per meal**

---

## 🚀 How to Use
1. Run the Python script to scrape Zomato data.
2. Clean the data and save it as a CSV file.
3. Import the dataset into Power BI.
4. Apply the custom theme and create visualizations.

---

## 📌 Technologies Used
- **Python (Selenium, BeautifulSoup, Pandas)** → Web Scraping & Cleaning
- **Power BI** → Dashboard & Visualization
- **GitHub** → Version Control & Documentation

---

## 📢 Contributors
👤 **Yash** - Data Collection, Analysis & Power BI Dashboard

🔗 **Connect with Me**: [LinkedIn](#) | [GitHub](#)

---

## ⭐ Show Some Love!
If you like this project, give it a ⭐ on GitHub!
