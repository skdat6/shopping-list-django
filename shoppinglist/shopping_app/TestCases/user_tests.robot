*** Settings ***
Library     SeleniumLibrary
Library     RequestsLibrary

*** Variables ***
${url}   http://127.0.0.1:8000/
${username}     test12113
${password}     test12113
${email}        test121113@test123.com

*** Test Cases ***
Register Test
    [Tags]    Test user registration
    open browser    http://127.0.0.1:8000/register      chrome
    registerUser
    close browser

Login User Test
    [Tags]    Test user login
    open browser    http://127.0.0.1:8000/user_login/     chrome
    loginUser
    close browser

*** Keywords ***
registerUser

    input text  id:id_username      ${username}
    input text  id:id_email     ${email}
    input password  id:id_password      ${password}
    click button    xpath:/html/body/div/div/div/div/div/div/div/form/input[2]
    close browser



loginUser
    input text  id:email2     ${username}
    input password  id:password2      ${password}
    click button    xpath:/html/body/div/div[2]/div/div/div/div/form/button
    close browser