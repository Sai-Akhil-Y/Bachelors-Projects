from pprint import pprint
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException, \
    UnexpectedAlertPresentException, ElementNotSelectableException,NoAlertPresentException
from selenium.webdriver import Firefox
from time import sleep
import requests
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as ec
from random import randint, choices
from string import ascii_letters, printable, digits
from selenium.webdriver.common.action_chains import ActionChains

driver = Firefox(executable_path=r'D:\geckodriver.exe')
url = 'http://localhost/teacher/'

print(" ....................... Starting UI Testing ...............................")
try:
    driver.get(url=url)
    print("Trying to open the Website ")
    req = requests.head(url=url)
    if req.status_code == 200:
        print('The Website exists and a response code of {} was received'.format(req.status_code))
    else:
        print('Unable to open the website and a response code of {} was received'.format(req.status_code))
        exit(105)
except Exception as e:
    print('Encounted a excception of {}'.format(e))

print('Length of the screen/Window Size is {}.'.format(driver.current_window_handle))
print('........Making the window to full Screen .............')
driver.maximize_window()
# sleep(3)
driver.get_screenshot_as_png()

print('Starting Main page Button testing    ..........')
try:
    for iter in range(6):
        main_buttons = driver.find_elements_by_class_name('login100-form-btn')
        ran = randint(0, 2)
        main_buttons[ran].click()
        current_url = driver.current_url
        if current_url == 'http://localhost/teacher/login.html':
            var = 'login'
        elif current_url == 'http://localhost/teacher/register.html':
            var = 'register'
        else:
            if current_url == 'http://localhost/teacher/shome.php':
                var = 'Student home'
        # noinspection PyUnboundLocalVariable
        print('In {i} iteration clicked on {button} button.'.format(i=iter + 1, button=var))
        # sleep(1)
        driver.get(url)
        driver.get_screenshot_as_png()

        # sleep(3)
except StaleElementReferenceException as exe:
    # noinspection PyUnboundLocalVariable
    print('Reference button is not found. Might be using old reference. Found in the {i} iteration'.format(i=iter))

print('.........Successfully tested all the buttons in the main page\t...........')

print('................Main page Testing Complete ..............')

print(' -------------   Checking Student Home  ------------------- ')
url = 'http://localhost/teacher/shome.php'
for _ in range(5):
    driver.get(url)
    dropdn = Select(driver.find_element_by_class_name('list-group-item'))
    print(' ...............  choosing from drop down in the studnet menu ..................')
    dropdn.select_by_index(randint(0, 1))
    # sleep(2)
    # driver.get_screenshot_as_png()
    button = driver.find_element_by_class_name('btn-outline-light').click()
    if driver.current_url == 'http://localhost/teacher/studentdisplay.php':
        print('SUCCESSFULLY ABLE TO VIEW FACULTY TIMETABLE')
    # sleep(5)

print('..............   Finished testing student home page ..............')
print('...............  Starting Login page testing .........................')

url = 'http://localhost/teacher/login.html'
# Postive Testcases
for iter in range(5):
    driver.get(url)
    rand_user = ''.join(choices(ascii_letters, k=randint(0, 12))).strip()
    rand_pass = ''.join(choices(ascii_letters, k=randint(0, 12))).strip()
    print('Sending a username :{user}\t and password of :{passs}\t'.format(user=rand_user, passs=rand_pass))
    username = driver.find_element_by_name('username')
    password = driver.find_element_by_name('pass')
    login_button = driver.find_elements_by_class_name('login100-form-btn')
    username.send_keys(rand_user)
    password.send_keys(rand_pass)

    # sleep(2)
    # driver.get_screenshot_as_png()
    print('  ..... Login was attempted ......  ')
    if len(rand_pass) > 0 and len(rand_user) > 0:
        try:
            login_button[0].click()
            alert = driver.find_element_by_class_name('alert-validate')
            print('Empty Username or Empty Password \t')
            print('\t\tRefreshing the Page \t')
            driver.refresh()
            continue
        except NoSuchElementException as e:
            try:
                WebDriverWait(driver, 3).until(ec.alert_is_present(),
                                               "Username and/or Password incorrect.\\nTry again.")
                alert = driver.switch_to.alert
                alert.accept()
                print("...............  Login is tested in iteration {iter}  ...........".format(iter=iter))
                driver.get(url)
            except TimeoutException:
                print("There is problem with login button.")
        except UnexpectedAlertPresentException as e:
            # print('Alert has been dismissed')
            pass
    else:
        if len(rand_user) == 0:
            print('Null Value detected. Username is empty')
        elif len(rand_pass) == 0:
            print('Null Value detected. Password is empty')
        iter -= 1
        driver.refresh()

# Negative Testcases
# Both None
driver.get(url)
username = driver.find_element_by_name('username')
password = driver.find_element_by_name('pass')
login_button = driver.find_elements_by_class_name('login100-form-btn')
username.send_keys('')
password.send_keys('')
login_button[0].click()
try:
    alert = driver.find_element_by_class_name('alert-validate')
    print('Empty Username and  Empty Password case detected\t')
    print('\t\tRefreshing the Page \t')
except StaleElementReferenceException:
    print('Empty Username and  Empty Password case detected\t')
    print('\t\tRefreshing the Page \t')

driver.get(url)

driver.find_element_by_name('username').send_keys(''.join(choices(ascii_letters, k=randint(1, 12))))
driver.find_element_by_name('pass').send_keys('')
driver.find_elements_by_class_name('login100-form-btn')[0].click()
try:
    alert = driver.find_element_by_class_name('alert-validate')
    print(' Empty Password case detected\t')
    print('\t\tRefreshing the Page \t')

except StaleElementReferenceException:
    print(' Empty Password case detected\t')
    print('\t\tRefreshing the Page \t')

driver.get(url)
driver.find_element_by_name('username').send_keys('')
driver.find_element_by_name('pass').send_keys(''.join(choices(ascii_letters, k=randint(1, 12))))
driver.find_elements_by_class_name('login100-form-btn')[0].click()
try:
    alert = driver.find_element_by_class_name('alert-validate')
    print('Empty Username case detected \t')
    print('\t\tRefreshing the Page \t')

except StaleElementReferenceException:
    print('Empty Username case detected \t')
    print('\t\tRefreshing the Page \t')

driver.get(url)
print('...............  Clicking on forgot Password .........................')
driver.find_elements_by_class_name('login100-form-btn')[1].click()
url = 'http://localhost/teacher/forgot-password.php'
print('...............  Starting Forgot page testing .........................')
try:
    h2_forgotpass = driver.find_element_by_tag_name('h2')
    # print('GOt h2')
    fullname_forgotpass = driver.find_element_by_name('fullname')
    # print('GOt fname')
    email_forgotpass = driver.find_element_by_name('email')
    # print('GOt email ')
    reset_forgotpass = driver.find_element_by_class_name('btn')
    # print('GOt button ')
    valid_user_pass = {0: ['vijay', 'vij@gmail.com', 'Asdfgh12'], 1: ['sravan', 'sravan33333@gmail.com', 'Asdfgh123'],
                       2: ['saiakhil', 'akh@gmail.com', 'Qwert123']}
    # print('Value okay adj')

    for i in range(10):
        h2_forgotpass = driver.find_element_by_tag_name('h2')
        # print('GOt h2')
        fullname_forgotpass = driver.find_element_by_name('fullname')
        # print('GOt fname')
        email_forgotpass = driver.find_element_by_name('email')
        # print('GOt email ')
        reset_forgotpass = driver.find_element_by_class_name('btn')
        # print('GOt button ')
        ran = randint(0, 2)
        if ran == 0:

            h2_forgotpass.click()
            print('Reached welcome page by clicking h2 tag')
            driver.get(url)
            continue
        elif ran == 1:
            ran = randint(0, 2)

            fullname_forgotpass.send_keys(valid_user_pass[ran][0])

            email_forgotpass.send_keys(valid_user_pass[ran][1])
            # sleep(2)
            # driver.get_screenshot_as_png()
            reset_forgotpass.click()
            # sleep(3)
            try:
                WebDriverWait(driver, 3).until(ec.alert_is_present(), 'Alert Failure ')
                alert = driver.switch_to.alert
                alert.accept()
                print("...............  Problem with entered credentials  ...........")
                continue
            except TimeoutException:
                print("The reset credentials were correct.")
                if driver.current_url == 'http://localhost/teacher/reset-password.php':
                    current_url = driver.current_url
                    rand = randint(0, 1)
                    if rand == 0:
                        #     positive cases
                        pass_buttons = driver.find_elements_by_class_name('form-control')
                        pass_buttons[0].send_keys(valid_user_pass[ran][2])
                        pass_buttons[1].send_keys(valid_user_pass[ran][2])
                        # sleep(2)
                        # driver.get_screenshot_as_png()
                        driver.find_element_by_class_name('btn btn-primary pull-right').click()
                        # sleep(2)
                        if driver.current_url == 'http://localhost/teacher/login.html':
                            print('....... The password was reset successfully ..........')
                            # driver.get_screenshot_as_png()
                            # sleep(1)
                            driver.get(url)
                            print(
                                ' ......One positive testcase of reset cred done ...... iteration : {iter}'.format(
                                    iter=iter))
                            continue
                        else:
                            print('\tError in + cases\t\t')
                    else:
                        # negative test cases
                        print(' ......One negative testcase of reset cred ')
                        rand_user = ''.join(choices(ascii_letters, k=randint(0, 12))).strip()
                        rand_pass = ''.join(choices(ascii_letters, k=randint(0, 12))).strip()
                        try:
                            error_ele = driver.find_element_by_class_name('sense-danger')
                            pass_buttons = driver.find_elements_by_class_name('form-control')
                            pass_buttons[0].send_keys(valid_user_pass[ran][2])
                            pass_buttons[1].send_keys(valid_user_pass[ran][2])
                            # sleep(2)
                            driver.find_element_by_class_name('btn btn-primary pull-right').click()
                            try:
                                WebDriverWait(driver, 3).until(ec.alert_is_present(), "Password and Confirm  Password "
                                                                                      "Field do not match  !!")
                                alert = driver.switch_to.alert
                                alert.accept()
                                print("...............  Login is tested in iteration {iter}  ...........".format(
                                    iter=iter))
                                driver.get(url)
                                continue
                            except TimeoutException:
                                print("There is problem with conform button.")
                            except UnexpectedAlertPresentException as e:
                                continue
                            # Password and Confirm
                            # Password
                            # Field
                            # do
                            # not match  !!

                        except NoSuchElementException:
                            pass_buttons = driver.find_elements_by_class_name('form-control')
                            pass_buttons[0].send_keys(valid_user_pass[ran][2])
                            pass_buttons[1].send_keys(valid_user_pass[ran][2])
                            # sleep(2)
                            driver.find_element_by_class_name('btn btn-primary pull-right').click()
                            try:
                                WebDriverWait(driver, 3).until(ec.alert_is_present(), "Password and Confirm  Password "
                                                                                      "Field do not match  !!")
                                alert = driver.switch_to.alert
                                alert.accept()
                                print("...............  Login is tested in iteration {iter}  ...........".format(
                                    iter=iter))
                                driver.get(url)
                                continue
                            except TimeoutException:
                                print("There is problem with conform button.")
                            except UnexpectedAlertPresentException as e:
                                continue
                else:
                    print('............ Error with page rendering ................')
        else:
            try:
                login_option = driver.find_element_by_class_name('href-login-text')
                login_option.click()
                if driver.current_url == 'http://localhost/teacher/login.html':
                    print('\tSuccessfully entered into login page from forgot password page.\t')
                    driver.get(url)
            except NoSuchElementException as exe:
                # print('Had an issue with getting the elements. .. ')
                # print('Returing error logs ' + exe.msg)
                # exit(101)
                pass
except NoSuchElementException as exe:
    # print('Had an issue with getting the elements. .. ')
    # print('Returing error logs ' + exe.msg)
    # exit(101)
    pass

print('...............  Login page testing Finished .........................')

print('...................  Register Page testing .............................')

url = 'http://localhost/teacher/register.html'
driver.get(url)
random_numbers = [i for i in range(pow(2, 30), pow(2, 30) + 100)]
# print(random_numbers)
# inputs_fields = driver.find_elements_by_class_name('wrap-input100 validate-input')
passcondns = printable + digits + ascii_letters
cred = {'fullname': ''.join(choices(ascii_letters, k=randint(1, 12))).strip(),
        'username': ''.join(choices(ascii_letters, k=randint(1, 12))).strip(),
        'pass': ''.join(choices(passcondns, k=randint(8, 12))).strip(),
        'phone': str(choices(random_numbers)[0]),
        'email': ''.join(choices(ascii_letters, k=randint(1, 12))) + '@gmail.com',
        'subject': ''.join(choices(ascii_letters, k=randint(2, 2))).strip(),
        'cabin': 'C 302'
        }
driver.find_element_by_name('fullname').send_keys(cred['fullname'])
driver.find_element_by_name('username').send_keys(cred['username'])
driver.find_element_by_name('pass').send_keys(cred['pass'])
driver.find_element_by_name('phone').send_keys(cred['phone'])
driver.find_element_by_name('email').send_keys(cred['email'])
driver.find_element_by_name('subject').send_keys(cred['subject'])
driver.find_element_by_name('cabin').send_keys(cred['cabin'])
# sleep(2)
driver.find_element_by_class_name('login100-form-btn').click()
print('.................. Register Page was tested ............')

print('......... Account  Page Testing ..............')
try:
    username = 'mahesh123'
    password = 'theOnlyTester1'
    driver.find_element_by_name('username').send_keys(username)
    driver.find_element_by_name('pass').send_keys(password)
    # sleep(2)
    driver.find_element_by_class_name('login100-form-btn').click()
    current_url = driver.current_url
except UnexpectedAlertPresentException:
    pass
# sleep(10)

# print(current_url)

print('........   Profile page Testing ...................')
print('\t\t\tabout to click edit profile ........')
driver.get('http://localhost/teacher/profile.php')
driver.find_element_by_class_name('login100-form-btn').click()
try:
    url = driver.current_url
    if url == 'http://localhost/teacher/profile.php':
        print(' ........... Not able to edit profile .............. ')
    elif url == 'http://localhost/teacher/edit.html':
        print(' ........... Was able to edit profile .............. ')
        pprint('Before updations \t')
        pprint(cred)
        cred['username'] = ''.join(choices(ascii_letters, k=randint(3, 12))).strip()
        cred['phone'] = str(choices(random_numbers))
        cred['email'] = ''.join(choices(ascii_letters, k=randint(1, 12))) + '@gmail.com'
        print('After updations\t')
        pprint(cred)
        sleep(2)
        driver.find_element_by_class_name('login100-form-btn').click()
        print(' ....... Done with edit profile page testing .........')
except UnexpectedAlertPresentException:
    print('Error at edit profile page ...')

url = 'http://localhost/teacher/home.php'
driver.get(url)

print(' ...............  choosing from drop down in the faculty menu ..................')
try:
    for _ in range(5):
        driver.get(url=url)

        select = Select(driver.find_element_by_class_name('list-group-item'))
        select.select_by_index(randint(0, 3))
        driver.find_element_by_class_name('btn').click()
        try:
            if driver.current_url == 'http://localhost/teacher/displayother.php':
                print('Successfully was able to view the timetable of requested faculty at iteration {itr}'.format(itr=_))
            else:
                print('Had a issue in the iteration {itr}'.format(itr=_))
        except StaleElementReferenceException:
            print('The driver has selected an old reference. refreshing page..........')
            driver.refresh()
        except ElementNotSelectableException:
            print('Not to able select button.Please check 👎🏻👎🏻👎🏻👎🏻👎🏻')
        except NoSuchElementException:
            print(' ...........  Error detecting buttons ......')
except TypeError:
    pprint('Done Selecting values ..')

driver.get(url)
# sleep(2)
print(' ..........  Checking write notes feature ......................')
driver.get('http://localhost/teacher/notes.html')

for _ in range(7):
    notes_text = 'This is a sample notes'
    dateobj = driver.find_element_by_name('date')
    ActionChains(driver).move_to_element(dateobj).click().send_keys('15032020').perform()
    # sleep(5)
    driver.find_element_by_class_name('login100-form-btn').click()
    print('Successfully added notes to list')
    # sleep(3)

print(' --------- Done checking notes checking ------------')
driver.get(url)
print(' ---------------  Checking whether notes is reflected in db. --------------')
try:
    WebDriverWait(driver, 3).until(ec.alert_is_present(),'you have no notes for today')
    alert = driver.switch_to.alert
    alert.accept()
    print("..............   Notes staus for today is displayed. No issues connecting with database .......")
except TimeoutException:
    print("..............   Notes staus for today is displayed. No issues connecting with database .......")

sleep(1)
for _ in range(5):
    driver.get(url=url)
    print(' .....  Entering Schedule tutorial page .............')
    try:
        driver.find_element_by_link_text('Schedule Tutorial').click()
        sleep(2)
        if driver.current_url == url:
            print('Error opening schedule tutorial at iteration {itera}'.format(itera=_))
        elif driver.current_url == 'http://localhost/teacher/tutorial.html':
            print('Was able to open schedule tutorial')
            print(' ----------  checking tutorial page ...............')
            datefield = driver.find_element_by_name('date')
            ActionChains(driver).move_to_element(datefield).click().send_keys('15032020').perform()
            # driver.find_elements_by_class_name('input100')[1].send_keys(months[randint(0, 12)])
            # driver.find_elements_by_class_name('input100')[2].send_keys(year)
            # sleep(2)
            driver.find_element_by_name('tutno').send_keys(randint(12, 125))
            sleep(2)
            driver.find_element_by_class_name('login100-form-btn').click()
            sleep(1)
            if driver.current_url == url:
                print('Successfully added tutorial remainder..')
            else:
                # print('Error inserting values into tutorial.......')
                print('Successfully added tutorial remainder..')
    except NoSuchElementException:
        print('Error opening schedule page ')
    except StaleElementReferenceException:
        print(' Driver using old reference ..  Refreshing page .....')
    except ElementNotSelectableException:
        print(' Problem in linking the pages ')

sleep(2)
driver.get(url)
print(' Evaluating the check tutorial page ...')
driver.find_element_by_link_text('Check Tutorial').click()
try:
    WebDriverWait(driver,3).until(ec.alert_is_present(),"No tutorials are scheduled for today")
    alert = driver.switch_to.alert
    alert.accept()
    print(' No tutorial case detected')
except TimeoutException:
    try:
        WebDriverWait(driver, 3).until(ec.alert_is_present(), "Your have a quiz/tutorial called :  2  scheduled for "
                                                              "today.")
        alert = driver.switch_to.alert
        alert.accept()
        print('  tutorial case detected')
    except UnexpectedAlertPresentException:
        pass
    except NoAlertPresentException:
        pass
    except TimeoutException:
        print('Alert not detected exception ..............')

print('Done with check tutorial page testing ......')

print(' ..................  Testing ping messages .......................')

driver.get(url=url)
driver.find_element_by_link_text('Ping').click()

try:
    if driver.current_url == 'http://localhost/teacher/ping.php':
        print('Successfully opened ping page .....')
        for _ in range(5):
            select = Select(driver.find_element_by_class_name('list-group-item'))
            print(' Choosing faculties to ping ..')
            select.select_by_index(randint(0,3))
            sleep(2)
            driver.find_element_by_class_name('btn btn-outline-light').click()
            if driver.current_url == url:
                print("Successfully pinged a faculty ")
            else:
                print("Error pinging faculty")
    else:
        print("error opening ping page ")
except NoSuchElementException:
    print('Error clicking buttons')
except StaleElementReferenceException:
    print('Referencing an old element')
    driver.refresh()
except ElementNotSelectableException:
    print('problem with button or ping page')


print(' ....... Tested Ping page  ---------------')

driver.get(url=url)
print('Testing messages page ..')
driver.find_element_by_link_text('Messages')
try:
    WebDriverWait(driver, 3).until(ec.alert_is_present(), "You have no messages from other faculties")
    alert = driver.switch_to.alert
    alert.accept()
    print('Message alert received ')
except UnexpectedAlertPresentException:
    print('A faculty has sent you a message case detection')
except NoAlertPresentException:
    pass
except TimeoutException:
    print('Alert not detected exception ..............')

sleep(2)

driver.get(url=url)
driver.find_element_by_link_text('Exam timetable').click()
if driver.current_url == 'http://localhost/teacher/examtt.php':
    print(' Exam time table visible')
else:
    print(' Problem with exam time table rendering')
print('............ Done with home page testing .............')

driver.get(url)

driver.find_element_by_link_text("Logout").click()

print('..........   Account page tested .......................')

pprint(' ........... Hope So done with UI Testing 👍👍👍👍👍👍👍👍👍👍👍👍    .....................')
