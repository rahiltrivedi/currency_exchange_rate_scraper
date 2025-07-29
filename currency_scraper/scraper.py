import os
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_exchange_rates():
    print("🌐 Scraping exchange rates from x-rates.com...")

    # Setup headless Chrome
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(service=Service(), options=chrome_options)
    url = "https://www.x-rates.com/table/?from=USD&amount=1"
    driver.get(url)

    wait = WebDriverWait(driver, 10)

    # There are two tables: USD to others, and others to USD
    tables = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "ratesTable")))

    currencies = []
    rates = []

    for table in tables:
        rows = table.find_elements(By.TAG_NAME, "tr")[1:]  # skip header row
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            if len(cols) >= 2:
                currency = cols[0].text.strip()
                try:
                    rate = float(cols[1].text.strip())
                except ValueError:
                    continue
                currencies.append(currency)
                rates.append(rate)

    driver.quit()

    # Save to CSV
    data = pd.DataFrame({"Currency": currencies, "Rate (per USD)": rates})
    os.makedirs("data", exist_ok=True)
    date_str = datetime.now().strftime("%Y-%m-%d")
    csv_path = f"data/exchange_rates_{date_str}.csv"
    data.to_csv(csv_path, index=False)
    print(f"✅ Data saved to {csv_path}")

    # Visualization: Top 10 strongest currencies
    data_sorted = data.sort_values(by="Rate (per USD)").tail(10)

    plt.figure(figsize=(12, 7))
    bars = plt.barh(data_sorted["Currency"], data_sorted["Rate (per USD)"],
                    color="mediumseagreen", edgecolor="black")
    plt.title("Top 10 Strongest Currencies per USD", fontsize=16, weight='bold')
    plt.xlabel("Exchange Rate", fontsize=12)
    plt.grid(axis="x", linestyle="--", alpha=0.7)

    for bar in bars:
        plt.text(bar.get_width(), bar.get_y() + bar.get_height()/2,
                 f"{bar.get_width():.2f}", va="center", ha="left", fontsize=10)

    plt.tight_layout()
    plot_path = f"data/exchange_rates_chart_{date_str}.png"
    plt.savefig(plot_path)
    plt.close()
    print(f"📊 Chart saved to {plot_path}")
