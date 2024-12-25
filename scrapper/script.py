from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import CONSTANT as c
from pymongo import MongoClient
import time
import os
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv(c.DATABASE))
db=client[c.DATABASE_NAME]
collection = db[c.DATABASE_JOBS]

class Linkedin:

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        self.jobs=[]

    def login(self):
        self.driver.get(c.PAGE_URL)
        username = self.wait.until(EC.presence_of_element_located((By.ID,c.LOGIN_USERNAME)))
        username.click()
        time.sleep(5)
        username.send_keys(os.getenv(c.EMAIL))
        time.sleep(5)
        password = self.wait.until(EC.presence_of_element_located((By.ID,c.LOGIN_PASSWORD)))
        password.click()
        time.sleep(5)
        password.send_keys(os.getenv(c.PASSWORD) + Keys.ENTER)
        time.sleep(15)

    def jobs(self,locate=None,subtitle=None):
        navbars = self.wait.until(EC.presence_of_element_located((By.XPATH,c.JOBS)))
        navbars.click()
        time.sleep(10)
        location = self.wait.until(EC.presence_of_element_located((By.XPATH,c.LOCATION)))
        location.click()
        location.clear()
        location.send_keys(locate + Keys.ENTER)
        time.sleep(10)
        title = self.wait.until(EC.presence_of_element_located((By.XPATH,c.JOBS_TITLE)))
        title.click()
        title.clear()
        title.send_keys(subtitle + Keys.ENTER)
        time.sleep(10)
        job_cards = self.wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME,c.JOBS_CRAWL)))
        time.sleep(5)
        for job in job_cards:
            job_link = WebDriverWait(job,10).until(EC.presence_of_element_located((By.XPATH,c.JOBS_LINK)))
            job_title = WebDriverWait(job,10).until(EC.presence_of_element_located((By.CLASS_NAME,c.JOB_TITLE)))
            company = WebDriverWait(job,10).until(EC.presence_of_element_located((By.CLASS_NAME,c.JOBS_PROVIDER)))
            job_location = WebDriverWait(job,10).until(EC.presence_of_element_located((By.CLASS_NAME,c.JOBS_LOCATION)))
            job_id = list((job_link.get_attribute("href")).split("/"))[5]
            job.click()
            job_details = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME,c.JOBS_DESCRIPTION)))
            data={
                "job_id": job_id,
                "link": job_link.get_attribute("href"),
                "company":company.text,
                "title":job_title.text,
                "location":job_location.text,
                "description":list((job_details.text).split("\n"))
            }
            self.jobs.append(data)
            time.sleep(10)
        
    def addJobs(self):
        for data in self.jobs:
            existing_job = collection.find_one({"job_id": data["job_id"]})
            if existing_job!=None:
                insert_data = collection.insert_one(data)



user = Linkedin()
user.login()
time.sleep(5)
user.jobs(locate="Bangalore",subtitle="Software Engineer")
time.sleep(5)

