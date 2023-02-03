from math import fabs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions

# options
Path = "G:\\chromedriver\\chromedriver.exe"
chrome_options = ChromeOptions()
chrome_options.add_experimental_option("detach", True) # to keep the chrome open

# search target
def search_target(driver, target):
    driver.implicitly_wait(1)
    search_box = driver.find_element(
        By.XPATH, '//div[@class="Er7QU copyable-text selectable-text"]')
    search_box.send_keys(target + Keys.ENTER)

    # get target
    driver.implicitly_wait(1)
    driver.find_element(By.XPATH, '//span[@class="matched-text _11JPr"]').click()

# set what to send
def chat(driver, message):
    driver.implicitly_wait(1)
    # message_box = driver.find_element(By.XPATH, '//div[@class="fd365im1 to2l77zo bbv8nyr4 mwp4sxku gfz4du6o ag5g9lrv bze30y65 bdf91cm1"]')
    message_box = driver.find_element(By.XPATH, '//div[@title="Ketik pesan"]')
    message_box.send_keys(message)
    message_box.send_keys(Keys.ENTER)

# spam message
def spam_message(driver, message, spamMessage):
    for i in range(int(spamMessage)):
        driver.implicitly_wait(1)
        chat(driver, message)

# do send message 
def send_message(driver):
    message = input("Enter message: ")
    spamMessage = input("Enter numbers to spam message: ")
    spam_message(driver, message, spamMessage)
    # program finished
    print("Program finished\n")
    # ask to repeat the message, and ask to change the target or not
    repeat_message(driver, message, spamMessage)

# ask to repeat the message, and ask to change the target or not
def repeat_message(driver, message, spamMessage):
    repeat = input("Do you want to repeat the message? (y/n): ")
    if repeat == "y":
        # CHANGE THE TARGET
        change_target = input("Do you want to change the target? (y/n): ")
        if change_target == "y":
            target = input("Enter target name: ")
            search_target(driver, target)
            # CHANGE THE MESSAGE
            send_message(driver)
        else:
            # ask to change the message
            change_message = input("Do you want to change the message? (y/n): ")
            if change_message == "y":
                # change the message
                send_message(driver)
            else:
                spam_message(driver, message, spamMessage)
    else:
        print("Program finished\n")
        return False

    # ask to repeat the message, and ask to change the target or not
    run_again()

# run the program again
def run_again():
    run = input("Do you want to run the program again? (y/n): ")
    if run == "y":
        main()
    else:
        print("Program finished\n")
        return False

# main
def main():
    # open web driver
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://web.whatsapp.com/")

    # wait for user to scan qr code
    input("Press any key after scanning qr code\n")

    # get target
    target = input("Enter target name: ")
    search_target(driver, target)

    # send message
    send_message(driver)

    # close driver
    driver.close()


# run the program
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("There is an error, please run the program again\n")
        print(e) # to show the error when debugging
        # ask to run the program again
        run_again()