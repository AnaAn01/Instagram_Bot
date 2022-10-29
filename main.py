from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

CHROME_DRIVER_PATH = "driver_path"
NECESSARY_ACCOUNT = 'account'
USER_NAME = 'name'
PASSWORD = 'password'


class InstaGet:
    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=path)

    def login(self):
        self.driver.get('https://www.instagram.com/')
        time.sleep(4)
        user_name = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        password = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        button = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[3]/button/div')
        user_name.send_keys(USER_NAME)
        time.sleep(2)
        password.send_keys(PASSWORD)
        time.sleep(2)
        # password.send_keys(Keys.ENTER)
        button.click()
        self.driver.get(f"https://www.instagram.com/{NECESSARY_ACCOUNT}")

    def find_followers(self):
        followers_button = self.driver.find_element(By.XPATH, '//*[@id="mount_0_0_n3"]/div/div/div/div[1]/div/div/div/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a/div')
        followers_button.click()
        followers_name = self.driver.find_elements(By.CLASS_NAME, '._ab8y._ab94._ab97._ab9f._ab9k._ab9p._abcm')
        followers_list = []
        for follower in followers_name:
            followers_list.append(follower.text)
        return followers_list

    def find_following(self):
        following_button = self.driver.find_element(By.XPATH,
                                                    '//*[@id="mount_0_0_VI"]/div/div/div/div[1]/div/div/div/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a/div')
        following_button.click()
        following_name = self.driver.find_elements(By.CLASS_NAME, '._ab8y._ab94._ab97._ab9f._ab9k._ab9p._abcm')
        following_list = []
        for following in following_name:
            following_list.append(following.text)
        return following_list

    def compare(self, list_1, list_2):
        common_list = set(list_1).intersection(list_2)
        unfollowers_list = []
        for item in list_2:
            if item not in common_list:
                unfollowers_list.append(item)
        print(unfollowers_list)


bot = InstaGet(CHROME_DRIVER_PATH)
bot.login()
# bot.find_followers()
# bot.find_following()
bot.compare(bot.find_followers(), bot.find_following())