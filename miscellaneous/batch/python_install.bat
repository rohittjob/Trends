@echo off
for %%A in ("%~dp0.") do set parent=%%~dpA

C:\windows\system32\msiexec /a "%parent%dependencies\python-2.7.10.amd64.msi" /qn+
