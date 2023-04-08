

# Script Description
This is a Python script that extracts data from the HTML of a given URL using the `Playwright` and `BeautifulSoup` libraries. The script is designed to extract information about a specific type of product from a Romanian eCommerce website called `Cartuseria.ro`. The extracted information includes whether or not a Frequently Asked Questions (FAQ) section exists, whether or not a product category exists, the number of internal links within the category description, and the total number of products available in the category.

# Requirements
- Python 3.x
- `playwright` library
- `bs4` library

# Usage
- Install `playwright` and `bs4` libraries using the following command: `pip install playwright bs4`
- Clone the repository containing the script
- Run the script with the following command: `python script_name.py url`
  - Replace `script_name.py` with the name of the script file
  - Replace `url` with the URL of the page to extract data from

# Output
The script outputs the following data:
- Whether or not a FAQ section exists
- Whether or not a product category exists
- The number of internal links within the category description
- The total number of products available in the category

The output is displayed in the console.
