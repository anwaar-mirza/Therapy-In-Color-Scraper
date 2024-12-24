# Therapy-In-Color-Scraper

This document provides detailed documentation for the two Python scripts: **dataFile.py** and **linkFiles.py**. These scripts are designed for web scraping tasks using Selenium, pandas, and other libraries.

---

## **Script 1: dataFile.py**

### **Overview**
This script is designed to scrape detailed profile information about therapists from a specific website. It extracts various details and saves them into structured CSV files for further analysis or use.

### **Dependencies**
The script relies on the following Python libraries:
- Selenium: For automating browser actions.
- geopy: For geocoding addresses into latitude and longitude.
- pandas: For handling and exporting data.
- time and os: For time delays and file system interactions.

Install the required libraries using:
```bash
pip install selenium geopy pandas
```

### **Class: TherapyInColorData**
This class encapsulates all functionality for web scraping therapist profiles.

#### **Attributes**
- `data_dict`: A dictionary for storing scraped data.
- `driver`: Selenium WebDriver instance for browser automation.
- `geocode`: ArcGIS geocoder instance for retrieving geographic coordinates.

#### **Methods**

1. **`__init__(self)`**
   - Initializes the WebDriver and maximizes the browser window.

2. **`land_required_page(self, my_url)`**
   - Navigates to the specified URL and waits for the page to load.

3. **Data Extraction Methods:**
   - **`get_name(self)`**: Extracts the therapist’s name.
   - **`get_speciality(self)`**: Extracts the therapist’s specialties.
   - **`treatment_approach(self)`**: Extracts the approach to treatment.
   - **`get_insurance_accepted(self)`**: Checks and retrieves accepted insurance information.
   - **`get_discription(self)`**: Extracts the profile description.
   - **`get_ratting(self)`**: Extracts the profile rating.
   - **`get_address(self)`**: Extracts the address and converts it into geographic coordinates.
   - **`get_phone_number(self)`**: Retrieves the contact number.
   - **`get_website(self)`**: Retrieves the website link.
   - **`get_socail_links(self)`**: Extracts links to social media profiles (Facebook, Twitter, Instagram).
   - **`get_timings(self)`**: Extracts the therapist’s availability.
   - **`get_youtube_link(self)`**: Extracts a YouTube video link if available.

4. **File Management Methods:**
   - **`get_url(self, type, img)`**: Saves listing type and image URL.
   - **`move_into_file(self, file)`**: Saves the scraped data into CSV files.

5. **Main Execution Loop**
   - Iterates over a list of therapist types, loads URLs from CSV files, and scrapes data for each profile.

#### **Outputs**
- Individual CSV files for each therapist type.
- A combined CSV file containing all scraped data.

#### **Execution Notes**
- Ensure proper XPath selectors match the target website’s structure.
- Set the correct paths for saving output files.
- Handle missing or unavailable data with `try-except` blocks.

---

## **Script 2: linkFiles.py**

### **Overview**
This script is designed to scrape listing links and associated images from WordPress-based websites. It handles pagination and stores the results in CSV files.

### **Dependencies**
The script uses the following libraries:
- Selenium: For browser automation.
- pandas: For managing and exporting data.
- time and os: For delays and file management.

Install the required libraries using:
```bash
pip install selenium pandas
```

### **Class: WordpressListingLinks**
This class handles the scraping of links and images.

#### **Attributes**
- `data`: A dictionary to temporarily store link and image data.
- `driver`: Selenium WebDriver instance for browser automation.

#### **Methods**

1. **`__init__(self)`**
   - Initializes the WebDriver and maximizes the browser window.

2. **`land_required_page(self, my_url)`**
   - Navigates to the specified URL and waits for the page to load.

3. **`get_links(self, file)`**
   - Extracts links and image URLs from the current page and saves them into a CSV file.

4. **`handle_pagination(self, i)`**
   - Handles pagination by clicking the next page button.

#### **Main Execution Loop**
1. Accepts user inputs for:
   - URL to scrape.
   - File name for output.
   - Number of pages to scrape.
2. Iterates through the specified number of pages, extracting links and images.

#### **Outputs**
- A CSV file containing links and image URLs for each page.

#### **Execution Notes**
- Adjust XPath selectors to match the target website’s structure.
- Ensure proper handling of pagination if the website uses dynamic content loading.
- Set the output directory and file name correctly.

---

## **Common Best Practices**
1. **Set Up WebDriver Properly:**
   - Ensure the correct version of ChromeDriver matches your Chrome browser.
   - Use `Options()` for headless operation if needed.

2. **Implicit Waits:**
   - Use `implicitly_wait()` to allow sufficient time for elements to load.

3. **Error Handling:**
   - Wrap extraction logic in `try-except` blocks to handle missing or inaccessible elements.

4. **Data Management:**
   - Use pandas for efficient handling and saving of data.
   - Specify unique headers for CSV files to avoid overwriting.

5. **Resource Management:**
   - Close the WebDriver session after completing tasks.

---

## **Improvements and Extensions**
- **Error Logging:** Add logging to track errors and exceptions.
- **Dynamic XPath:** Use more robust selectors to handle minor changes in website structure.
- **Parallel Processing:** Use threading or multiprocessing for scraping multiple pages simultaneously.
- **API Integration:** If the website offers an API, consider using it for faster and more reliable data retrieval.

---

## **Conclusion**
The provided scripts, **dataFile.py** and **linkFiles.py**, offer a robust framework for web scraping tasks. While **dataFile.py** is tailored for extracting detailed profile information, **linkFiles.py** focuses on gathering listing links and associated images. Both scripts demonstrate the effective use of Selenium and pandas to automate and manage data extraction. By following best practices and implementing suggested improvements, these scripts can be further optimized for scalability, reliability, and adaptability to various web scraping scenarios. These tools serve as a foundation for developing advanced data scraping solutions to meet diverse needs.

