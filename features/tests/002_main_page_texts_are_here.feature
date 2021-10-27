# Created by rapid at 7/08/2021
Feature: # 002 Verify texts(see steps below are here)

  Scenario: # 002 Verify texts(see steps below are here)
    Given Loginpage
    Then Verify text 1 "This service is provided entirely for free and without ads, but the server is not free to run. Please consider making a small contribution towards those costs." is here
    Then Verify text 2 "Bart Busschots" is here
    And Verify text 3 "www.bartb.ie/xkpasswd" is here