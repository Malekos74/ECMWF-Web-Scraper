'''
    This Python scrip will help you scrape the ECMWF data out of the specified website in the code
    
    IN:
        - Number of pages to take into consideration
        - URL and other variables can be edited as see fit
    OUT:
        - The number of relevant pages of .NC files will be downloaded to the specified path
    
[Malek Miled] 21.03.2024
'''

import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Find latest downloaded file and return it
def latest_download_file():
    path = NETWORK_DRIVE_PATH
    os.chdir(path)
    files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
    
    if not files:
        return None  # No files in the directory
    
    newest = files[-1]
    return newest

# Check if a file is downloaded.
def is_download_complete(file_path):
    # Check if the file extension is not ".crdownload"
    return file_path.endswith(".tar")

# Update the default download path to the NAS file path
def change_download_path():
    chromeOptions = webdriver.ChromeOptions()
    prefs = {"download.default_directory" : NETWORK_DRIVE_PATH}
    chromeOptions.add_experimental_option("prefs", prefs)
    
    # # ignore SSL certificate errors Can't do this because then the page doesn't load
    # chromeOptions.add_argument('--ignore-certificate-errors')
    
    driver = webdriver.Chrome(options = chromeOptions)
    return driver

# Function to wait for an element to be clickable
def wait_for_element_clickable(driver, by, value, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((by, value))
    )

# Website URL
URL = 'http://data.aicnic.cn/ECMWF/'

# NAS file path
NETWORK_DRIVE_PATH = r"X:\Weather"

if __name__ == '__main__':
    driver = change_download_path()
    driver.get(URL)


    while True:
        try:
            user_input = int(input("Enter a number of pages between 1 and 585 you want to download: "))
            if 1 <= user_input <= 585:
                break  # Exit the loop if the input is valid
            else:
                print("Input must be between 1 and 585. Try again.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    for i in range(1, user_input + 1):
        try:
            # Wait for the checkbox to be clickable
            checkbox = wait_for_element_clickable(driver, By.XPATH, '/html/body/div[1]/div[2]/div[4]/div[3]/div/div/div[2]/table/thead/tr/th[1]/div/label')
            
            # Check the checkbox
            checkbox.click()
            time.sleep(0.5)

            # Go to next page
            button = wait_for_element_clickable(driver, By.CLASS_NAME, 'btn-next')
            button.click()
            time.sleep(0.25)

        except Exception as e:
            print(f"Error on page {i}: {str(e)}")


    time.sleep(2)

    #download selected
    downloadButton = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[4]/div[1]/button[1]")
    downloadButton.click()

    time.sleep(2)

    while True:
        try:
            time.sleep(1)
            newest_file = latest_download_file()

            if newest_file is None:
                print("No files in the directory. Waiting...")
            elif is_download_complete(newest_file):
                print("Download completed: ", newest_file)
                break
            else:
                print("Download in progress. Waiting...")
        except KeyboardInterrupt:
            print("Download process interrupted. Exiting.")
            break
            
    time.sleep(4)
            
    # close browser
    driver.quit()
