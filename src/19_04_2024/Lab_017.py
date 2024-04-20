# How to navigate to another URL? by using get command but there is no any navigation command in python.
# Navigation commands are very popular in JAVA.
from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.by import By  # Imported By from common


# @pytest.mark.smoke
def test_vwologin_negative_TC():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    # driver.find_element(By.ID,"btn-make-appointment").click() --> by using ID

    # By.Link Text:
    # -------------
    # Rule 1) It will work only a tag , and it will always do full match or exact match with the text.
    # Rule 2) If there is no link text then it won't be able to find the element.
    # a tag-> anchor tag.

    # In the below tag, we have 3 attributes:-

    # <a id="btn-make-appointment" href="./profile.php#login" class="btn btn-dark btn-lg">Make Appointment</a>
    # <a
    # id="btn-make-appointment" -- 1st attribute
    # href="./profile.php#login" -- 2nd attribute
    # class="btn btn-dark btn-lg"> -- 3rd attribute
    # Make Appointment -- This is not an attribute. This is just a text which is a link text. This value we are looking for here in this case.
    # </a>

    # <a
    # id="btn-make-appointment" -- 1st attribute
    # href="./profile.php#login" -- 2nd attribute
    # class="btn btn-dark btn-lg"> -- 3rd attribute
    # Make Appointment -- This is not an attribute. This is just a text which is a link text. This value we are looking for here in this case.
    # </a>

    # Suppose "Make Appointment" (Link Text) is not present, then "Link Text" won't work.
    # Suppose if there are 2 elements with the same name, then It will return 1st one.

    # LINK_TEXT says that whatever the link text is available, it will pick that
    # but the important condition is that it will always do full match or exact match.
    # assert error_msg_element.text == "Your email, password, IP address or location did not match"

    # make_appointment_btn = driver.find_element(By.LINK_TEXT, "Make Appointment")
    # make_appointment_btn.click()

    # Partial Text:
    # ------------
    # This also works with anchor a tag. It is basically called as partial match (PARTIAL_LINK_TEXT).
    # PARTIAL_LINK_TEXT means what is the exact value , it will match with "Make Appointment".
    # It will match with "Make Appointment".
    # It will match with "Appointment" word also.
    # It will match with "Make" word also.
    # It will match with "App" word also.
    # It will match with "ment" also.
    # It checks for contains - keyword

    # For "LINK_TEXT" & "PARTIAL_LINK_TEXT", rules are same. But PARTIAL_LINK_TEXT will find the 1st element which is best matching.
    # First element which is best matching for "make appointment" and then it will click on it.
    # It finds the first unique element.
    # make_appointment_btn = driver.find_element(By.PARTIAL_LINK_TEXT, "Appointment")
    # make_appointment_btn.click()

    # By TagName:
    # -------
    # It means if we do "ctrl+f" via "inspect" element, and you mention a tag, we will see the
    # 6th element of "Make Appointment" with the tag name a.
    list_of_tags = driver.find_elements(By.TAG_NAME, "a") # a tag will give you multiple element. That' why we use fuction know as
    # find_elements instead of find_element. Instead of give you "Make Appointment" button, it will give you list of a tags.
    make_appointment_btn = list_of_tags[5]  # because index of list starts from 0 only.
    make_appointment_btn.click()

    time.sleep(2)
    driver.quit()
# Note: All these things finding the same thing. By using the same mechnaism, we are able to find it.
# ID - Unique ID,
# name - Unique ClassName,
# TagName - get 1, list of elements via findElements
# Link/Partial - a anchor tags
# Css Selector - 20% we will be using it.
# XPath - 60% we will be using it.
