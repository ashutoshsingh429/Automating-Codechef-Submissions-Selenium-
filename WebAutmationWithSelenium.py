from selenium import webdriver
import getpass
import time

# Codechef credentials for login
username = "ashutosh_429"
password = getpass.getpass("Password : ")

# Problem code
problem = "TEST"

# Submission code
code = """
#include<bits/stdc++.h>
using namespace std;
int main()
{
    while(true)
    {
        int input;
        cin>>input;
        if(input == 42)
            break;
        else 
            cout<<input<<endl;
    }
}
"""

# Start a browser session
browser = webdriver.Chrome("C:/Users/ashut/WebDrivers/chromedriver.exe")

# Open link in browser
browser.get("https://www.codechef.com/")

# Login
username_element = browser.find_element_by_id("edit-name")
username_element.send_keys(username)

password_element = browser.find_element_by_id("edit-pass")
password_element.send_keys(password)

browser.find_element_by_id("edit-submit").click()
time.sleep(10)

# Open submission page
browser.get("https://www.codechef.com/submit/" + problem)

# Sleep function to let web components load incase of slow internet connection
time.sleep(10)

# Click on toggle button to open simple text mode
# browser.find_element_by_id("edit_area_toggle_checkbox_edit-program").click()
browser.find_element_by_xpath('//*[@id="edit-language"]/option[1]').click()

# Adding code
code_element = browser.find_element_by_id("edit-program")
code_element.send_keys(code)

# Submitting Problem
# browser.find_element_by_id("edit-submit-1").click()
