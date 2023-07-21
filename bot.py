from datetime import *
import os

count = 0


class message:
    def message1(self, message, path):
        print(message)
        if not os.path.exists(path):
            os.mkdir(path)
        else:
            if os.path.isfile("./logs/{}.{}".format(date.today(), 'log')):
                y = open("./logs/{}.{}".format(date.today(), 'log'), 'a')
                y.write("{}:{}:{}: {}".format(datetime.now().hour, str(datetime.now().minute).ljust(2, "0"),
                                              str(datetime.now().second).ljust(2, "0"),
                                              message) + "\n")
                y.close()
            else:
                os.path.join('./logs/{}.{}'.format(date.today(), 'log'))
                y = open("./logs/{}.{}".format(date.today(), 'log'), 'a')
                y.write("{}:{}:{}: {}".format(datetime.now().hour, str(datetime.now().minute).ljust(2, "0"),
                                              str(datetime.now().second).ljust(2, "0"),
                                              message) + "\n")
                y.close()


def bot():
    global count
    try:
        from selenium import webdriver
        from selenium.webdriver.common.keys import Keys
        from time import sleep
        from random import randint, choice
        import configparser

        config = configparser.ConfigParser()
        config.read("bot.ini", encoding="utf-8")
        message2.message1("\nVersion: 1.02", path)
        message2.message1(
            "Status: bot started", path)
        chromedriver_path = './chromedriver.exe'
        webdriver = webdriver.Chrome(executable_path=chromedriver_path)
        sleep(2)
        webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
        sleep(3)
        message2.message1("Status: writing login", path)
        username = webdriver.find_element_by_name('username')
        username.send_keys(config["bot"]["login"])
        message2.message1("Status: writing password", path)
        password = webdriver.find_element_by_name('password')
        password.send_keys(config["bot"]["password"])

        button_login = webdriver.find_element_by_css_selector('#loginForm > div > div:nth-child(3) > button > div')
        button_login.click()
        sleep(10)
        try:
            notnow = webdriver.find_element_by_css_selector(
                'body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm')
            notnow.click()  # comment these last 2 lines out, if you don't get a pop up asking about notifications
        except:
            pass
        hashtag_list = config["bot"]["tags"].split(";")
        new_followed = []
        tag = -1
        followed = 0
        likes = 0
        comments = 0
        commentariy = []
        c = open("comment.txt", "r", encoding="utf-8")
        comment = c.readline().rstrip()
        while comment != "":
            if comment[0] == "#":
                comment = c.readline().rstrip()
                continue
            else:
                commentariy.append(comment)
                comment = c.readline().rstrip()
        c.close()
        pertag = config["bot"]["pertag"]
        pause1 = int(config["bot"]["pause"].split(";")[0])
        pause2 = int(config["bot"]["pause"].split(";")[1])
        for hashtag in hashtag_list:
            tag += 1
            webdriver.get('https://www.instagram.com/explore/tags/' + hashtag_list[tag] + '/')
            sleep(10)
            first_thumbnail = webdriver.find_element_by_xpath(
                '/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div/div[2]')
            message2.message1("Status: open publication", path)
            first_thumbnail.click()
            sleep(randint(1, 2))

            for x in range(1, int(pertag)):
                try:
                    if webdriver.find_element_by_xpath(
                            '/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').text == 'Подписаться':
                        message2.message1("Status: following", path)
                        webdriver.find_element_by_xpath(
                            '/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').click()
                        new_followed.append(username)
                        followed += 1
                        message2.message1("Status: pause 15 sec between following and like", path)
                        sleep(15)
                    else:
                        message2.message1("Status: error: already subscribed", path)
                    button_like = webdriver.find_element_by_xpath(
                        '/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button')
                    message2.message1("Status: make a like", path)
                    button_like.click()
                    likes += 1
                    # Comments and tracker
                    comm_prob = randint(1, 10)
                    if comm_prob > 7:
                        u = randint(int(pause1), int(pause2))
                        message2.message1("Status: pause {} sec between like and comment".format(u), path)
                        sleep(u)
                        comments += 1
                        webdriver.find_element_by_xpath(
                            '/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[2]/button').click()
                        comment_box = webdriver.find_element_by_xpath(
                            '/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea')
                        comment_box.send_keys(choice(commentariy))
                        sleep(1)
                        # Enter to post comment
                        comment_box.send_keys(Keys.ENTER)
                        message2.message1("Status: pause 10 sec between comment and transition", path)
                        sleep(10)
                    message2.message1("Status: transition to the next post", path)
                    webdriver.find_element_by_link_text('Далее').click()
                    p = randint(int(pause1), int(pause2))
                    message2.message1("Status: pause {} sec between transition and subscribing".format(p), path)
                    sleep(p)
                except Exception as e:
                    message2.message1("ERROR: {}".format(e), path)
                    message2.message1("Status: transition to the next post", path)
                    webdriver.find_element_by_link_text('Далее').click()
                    p = randint(int(pause1), int(pause2))
                    message2.message1("Status: pause {} sec between transition and subscribing".format(p), path)
                sleep(p)
    except Exception as e:
        count += 1
        print(e)
    if count < 5:
        bot()


path = "./logs"
message2 = message()
bot()
