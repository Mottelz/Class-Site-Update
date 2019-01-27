# Class-Site-Update

A simple python program to check if there's been an update to a class website.

## Description

This project notifies me every time my professor updates the class website by putting a .txt file on my desktop. The program is run as a crontab job every few hours. The md5 checksum of each webpage I'm watching is used to track if any changes have been made since the last check. The most recent checksum is stored in the data.json file.

## Changes You Need to Make Before Use

These are the things you need to change before using this project (all changes need to be made to class-site-update.py):

- Set the url(s) to the webpage(s) you wish to track. (Lines 32-35)
- Change the variable name(s) for each md5 token to match in their declaration (Lines 32-35), their use (Lines 40-51), and in the data.json file.
- Make sure all file paths are correct. (Lines: 37, 55, and 58)

### Potential Future Plans

If you can think of anything this program is missing, let me know.

- Setup a better notification system (maybe even using macOS's internal notices).