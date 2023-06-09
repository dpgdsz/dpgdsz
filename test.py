import time
import ddddocr
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class CoursePlayer:
    def __init__(self):
        self.driver = None
        self.ocr = None

    def open_browser(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=options)

    def close_browser(self):
        if self.driver is not None:
            self.driver.quit()

    def login(self, username, password):
        wait = WebDriverWait(self.driver, 10)
        self.driver.get('https://student.cx-online.net/#/login')
        name_input = wait.until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/div/div/div/form/div[2]/div[2]/div[1]/div/div/div/input')))
        name_input.send_keys(username)
        password_input = self.driver.find_element(By.XPATH,
                                                  '/html/body/div/div/div/form/div[2]/div[2]/div[2]/div/div/div/input')
        password_input.send_keys(password)
        code_input = self.driver.find_element(By.XPATH,
                                              '/html/body/div/div/div/form/div[2]/div[2]/div[3]/div/div[1]/div/input')
        img_code = self.driver.find_element(By.XPATH, '/html/body/div/div/div/form/div[2]/div[2]/div[3]/div/div[2]')
        if self.ocr is None:
            self.ocr = ddddocr.DdddOcr()
        img_text = self.ocr.classification(img_code.screenshot_as_png)
        code_input.send_keys(img_text)
        login_button = self.driver.find_element(By.XPATH, '/html/body/div/div/div/form/div[4]/button')
        login_button.click()

    def watch_course_1(self, course_rounds=5):
        wait = WebDriverWait(self.driver, 10)
        my_class_button = wait.until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/section/aside/div/ul/div[5]/li/span')))
        my_class_button.click()
        time.sleep(2)
        course_button = self.driver.find_element(By.XPATH,
                                                 '/html/body/div[1]/section/main/main/div/div/div[2]/div[1]/div['
                                                 '1]/div[1]/div[3]/div/div[1]/div/table/tbody/tr[1]/td['
                                                 '6]/div/div/button/span')
        course_button.click()
        handles = self.driver.window_handles
        current_handle = self.driver.current_window_handle
        for i in range(course_rounds):
            for handle in handles:
                if handle != current_handle:
                    self.driver.switch_to.window(handle)
                try:
                    wait_video = WebDriverWait(self.driver, 10)
                    video = wait_video.until(EC.presence_of_element_located((By.TAG_NAME, 'video')))
                    url = self.driver.execute_script("return arguments[0].currentSrc;", video)
                    print(f"正在观看第1种课程视频: {url}")
                    video.click()  # 点击播放
                    time.sleep(10)
                    video.send_keys(Keys.END)  # 跳转到视频结尾
                    time.sleep(5)  # 暂停
                    video.send_keys(Keys.ESCAPE)  # 按下ESC
                    time.sleep(10)
                except Exception as e:
                    print(f"发生异常: {str(e)}")
            print(f"第{i + 1}节第1种课程已完成")
        print("所有第1种课程已完成")

    def watch_course_2(self, course_rounds=5):
        wait = WebDriverWait(self.driver, 10)
        my_class_button = wait.until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/section/aside/div/ul/div[5]/li/span')))
        my_class_button.click()
        time.sleep(2)
        course_button = self.driver.find_element(By.XPATH,
                                                 '/html/body/div[1]/section/main/main/div/div/div[2]/div[1]/div['
                                                 '1]/div[1]/div[3]/div/div[1]/div/table/tbody/tr[2]/td['
                                                 '6]/div/div/button/span')
        course_button.click()
        handles = self.driver.window_handles
        current_handle = self.driver.current_window_handle
        for i in range(course_rounds):
            for handle in handles:
                if handle != current_handle:
                    self.driver.switch_to.window(handle)
                try:
                    wait_video = WebDriverWait(self.driver, 10)
                    video = wait_video.until(EC.presence_of_element_located((By.TAG_NAME, 'video')))
                    url = self.driver.execute_script("return arguments[0].currentSrc;", video)
                    print(f"正在观看第2种课程视频: {url}")
                    video.click()  # 点击播放
                    time.sleep(10)
                    video.send_keys(Keys.END)  # 跳转到视频结尾
                    time.sleep(5)  # 暂停
                    video.send_keys(Keys.ESCAPE)  # 按下ESC
                    time.sleep(10)
                except Exception as e:
                    print(f"发生异常: {str(e)}")
            print(f"第{i + 1}节第2种课程已完成")
        print("所有第2种课程已完成")

    def watch_course_3(self, course_rounds=5):
        wait = WebDriverWait(self.driver, 10)
        my_class_button = wait.until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/section/aside/div/ul/div[5]/li/span')))
        my_class_button.click()
        time.sleep(2)
        course_button = self.driver.find_element(By.XPATH,
                                                 '/html/body/div[1]/section/main/main/div/div/div[2]/div[1]/div['
                                                 '1]/div[1]/div[3]/div/div[1]/div/table/tbody/tr[3]/td['
                                                 '6]/div/div/button/span')
        course_button.click()
        handles = self.driver.window_handles
        current_handle = self.driver.current_window_handle
        for i in range(course_rounds):
            for handle in handles:
                if handle != current_handle:
                    self.driver.switch_to.window(handle)
                try:
                    wait_video = WebDriverWait(self.driver, 10)
                    video = wait_video.until(EC.presence_of_element_located((By.TAG_NAME, 'video')))
                    url = self.driver.execute_script("return arguments[0].currentSrc;", video)
                    print(f"正在观看第3种课程视频: {url}")
                    video.click()  # 点击播放
                    time.sleep(10)
                    video.send_keys(Keys.END)  # 跳转到视频结尾
                    time.sleep(5)  # 暂停
                    video.send_keys(Keys.ESCAPE)  # 按下ESC
                    time.sleep(10)
                except Exception as e:
                    print(f"发生异常: {str(e)}")
            print(f"第{i + 1}节第3种课程已完成")
        print("所有第3种课程已完成")

    def watch_course_4(self, course_rounds=5):
        wait = WebDriverWait(self.driver, 10)
        my_class_button = wait.until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/section/aside/div/ul/div[5]/li/span')))
        my_class_button.click()
        time.sleep(2)
        course_button = self.driver.find_element(By.XPATH,
                                                 '/html/body/div[1]/section/main/main/div/div/div[2]/div[1]/div['
                                                 '1]/div[1]/div[3]/div/div[1]/div/table/tbody/tr[4]/td['
                                                 '6]/div/div/button/span')
        course_button.click()
        handles = self.driver.window_handles
        current_handle = self.driver.current_window_handle
        for i in range(course_rounds):
            for handle in handles:
                if handle != current_handle:
                    self.driver.switch_to.window(handle)
                try:
                    wait_video = WebDriverWait(self.driver, 10)
                    video = wait_video.until(EC.presence_of_element_located((By.TAG_NAME, 'video')))
                    url = self.driver.execute_script("return arguments[0].currentSrc;", video)
                    print(f"正在观看第4种课程视频: {url}")
                    video.click()  # 点击播放
                    time.sleep(10)
                    video.send_keys(Keys.END)  # 跳转到视频结尾
                    time.sleep(5)  # 暂停
                    video.send_keys(Keys.ESCAPE)  # 按下ESC
                    time.sleep(10)
                except Exception as e:
                    print(f"发生异常: {str(e)}")
            print(f"第{i + 1}节第4种课程已完成")
        print("所有第4种课程已完成")

    def watch_course_5(self, course_rounds=5):
        wait = WebDriverWait(self.driver, 10)
        my_class_button = wait.until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/section/aside/div/ul/div[5]/li/span')))
        my_class_button.click()
        time.sleep(2)
        course_button = self.driver.find_element(By.XPATH,
                                                 '/html/body/div[1]/section/main/main/div/div/div[2]/div[1]/div['
                                                 '1]/div[1]/div[3]/div/div[1]/div/table/tbody/tr[5]/td['
                                                 '6]/div/div/button/span')
        course_button.click()
        handles = self.driver.window_handles
        current_handle = self.driver.current_window_handle
        for i in range(course_rounds):
            for handle in handles:
                if handle != current_handle:
                    self.driver.switch_to.window(handle)
                try:
                    wait_video = WebDriverWait(self.driver, 10)
                    video = wait_video.until(EC.presence_of_element_located((By.TAG_NAME, 'video')))
                    url = self.driver.execute_script("return arguments[0].currentSrc;", video)
                    print(f"正在观看第5种课程视频: {url}")
                    video.click()  # 点击播放
                    time.sleep(10)
                    video.send_keys(Keys.END)  # 跳转到视频结尾
                    time.sleep(5)  # 暂停
                    video.send_keys(Keys.ESCAPE)  # 按下ESC
                    time.sleep(10)
                except Exception as e:
                    print(f"发生异常: {str(e)}")
            print(f"第{i + 1}节第5种课程已完成")
        print("所有第5种课程已完成")

    def watch_course_6(self, course_rounds=5):
        wait = WebDriverWait(self.driver, 10)
        my_class_button = wait.until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/section/aside/div/ul/div[5]/li/span')))
        my_class_button.click()
        time.sleep(2)
        course_button = self.driver.find_element(By.XPATH,
                                                 '/html/body/div[1]/section/main/main/div/div/div[2]/div[1]/div['
                                                 '1]/div[1]/div[3]/div/div[1]/div/table/tbody/tr[6]/td['
                                                 '6]/div/div/button/span')
        course_button.click()
        handles = self.driver.window_handles
        current_handle = self.driver.current_window_handle
        for i in range(course_rounds):
            for handle in handles:
                if handle != current_handle:
                    self.driver.switch_to.window(handle)
                try:
                    wait_video = WebDriverWait(self.driver, 10)
                    video = wait_video.until(EC.presence_of_element_located((By.TAG_NAME, 'video')))
                    url = self.driver.execute_script("return arguments[0].currentSrc;", video)
                    print(f"正在观看第6种课程视频: {url}")
                    video.click()  # 点击播放
                    time.sleep(10)
                    video.send_keys(Keys.END)  # 跳转到视频结尾
                    time.sleep(5)  # 暂停
                    video.send_keys(Keys.ESCAPE)  # 按下ESC
                    time.sleep(10)
                except Exception as e:
                    print(f"发生异常: {str(e)}")
            print(f"第{i + 1}节第6种课程已完成")
        print("所有第6种课程已完成")

    def watch_course_7(self, course_rounds=5):
        wait = WebDriverWait(self.driver, 10)
        my_class_button = wait.until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/section/aside/div/ul/div[5]/li/span')))
        my_class_button.click()
        time.sleep(2)
        course_button = self.driver.find_element(By.XPATH,
                                                 '/html/body/div[1]/section/main/main/div/div/div[2]/div[1]/div['
                                                 '1]/div[1]/div[3]/div/div[1]/div/table/tbody/tr[7]/td['
                                                 '6]/div/div/button/span')
        course_button.click()
        handles = self.driver.window_handles
        current_handle = self.driver.current_window_handle
        for i in range(course_rounds):
            for handle in handles:
                if handle != current_handle:
                    self.driver.switch_to.window(handle)
                try:
                    wait_video = WebDriverWait(self.driver, 10)
                    video = wait_video.until(EC.presence_of_element_located((By.TAG_NAME, 'video')))
                    url = self.driver.execute_script("return arguments[0].currentSrc;", video)
                    print(f"正在观看第7种课程视频: {url}")
                    video.click()  # 点击播放
                    time.sleep(10)
                    video.send_keys(Keys.END)  # 跳转到视频结尾
                    time.sleep(5)  # 暂停
                    video.send_keys(Keys.ESCAPE)  # 按下ESC
                    time.sleep(10)
                except Exception as e:
                    print(f"发生异常: {str(e)}")
            print(f"第{i + 1}节第7种课程已完成")
        print("所有第7种课程已完成")

    def watch_course_8(self, course_rounds=5):
        wait = WebDriverWait(self.driver, 10)
        my_class_button = wait.until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/section/aside/div/ul/div[5]/li/span')))
        my_class_button.click()
        time.sleep(2)
        course_button = self.driver.find_element(By.XPATH,
                                                 '/html/body/div[1]/section/main/main/div/div/div[2]/div[1]/div['
                                                 '1]/div[1]/div[3]/div/div[1]/div/table/tbody/tr[8]/td['
                                                 '6]/div/div/button/span')
        course_button.click()
        handles = self.driver.window_handles
        current_handle = self.driver.current_window_handle
        for i in range(course_rounds):
            for handle in handles:
                if handle != current_handle:
                    self.driver.switch_to.window(handle)
                try:
                    wait_video = WebDriverWait(self.driver, 10)
                    video = wait_video.until(EC.presence_of_element_located((By.TAG_NAME, 'video')))
                    url = self.driver.execute_script("return arguments[0].currentSrc;", video)
                    print(f"正在观看第8种课程视频: {url}")
                    video.click()  # 点击播放
                    time.sleep(10)
                    video.send_keys(Keys.END)  # 跳转到视频结尾
                    time.sleep(5)  # 暂停
                    video.send_keys(Keys.ESCAPE)  # 按下ESC
                    time.sleep(10)
                except Exception as e:
                    print(f"发生异常: {str(e)}")
            print(f"第{i + 1}节第8种课程已完成")
        print("所有第8种课程已完成")


if __name__ == '__main__':
    player = CoursePlayer()

    player.open_browser()

    player.login("511", "a123456")
    player.watch_course_1()
    player.watch_course_2()
    player.watch_course_3()
    player.watch_course_4()
    player.watch_course_5()
    player.watch_course_6()
    player.watch_course_7()
    player.watch_course_8()
    player.close_browser()
