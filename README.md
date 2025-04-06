# Flipkart Laptop Price Scraper 🛒💻

This project scrapes laptop listings from [Flipkart](https://www.flipkart.com/) and extracts their names and prices into a CSV file for further analysis.

## 🧠 Overview

The script uses:

- **Selenium** to render the dynamic JavaScript-based Flipkart web page.
- **BeautifulSoup** to parse the HTML content.
- **Pandas** to structure and save the data into a CSV file.

The program is completely headless — it runs in the background without opening a browser window.

---

## 📂 Files in the Repository

| File/Folder               | Description |
|--------------------------|-------------|
| `main.py`                | Main Python script that performs the web scraping and saves output files. |
| `flipkart_laptops.csv`   | CSV file containing scraped laptop names and prices. |
| `flipkart_laptops_page.txt` | Raw HTML content of the Flipkart search page for laptops. |
| `env.yml`                | Conda environment file listing all dependencies. |
| `chrome-win64/`          | Chrome browser binary folder (headless use). |
| `chromedriver-win64/`    | ChromeDriver binary folder. |
| `.gitignore`             | Specifies files/folders to be ignored by git. |
| `README.md`              | This file. |

---

## 🛠 Requirements

- Python 3.8+
- Google Chrome (headless binary provided)
- ChromeDriver (compatible version provided)

### 🔧 Install dependencies using Conda

```bash
conda env create -f env.yml -n your_env_name
