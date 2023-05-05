*** Settings ***
Library  Utils.DataFileReader
Library  Validations.ValidateZAxisMovement  ${microscope_config_path}   ${laser_config_path}


Suite Setup
Suite Teardown

*** Test Cases ***
Move Z Sanity
    [Tags]  Sanity  Motor
    # read vector data from the CSV file
    ${data}=    read csv    ZAxisSanity.csv
    ${result}=  run sanity  ${data}
    should be true      ${result}

*** Keywords ***
Move Motor
    [Arguments]  ${vector}
    # call the Python function to move the motor
    Run Keyword  run keyword and ignore error  motor.move_motor  ${vector}