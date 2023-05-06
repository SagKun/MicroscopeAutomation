*** Settings ***
Library  Utils.DataFileReader
Library  Validations.ValidateZAxisMovement  ${microscope_config_path}   ${laser_config_path}    ${microscope_key}    ${laser_key}

## can define here things to do before the tests run
Suite Setup
## can define here things to do after the tests finished running
Suite Teardown



*** Test Cases ***
Move Z Sanity
    [Documentation]     this test checks that the step movement in the z axis has the expected step-to-mm ratio.
    ...                 test setup locks all degrees of freedom except z axis, moves the the step vector to z=0.
    ...                 then go over test data csv, and for each row compare, take a laser reading, move the microscope,
    ...                 take another laser reading, and compare to the expected movement in mm.
    [Tags]  Sanity  Motor
    ${setup_result}=    setup zaxis test
    should be true      ${setup_result}
    ${data}=    read csv    ZAxisSanity.csv
    ${test_result}=  run zaxis sanity  ${data}
    should be true      ${test_result}

*** Keywords ***
Move Motor
    [Arguments]  ${vector}
    # call the Python function to move the motor
    Run Keyword  run keyword and ignore error  motor.move_motor  ${vector}