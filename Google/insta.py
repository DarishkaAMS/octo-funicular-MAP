# import getpass
#
# my_password = getpass.getpass('What is your password?\n')
# print(my_password)
from urllib.parse import urlparse
import os
import time
import requests
from conf import INSTA_USERNAME, INSTA_PASSWORD
from selenium import webdriver


browser = webdriver.Chrome()
url = 'https://www.instagram.com'
browser.get(url)

time.sleep(2)
username_el = browser.find_element_by_name('username')
username_el.send_keys(INSTA_USERNAME)
password_el = browser.find_element_by_name('password')
password_el.send_keys(INSTA_PASSWORD)

submit_btl_el = browser.find_element_by_css_selector('button[type="submit"]')
submit_btl_el.click()

body_el = browser.find_element_by_css_selector('body')
html_text = body_el.get_attribute('innerHTML')
# print(html_text)

'''
<button class="_5f5mN       jIbKX  _6VtSN     yZn4P   ">Follow</button>
'''

# browser.find_elements_by_css_selector('button')

# Using xpath
# my_button_xpath = '//button'
# browser.find_elements_by_css_selector(my_button_xpath)


def click_to_follow(browser):
    # my_follow_btn_xpath = "//a[contains(text(), 'Follow')][not(contains(text(), 'Following'))]"
    # my_follow_btn_xpath = "//*[contains(text(), 'Follow')][not(contains(text(), 'Following'))]"
    my_follow_btn_xpath = "//button[contains(text(), 'Follow')][not(contains(text(), 'Following'))]"
    follow_btn_elments = browser.find_elements_by_xpath(my_follow_btn_xpath)
    for btn in follow_btn_elments:
        time.sleep(2)  # self-throttle
        try:
            btn.click()
        except:
            pass

#
# new_user_url = 'https://www.instagram.com/ted/'
# browser.get(new_user_url)
# click_to_follow(browser)


time.sleep(2)
the_VCP_url = 'https://www.instagram.com/veuveclicquot/'
browser.get(the_VCP_url)

post_url_pattern = 'https://www.instagram.com/p/<post-slug-id>'
post_xpath_str = '//a[contains(@href, "/p/")]'
post_links = browser.find_elements_by_xpath(post_xpath_str)
post_link_el = None

if len(post_links) > 0:
    post_link_el = post_links[0]

if post_link_el != None:
    post_href = post_link_el.get_attribute("href")
    browser.get(post_href)


video_els = browser.find_elements_by_xpath("//video")
images_els = browser.find_elements_by_xpath("//img")
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(BASE_DIR, "INSTA images")
os.makedirs(IMG_DIR, exist_ok=True)

# Python Image Library


def scrape_and_save(elements):
    for el in elements:
        # print(img.get_attribute('src'))
        url = el.get_attribute('src')
        base_url = urlparse(url).path
        # print(base_url)
        filename = os.path.basename(base_url)
        filepath = os.path.join(IMG_DIR, filename)
        if os.path.exists(filepath):
            continue
        with requests.get(url, stream=True) as r:
            try:
                r.raise_for_status()
            except:
                continue
            with open(filepath, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192): # To configure the size
                    if chunk:
                        f.write(chunk)


# scrape_and_save(video_els)
# scrape_and_save(images_els)
#
"""
<textarea aria-label="Add a comment…" placeholder="Add a comment…" 
class="Ypffh" autocomplete="off" autocorrect="off"></textarea>
"""


def automate_comment(browser, content="Magnifique!!!"):
    time.sleep(3)
    comment_xpath_str = "//textarea[contains(@placeholder, 'Add a comment')]"
    comment_el = browser.find_element_by_xpath(comment_xpath_str)
    comment_el.send_keys(content)
    submit_btns_xpath = "button[type='submit']"
    submit_btns_els = browser.find_elements_by_css_selector(submit_btns_xpath)
    time.sleep(2)
    for btn in submit_btns_els:
        try:
            btn.click()
        except:
            pass


# automate_comment(browser, content="Magnifique!!!")

"""
Like  = <svg aria-label="Like" class="_8-yf5 " fill="#262626" height="24" viewBox="0 0 48 48" width="24">
<path d="..."</path></svg>
"""


def automate_likes(browser):
    like_heart_svg_xpath = "//*[contains(@aria-label, 'Like')]"
    all_like_hearts_els = browser.find_elements_by_xpath(like_heart_svg_xpath)

    max_heart_height = -1
    for heart_el in all_like_hearts_els:
        h = heart_el.get_attribute("height")
        current_h = int(h)
        if current_h > max_heart_height:
            max_heart_height = current_h

    all_like_hearts_els = browser.find_elements_by_xpath(like_heart_svg_xpath)
    # print(max_heart_height, "max_heart_height")
    for heart_el in all_like_hearts_els:
        h = heart_el.get_attribute("height")
        # print(h)
        if h == max_heart_height or h == f'{max_heart_height}':
            parent_button = heart_el.find_element_by_xpath('..') #go to the parent button
            print(parent_button)
            time.sleep(2)
            try:
                parent_button.click()
            except:
                pass


automate_likes(browser)
automate_comment(browser, content="Magnifique!!!")