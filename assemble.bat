@echo off

:: pre process
set source_filename=%1
set subsystem=%2
set obj_filename=%source_filename:~0,-4%.obj

:: assembling and linking
echo [+] Assembling file %source_filename%...
ml -c -coff -Cp %source_filename%

echo.
echo [+] Linking file %obj_filename%
if [%2]==[] (
	link -subsystem:console %obj_filename%)
) else (link -subsystem:%subsystem% %obj_filename%)