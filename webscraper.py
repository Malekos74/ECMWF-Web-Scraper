import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# Find latest downloaded file and return it
def latest_download_file():
    path = r"/home/students/Downloads"
    os.chdir(path)
    files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
    
    if not files:
        return None  # No files in the directory
    
    newest = files[-1]
    return newest

# Check if a file is downloaded.
def is_download_complete(file_path):
    # Check if the file extension is not ".crdownload"
    return not file_path.endswith(".crdownload")


url = 'http://data.aicnic.cn/ECMWF/'
driver = webdriver.Chrome()
driver.get(url)


time.sleep(5)
# Wait for the dropdown to be clickable
# dropDown = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[4]/div[2]/div/span/div")

# TODO: Choose 100 in the drop down menu
# dropDown = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[4]/div[2]/div/span/div");
# dropDown.click()


# time.sleep(5)
# Now, wait for the options to become visible
# options_xpath = '//ul[@class="el-select-dropdown__list"]/li[@class="el-select-dropdown__item"]'
# options = WebDriverWait(driver, 10).until(
#     EC.visibility_of_all_elements_located((By.XPATH, options_xpath))
# )

# # Find the option with "100条/页" and click on it
# for option in options:
#     if option.text == '100条/页':
#         option.click()
#         break


# dropDown = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[4]/div[2]/div/span/div");
# dropDown.click()
# time.sleep(2)

# option = driver.find_element(By.XPATH, "//*[contains(text(), '100条/页')]")
# option.click()

while True:
    try:
        user_input = int(input("Enter a number of pages between 1 and 585 you want to downlad: "))
        if 1 <= user_input <= 585:
            break  # Exit the loop if the input is valid
        else:
            print("Input must be between 1 and 585. Try again.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

for i in range(1, user_input + 1) : 
    # Select all element on page
    checkBox = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[4]/div[3]/div/div/div[2]/table/thead/tr/th[1]/div/label')
    checkBox.click()
    time.sleep(0.25)

    # Go to next page
    button = driver.find_element(By.CLASS_NAME, 'btn-next')
    button.click()
    time.sleep(0.25)


time.sleep(1)

#download selected
downloadButton = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[4]/div[1]/button[1]")
downloadButton.click()

time.sleep(2)

while True:
    time.sleep(1)
    newest_file = latest_download_file()

    if newest_file is None:
        print("No files in the directory. Waiting...")
    elif is_download_complete(newest_file):
        print("Download completed: ", newest_file)
        break
    else:
        print("Download in progress. Waiting...")
        
time.sleep(2)
        


# close browser
driver.quit()
