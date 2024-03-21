# ECMWF-Web-Scraper
Web scraping the ECMWF NC files from "http://data.aicnic.cn/ECMWF/"

## Description
This Python script serves as a web scraper for the website "http://data.aicnic.cn/ECMWF/", specifically designed to automate the downloading process of weather data files. It utilizes the Selenium WebDriver to interact with the website, enabling the user to input the number of pages they wish to download data from, selecting all checkboxes on each page, and initiating the download process.

## Input
  - The user is prompted to enter an integer representing the number of pages of data they want to download.
    This input should be within the range of 1 to 585 (Max number of pages).

## Output
  - The script downloads the selected weather data files from the website and saves them to the specified network drive path.
    Once the download is completed, the webdriver will automatically close.

## Notes
1. **Selenium WebDriver**: Ensure that the Selenium WebDriver for Chrome is properly installed and compatible with your system.
2. **Network Drive Path**: Set the `NETWORK_DRIVE_PATH` variable to the appropriate path where you want to save the downloaded files.
3. **Download Time**: The script may take some time to download the data files, depending on the number of pages selected and the speed of the internet connection.
4. **Interrupting Download**: You can interrupt the download process by pressing `Ctrl+C` in the terminal. The script will handle the interruption gracefully.
5. **Page Structure**: Any changes to the structure or elements of the website may require corresponding updates to the XPath or CSS selectors used in the script.
6. **Error Handling**: The script includes basic error handling to deal with exceptions that may occur during the scraping process. If an error occurs on a specific page, it will print out an error message along with the page number.
7. **Browser Interaction**: The script interacts with the website using a Chrome browser instance controlled by Selenium WebDriver. Ensure that the browser window remains open until the script completes its execution.
8. **Download Completion**: The script checks for the completion of downloads by monitoring the presence of files with the ".tar" extension in the specified download directory. (This extension should be changed based on the system the script will be running on: .crdownload for windows)
9. **Dependency Installation**: Before running the script, make sure to install the required dependencies specified in the `import` statements at the beginning of the script. You can install them using pip:
   
    ```
    pip install selenium
    ```

### NB
  - You will need the chrome driver for this code to work corretly and unzip the driver in the directory where the code is. To get the chrome driver, here is the official link: https://chromedriver.chromium.org/downloads
  - Feel free to modify and adapt this script according to your specific requirements. If you encounter any issues or have further questions, please don't hesitate to reach out for assistance.

