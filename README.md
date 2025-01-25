# Project Gemini

## Google Login Mirroring Project

This project demonstrates how to mirror Google's login process to potentially capture user credentials. **Please note that this is for educational purposes only and should not be used for malicious activities.** 

**Disclaimer:** Using this code to capture credentials without explicit user consent is illegal and unethical. 

### How it Works

The project utilizes a combination of Flask, Selenium, and regular expressions to achieve the following:

1. **Web Server (Flask):** A Flask web server provides the initial interface where users enter their email address. It also handles the display of mirrored Google login pages and the reception of captured credentials.

2. **Browser Automation (Selenium):** Selenium is used to automate a Chrome browser instance. This automated browser interacts with the actual Google login pages, mirroring the user's actions on the mirrored pages provided by the Flask server.

3. **HTML Modification (Regular Expressions):**  The HTML content of Google's login pages is fetched using Selenium. Before being displayed to the user, the HTML is modified using regular expressions. This modification includes:
    * Changing form actions to point to the Flask server.
    * Altering or removing JavaScript that might interfere with the process.
    * Potentially adjusting input field names and adding visual cues for the user.

4. **Credential Capture:** When the user submits their email, password, and 2FA code on the mirrored pages, the data is sent to the Flask server, where it can be captured and processed.

![ZTAz3e8m40VmlKznB-3Yo60WyJEHHJJE5Iv8KbfoFJI-lQS614oGfMbplrxxRnfwriHrQPHEsH6SF99Ihn5c2pZZ9K6woIA0bMKa3rZgmgXlGTJ6kTnWLFDLM88sQrIdq38XErlLt3S_RGwO5OIfC7PGQU_lZZAPv3ZeshtYv-oUXkqntlUl-muNmBBmbT6FWH-Bti2_wLiu_W03Dlu6ytKqBNu39oHlUuQoK_x04m00](https://github.com/user-attachments/assets/49ab5149-5322-47b3-9867-b0a0fff4d94d)

### Project Structure

* **`web-server.py`:** Contains the Flask application code that handles routing, HTML rendering, and interaction with the Selenium module.
* **`google_auth.py`:**  Houses the Selenium automation logic for interacting with Google's login pages.
* **`regex_google.py`:**  Includes functions to modify the cloned HTML pages using regular expressions.
* **`templates/`:**  Contains HTML files:
    * `google-email.html`:  Initial page where the user enters their email.
    * `google-password.html`:  Mirrored Google password page.
    * `google-2fa.html`:  Mirrored Google 2FA page.

### Setup and Execution

1. **Install Dependencies:**
   ```bash
   pip install Flask Selenium undetected-chromedriver
2. **Download ChromeDriver:**
   Download the appropriate ChromeDriver executable for your Chrome browser version from the official website and place it in your project directory or add it to your system's PATH.

3. **Run the Flask Application:**
   ```bash
   python web-server.py

### Important Considerations
* **Ethical Use:** This project is intended for educational purposes only. Do not use it for any illegal or unethical activities.
* **Security Risks:** This approach involves handling sensitive user data, so it's crucial to implement robust security measures if used in any real-world scenario.
* **Detection:** Google employs various mechanisms to detect and prevent automated login attempts. This project might trigger those mechanisms, leading to account suspension or other consequences.

### Please use this code responsibly and ethically.
