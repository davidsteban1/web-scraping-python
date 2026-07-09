# E-Commerce Price Monitor & Automated Email Alert System

## 🎯 Project Overview
This project monitors product prices on e-commerce websites and sends an email alert when your target price is reached. It is designed as a modular, general-purpose system: by changing the target product URL and CSS selectors in the scraper module, you can track virtually any product on almost any online store.

## 🚀 Features
- **General-purpose product tracking** with configurable URL and selectors
- **Cloud automation** with GitHub Actions scheduled Cron runs
- **Modern dark-mode email alerts** powered by a separate HTML/CSS template
- **Reliable email delivery** using the Resend API
- **Secure configuration** via environment variables and GitHub Secrets

## ⚙️ Installation & Setup
1. **Clone the repository**
   ```bash
   git clone https://github.com/davidsteban1/web-scraping-python.git
   cd web-scraping-python
   ```

2. **Create and activate a virtual environment (recommended)**
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your `.env` file**
   Create a `.env` file in the project root:
   ```env
   API_KEY=your_resend_api_key
   EMAIL=your_destination_email
   ```

5. **Run locally**
   ```bash
   python main.py
   ```

## 🛠️ Customization

To monitor a different product or store:

* **Update the target URL and CSS selectors** inside `scraper.py` to match the new online store's structure.
* **(Optional) Update the destination link** and store name inside `template.html` so the button in your modern Dark Mode email redirects to the new product page.

Once committed and pushed, the GitHub Actions cloud workflow will automatically track your new product on the next scheduled run.
