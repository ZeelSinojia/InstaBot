from selenium import webdriver
from time import sleep
import os


class InstagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password

        self.driver = webdriver.Chrome('./chromedriver.exe')
        # open instagram
        self.driver.get('https://www.instagram.com/')
        sleep(5)
        # login to instagram
        self.driver.find_element_by_xpath(
            "//input[@name=\"username\"]").send_keys(username)
        self.driver.find_element_by_xpath(
            "//input[@name=\"password\"]").send_keys(password)
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()
        sleep(5)
        # skipping first dialogue
        self.driver.find_element_by_xpath(
            "//button[contains(text(), 'Not Now')]").click()

    def _follow_user(self, searchuser):
        # try:
        self.driver.find_element_by_xpath("//span[contains(text(), 'Search')]").click()
        # except Exception:
        #     self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()
        #     self.driver.find_element_by_xpath("//span[contains(text(), 'Search')]").click()
        # Type in searched username
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input').send_keys(searchuser)
        sleep(5)
        # Selecting the first username in search list
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]').click()
        sleep(5)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Follow')]").click()
        try:
            self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()
        except Exception:
            pass

    def followfromfollowers(self, searchuser, follow_range):
        follow_list = self._username_followers(searchuser, follow_range)
        # for rn in range(follow_range):
        #     self._follow_user(follow_list[rn])
        # print("Task completed succesfully")
        print(follow_list, len(follow_list))

    def _username_followers(self, searchuser, follow_range):
        self.driver.find_element_by_xpath(
            "//span[contains(text(), 'Search')]").click()
        # Type in searched username
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input').send_keys(searchuser)
        sleep(5)
        # Selecting the first username in search list
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]').click()
        sleep(3)
        # Selects the following lists
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/div/header/section/ul/li[3]/a').click()
        sleep(3)
        following = self._get_names(follow_range)
        return following

    def _get_names(self, max_user):
        # Assigning the scrollbox
        scroll_box = self.driver.find_element_by_xpath(
            '/html/body/div[4]/div/div[2]')

        number_of_iteration = 6
        # iterating through the list
        last_ht, ht = 0, 1
        print(max_user)
        while last_ht != ht:
            last_ht = ht
            sleep(4)
            print(number_of_iteration)
            if number_of_iteration >= max_user:
                break
            ht = self.driver.execute_script("""
            arguments[0].scrollTo(0, arguments[0].scrollHeight);
            return arguments[0].scrollHeight;
            """, scroll_box)
            number_of_iteration+=6
        # finding and storing all the a tags in links
        links = scroll_box.find_elements_by_tag_name('a')
        # fetching names from the links
        names = [name.text for name in links if name.text != '']
        sleep(3)
        # closing the list
        scroll_box.find_element_by_xpath(
            '/html/body/div[4]/div/div[1]/div/div[2]/button').click()
        return names


igbot = InstagramBot('optic.pubg', 'zeel2599@')
igbot.followfromfollowers('_zeel___', 50)



# Handle the number of accounts followed
# add the functionality to follow from followers list
# unfollow function
# delete post function based on something