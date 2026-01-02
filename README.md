# 📸 Image Alt Text Scraper

A clean and simple Python web scraper that extracts:

- Book titles  
- Image URLs  
- Image alt text  

from the website **Books to Scrape**, and saves the results into a structured `results.json` file.

This project is part of my learning journey in Python, web scraping, and backend development — built step‑by‑step with clarity and clean code.

---

## 🚀 Features

- Scrapes real product data from a live website  
- Extracts image alt text (useful for accessibility and computer vision tasks)  
- Normalizes image URLs  
- Saves results in a readable JSON format  
- Beginner‑friendly and easy to extend  

---

## 🛠️ Technologies Used

- Python 3  
- Requests  
- BeautifulSoup4  
- JSON  

---

## 📦 Installation

Install the required libraries:

```bash
pip install requests
pip install beautifulsoup4
```

▶️ How to Run

Run the scraper:
```
python scraper.py
```
After running, you will see:
```
Scraping completed. Results saved to results.json
```
The file results.json will contain all extracted data.

📁 Project Structure

```
image-alt-text-scraper/
│
├── scraper.py
├── results.json
├── sampleCode.html
├── README.md
└── screenshots/
```

📸 Screenshots

Add your screenshots here:

    Code running in VS Code

    Terminal output

    JSON results

📌 Future Improvements

    Add pagination support

    Export results to CSV

    Add CLI options

    Build a small API endpoint using Django or FastAPI


🧑‍💻 Author

Developed by Kamal Saleem Allah Al-Hejaili
Python Developer — Web Scraping & Automation