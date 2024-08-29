from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui


class imdb:  # Create a Class
    def __init__(self):  # Constructor method
        self.driver = webdriver.Chrome()  # Create a Chrome WebDriver Instance
        self.driver.maximize_window()  # Maximize the Window
        self.driver.implicitly_wait(10)  # Global wait for all the elements
        self.driver.get("https://www.imdb.com/search/name/")  # Open a website


    def fill_details(self):  # Method to perform Actions
        actions = ActionChains(self.driver)  # Initialize the ActionChains
        wait = WebDriverWait(self.driver, 20)  # Initialize the WebDriverWait (Explicit Wait)


        # Perform the Actions
        ExpandAll = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Expand all']")))
        actions.scroll_to_element(ExpandAll).perform()
        ExpandAll.click()


        Name = wait.until(EC.presence_of_element_located((By.ID, "text-input__3")))
        actions.scroll_to_element(Name).perform()
        Name.send_keys("Walt Disney")


        BirthDateFrom = wait.until(EC.presence_of_element_located((By.ID, "text-input__10")))
        actions.scroll_to_element(BirthDateFrom).perform()
        BirthDateFrom.send_keys("1901-01")


        BirthDateTo = wait.until(EC.presence_of_element_located((By.ID, "text-input__11")))
        actions.scroll_to_element(BirthDateTo).perform()
        BirthDateTo.send_keys("1901-12")


        BirthDay = wait.until(EC.presence_of_element_located((By.ID, "text-input__4")))
        actions.scroll_to_element(BirthDay).perform()
        BirthDay.send_keys("12-05")


        Awards_and_Recognition = wait.until(EC.presence_of_element_located((By.XPATH, "//div[text()='Awards & recognition']")))
        actions.scroll_to_element(Awards_and_Recognition).perform()
        pyautogui.press('tab', presses=15)
        pyautogui.press('enter')


        PageTopics = wait.until(EC.presence_of_element_located((By.XPATH, "//div[text()='Page topics']")))
        actions.scroll_to_element(PageTopics).perform()
        SearchTopic = wait.until(EC.presence_of_element_located((By.XPATH, "//select[@id='within-topic-dropdown-id']")))
        pyautogui.press('tab', presses=13)  # Navigate to Search With Topic
        pyautogui.press('down')  # Select Place of Birth
        Topic = wait.until(EC.presence_of_element_located((By.ID, "text-input__5")))
        Topic.send_keys("Chicago")


        DeathDateFrom = wait.until(EC.presence_of_element_located((By.ID, "text-input__14")))
        actions.scroll_to_element(DeathDateFrom).perform()
        DeathDateFrom.send_keys("1966-01")


        DeathDateTo = wait.until(EC.presence_of_element_located((By.ID, "text-input__15")))
        actions.scroll_to_element(DeathDateTo).perform()
        DeathDateTo.send_keys("1966-12")


        GenderIdentity = wait.until(EC.presence_of_element_located((By.XPATH, "//div[text()='Gender identity']")))
        actions.scroll_to_element(GenderIdentity).perform()
        pyautogui.press('tab', presses=2)  # Navigate to Male
        pyautogui.press('enter')  # Select Male


        Credits = wait.until(EC.presence_of_element_located((By.XPATH, "//div[text()='Credits']")))
        actions.scroll_to_element(Credits).perform()
        CreditsSearch = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@class='sc-cb8b4fe5-0 kbqvBS react-autosuggest__input']")))
        CreditsSearch.send_keys("EPCOT (1967)")
        actions.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).key_down(Keys.ENTER).key_up(Keys.ENTER)


        AdultNamesInclude = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Adult names']")))
        actions.scroll_to_element(AdultNamesInclude).perform()
        AdultNamesInclude.click()


        SeeResults = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='See results']")))
        actions.scroll_to_element(SeeResults).perform()
        SeeResults.click()


    def quit(self):  # Method to close the WebDriver
        self.driver.quit()


# Main Execution
if __name__ == "__main__":
    IMDB = imdb()

    try:
        IMDB.fill_details()

    except Exception as e:
        print(f"Error Occured: {e}")
    
    finally:
        IMDB.quit()
