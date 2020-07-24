@echo off
echo Runnig DNS/DPI from Dragonfly CLI with Natlink.

C:
cd C:\Caster

set currentpath=%~dp0

TITLE Caster: Status Window
"C:\Program Files\PythonEnvironments\caster\python.exe" -m dragonfly load --engine natlink _*.py --no-recobs-messages

pause 1