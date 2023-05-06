@echo off

set TimesToRun=%1
set SuitePath=TestSuites

if "%TimesToRun%" == "" (
  echo Error: TimesToRun parameter not specified.
  exit /b 1
)

for /l %%i in (1,1,%TimesToRun%) do (
  robot -P . -V "env.yml" --listener robotframework_reportportal.listener %SuitePath%
)