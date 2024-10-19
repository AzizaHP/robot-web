*** Settings ***
# Use Selenium WebDriver and Applitools Eyes.
Library     SeleniumLibrary

*** Variables ***
${url}  https://www.saucedemo.com/
${username}     visual_user
${password}     secret_sauce
${first_name}   aziza
${last_name}    regina
${postal_code}  72113

*** Keywords ***
Open New Page Browser
    Open Browser    ${url}  Chrome

Input credential
    Input Text  id=user-name    ${username}
    Input Text  id=password     ${password}

Click Login
    Click Button    id=login-button
    sleep       2s

Click Sauce Labs Bike Light
    Click Element   id=item_0_title_link

Click Shopping Cart
    Click Element   id=shopping_cart_container

Click Checkout
    Click Button    id=checkout 

Input Buyer Information
    Input Text  id=first-name   ${first_name}
    Input Text  id=last-name    ${last_name}
    Input Text  id=postal-code  ${postal_code}
    sleep   2s

Click Continue
    Click Button    id=continue
    sleep   2s

CLick Finish
    Click Button    id=finish

*** Test Cases ***
Setup
    Given Open New Page Browser
    When Input credential
    And Click Login
    And Click Shopping Cart
    And Click Checkout
    And Input Buyer Information
    And Click Continue
    Then Click Finish