# Automationpractice.com

## Description:
Automation of the purchase process of a product using __http://automationpractice.com/index.php__ webpage.

Used Page Object Pattern implementation. 

### Tests were implemented and run on:
* System: macOS Mojave 10.14
* Browsers: Firefox 62.0.3, Chrome 69.0.3497.100 (both 64-bit)
* Selenium WebDriver: 3.14.0
* Python: 3.6

### Prerequisites:
__geckodriver__: https://github.com/mozilla/geckodriver/releases

__chromedriver__: https://sites.google.com/a/chromium.org/chromedriver/

(example below shows how add to path __geckodriver__)

Chmod to executable file
```
chmod +x ~/Downloads/geckodriver
```
Move the file from Downloads folder to share folder
```
sudo mv -f ~/Downloads/geckodriver /usr/local/share/geckodriver
```
Create a symlink
```
sudo ln -s /usr/local/share/geckodriver /usr/local/bin/geckodriver
```
Chmod to executable file
```
chmod +x ~/Downloads/geckodriver
```
Move the file from Downloads folder to share folder
```
sudo mv -f ~/Downloads/geckodriver /usr/local/share/geckodriver
```
Create a symlink
```
sudo ln -s /usr/local/share/geckodriver /usr/local/bin/geckodriver
```
#### How to run the tests:
Single test cases are implemented into the following file
```
/automationpractice/tests_generic/FunctionalTest.py
```
and could be run independently.

A whole test suite is also defined in the root of the project and it includes the execution of the single test cases in a single run.
```
python /automationpractice/main.py
```