# Microscope Automation Project
The tests are written in python , the test framework in use is robot framework.
More about the framework can be found at https://robotframework.org.

### Description

This automation tests the Microscope system.

#### project structure:

* `Controllers` - This folder contains classes that implement the interface to the tested 
  systems / hardware / sensors that are required for the automations to run.
* `Resources` - This folder contains resource files for the automations, like testdata files and configurations.
* `TestSuites` - This folder contains Robot files with the actual tests.
* `Validations` -  This folder contains the python classes that implement the keywords in the robot tests.
* `Utils` - This folder contains helper functions and classes.

## Installation:

The project is based on python 3.9
To install the dependencies run (preferable in virtualenv)  
`pip install -r requirements.txt`  

## Excecution

The execution line is as follows:

`robot -P . -V "env.yml" --listener robotframework_reportportal.listener -i sanity TestSuites`

* `-P` adding current folder to path
* `-V` path to the file the contains the configuration file
* `-i` optional run only tests in the path with the included tag
* `--robotframework_reportportal.listener` optional if we want to send the tests run results to report portal.

another way to run the automation is to run the batch file RunTests.bat and optionally
provide the number of time to run the test or the suite/file path, for example:

`RunTests.bat 4 TestSuites` will run, all the robot files under TestSuites folder 4 times, its possible to add test tags also.


## Reporting

* local html report and html log are created in the automation folder.
* all the runs logs and reports are sent to report portal (endpoint can be seen in env.yml)

### configuring report portal:
* pip install the requirements
* deploy report portal on a machine, information can be found here: https://reportportal.io/docs/category/installation-steps/
* configure the next fields in env.yml  
`RP_UUID:` can be found in the report portal settings  
`RP_ENDPOINT:` default on a local machine is http://localhost:8080, but should be the hosting machine's ip or url.  
`RP_LAUNCH:` generic name for the execution   
`RP_PROJECT:` name of the project can be found in the report portal settings

