# Created by rapid at 7/9/2021
Feature: # 003 Generate password with default options

  Scenario: # 003 Generate password with default options
    Given Loginpage
    Then Click on all 7 buttons APPLEID, DEFAULT, NTLM, SECURITYQ, WEB16, WEB32, WIFI
    And Click on Generate 3 Passwords button
    Then Verify Passwords Field is not empty and has a content "3" rows and "64" cols
    And Verify STRENGTH Field is not empty and has a content "Good"