# 📦 Flipkart Scraping Platform


**Flipkart Scraping Platform** is a powerful web application designed to help you effortlessly scrape product data from Flipkart. Built with Django, BeautifulSoup4, Requests, Pandas, and NumPy, this tool allows you to input a Flipkart URL and retrieve detailed product information, displayed in an easy-to-compare table format. You can view product names, prices, ratings, and direct links to the products, and download this data as a CSV file for further analysis.


## 📚 Table of Contents

1. [Features](#-features)
2. [Screenshots](#-screenshots)
3. [Installation](#-installation)
4. [Usage](#-usage)
5. [Updating for Flipkart Changes](#-updating-for-flipkart-changes)
6. [Contributing](#-contributing)
7. [Author](#-author)


## ✨ Features

- 🌐 **Web Scraping**: Automatically extracts product details from Flipkart pages.
- 📊 **Product Comparison**: Displays product information in a structured table for easy comparison.
- 📁 **CSV Export**: Download the scraped data in CSV format with a single click.
- 🔄 **Dynamic Adaptation**: Easily update the scraper to handle changes in Flipkart’s HTML structure.

## 📸 Screenshots

*(Add screenshots of your application here)*

## 🛠️ Installation

Follow these steps to get the Flipkart Scraping Platform up and running on your local machine:

1. **Clone the repository**:
    ```bash
    git clone <your-repo-url>
    ```

2. **Navigate to the project directory**:
    ```bash
    cd Django-Web-Scraping-master
    ```

3. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

## 🌟 Usage

1. Open your web browser and navigate to `http://127.0.0.1:8000/`.

2. Enter a Flipkart URL in the input field.

3. Click on the 'Submit' button to fetch the product data.

4. View the product details in the displayed table.

5. To download the data, click on the 'Download' button.

## 🔄 Updating for Flipkart Changes

Flipkart's HTML structure may change, which can cause the scraper to malfunction. To update the scraper:

1. Inspect the current Flipkart page to find the updated classes and tags.

2. Locate the classes and tags used for scraping in `views.py`.

3. Update the relevant sections in `views.py` with the new classes and tags.

## 🤝 Contributing

We welcome contributions to enhance Flipkart Scraping Platform! If you want to contribute:

1. Fork the repository.

2. Create a new branch:
    ```bash
    git checkout -b feature/YourFeature
    ```

3. Make your changes and commit them:
    ```bash
    git commit -m 'Add some feature'
    ```

4. Push to the branch:
    ```bash
    git push origin feature/YourFeature
    ```

5. Open a pull request.
   

## 🙏 Author

Abhishek Rajput
