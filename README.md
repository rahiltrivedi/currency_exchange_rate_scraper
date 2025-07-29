# 💱 Currency Exchange Rate Scraper

This project is a Python-based web scraper that extracts live foreign exchange rates from [x-rates.com](https://www.x-rates.com/) using **Selenium** and saves the data into a CSV file. Additionally, it generates a professional bar chart showing the top 10 strongest currencies relative to USD.

---

## 📌 Features

- 🌐 Scrapes live currency exchange rates (USD base)
- 📁 Saves daily data to a `data/` folder in CSV format
- 📊 Automatically generates a clean bar chart of top 10 strongest currencies
- 🧼 Headless browser scraping using Selenium
- ✅ Beginner-friendly structure and code
- 📅 Supports daily execution and historical tracking

---

## 🗂️ Project Structure

currency_scraper_project/
- │
- ├── currency_scraper/
- - │ └── scraper.py # Core scraping and visualization logic
- │
-  ├── data/ # Output folder for CSVs and charts
- - │ └── exchange_rates_YYYY-MM-DD.csv
- - │ └── exchange_rates_chart_YYYY-MM-DD.png
- │
- ├── main.py # Entry point script
- ├── README.md # Project documentation
- └── venv/ (optional) # Virtual environment


---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/your-username/currency_scraper_project.git
cd currency_scraper_project
```
### 2. Set up a virtual environment (optional but recommended)
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # macOS/Linux
```
### 3. Run the scraper
```bash
python main.py
```
---
## 🛠️ Tech Stack

- Python 3.10+

- Selenium (Chrome WebDriver)

- Pandas

- Matplotlib

---
