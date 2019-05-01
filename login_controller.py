import requests
import instagramscraper
from selenium import webdriver
import re
import pdb
import time
import bs4
import pickle
from profile_objects import Picture
from profile_objects import Profile
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
import os

path = "/mnt/c/SE/Github/instagram-webscraper/chromedriver.exe"

def likes_parser(data):
    data = re.search("\n(.*) others", data, flags=0)
    return int(data.group(1)) + 1

def caption_parser(data):
    data = re.search("\n(.*)\n",data, flags=0)
    return data.group(1)

def add_headless(set):
    chrome_options = Options()
    if(set):
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920x1080")
    return chrome_options

def find_userdata(driver,profile):
    userdata = driver.find_elements_by_class_name("g47SY")
    numposts = int(userdata[0].text)
    followers = int(userdata[1].text.replace(",",""))
    following = int(userdata[2].text.replace(",",""))

    try:
        link_to_profile_pic = driver.find_element_by_class_name("_6q-tv").get_attribute('src')
        profile.set_profilePic(link_to_profile_pic)
    except:
        link_to_profile_pic = driver.find_element_by_class_name("be6sR").get_attribute('src')
        profile.set_profilePic(link_to_profile_pic)

    profile.set_num_posts(numposts)
    profile.set_followers(followers)
    profile.set_following(following)
    time.sleep(1)
    return profile

def login(driver,url,username,password):
    driver.get("https://www.instagram.com/"+url)
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/nav/div[2]/div/div/div[3]/div/span/a[1]/button").click()
    time.sleep(1)
    driver.find_element_by_xpath("//input[@name='username']").send_keys(username)
    driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
    driver.find_element_by_xpath("//button[@type='submit']").click()
    time.sleep(1)

def find_posts(driver):
    posts = driver.find_elements_by_class_name("v1Nh3")
    postlist = []
    for post in posts:
        post.click()
        time.sleep(2)
        likes = driver.find_element_by_class_name("Nm9Fw")
        likes = likes_parser(likes.text)

        caption = driver.find_element_by_class_name("C4VMK")
        caption = caption_parser(caption.text.strip())

        numcomments = driver.find_element_by_class_name("XQXOT").get_attribute("outerHTML").count("Mr508")
        driver.find_element_by_class_name("ckWGn").click()
        pic = Picture(likes,numcomments,caption,"")
        print("Likes", likes)
        print("Number of Commnets", numcomments)
        postlist.append(pic)
    return postlist

def privateuser(username,password,url,path_to_driver,headless):

    profile = Profile(url,"","","","","")
    chrome_options = add_headless(headless)
    driver = webdriver.Chrome(chrome_options=chrome_options,executable_path=path_to_driver)
    login(driver,url,username,password)
    profile = find_userdata(driver,profile)
    postlist = find_posts(driver)
    profile.set_posts(postlist)
    driver.close()
    profile.view_all()

privateuser("mikeyilao","Chantelle16","mikeyilao",path,False)
#unblockeduser("https://www.instagram.com/mattyilao/")
