from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
@given('url given')
def step_impl(context):
    print('hello')

@when('url select')
def step_impl(context):
    print('url select')


@then('url verified')
def step_impl(context):
    #raise NotImplementedError(u'STEP: Then url verified')
    print('url verified')

# --------------------- Login to Sauce Application ----------------------------------
@given('i open the browser')
def step_impl(context):
    #raise NotImplementedError(u'STEP: Given i open the browser')
    context.driver=driver
    context.driver.implicitly_wait(2)
    context.driver.maximize_window()


@when(u'i enter the application url')
def step_impl(context):
    #raise NotImplementedError(u'STEP: When i enter the application url')
    context.driver.get('https://www.saucedemo.com/')

@when(u'i enter invalid user')
def step_impl(context):
    #raise NotImplementedError(u'STEP: When i enter invalid user')
    context.driver.find_element(By.ID,'user-name').clear()
    context.driver.find_element(By.ID,'user-name').send_keys('standard_user')


@when(u'i enter invalid password')
def step_impl(context):
    #raise NotImplementedError(u'STEP: When i enter invalid password')
    context.driver.find_element(By.ID, 'password').clear()
    context.driver.find_element(By.ID, 'password').send_keys('123456')


@when(u'i click login button')
def step_impl(context):
#    raise NotImplementedError(u'STEP: When i click login button')

    context.driver.find_element(By.ID, 'login-button').click()


@then(u'i verify the invalid user message')
def step_impl(context):
    #raise NotImplementedError(u'STEP: Then i verify the invalid user message')
    #print('Message verified')
    #Epic sadface: Username and password do not match any user in this service
    str=context.driver.find_element(By.XPATH,"//h3[@data-test='error']").text
    assert str == 'Epic sadface: Username and password do not match any user in this service'


