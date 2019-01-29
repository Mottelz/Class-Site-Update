# Class-Site-Update

A simple python program to check if there's been an update to a class website.

## Description

This project notifies me every time my professor updates the class website by putting a .txt file on my desktop. The program is run as a crontab job every few hours. The md5 checksum of each webpage I'm watching is used to track if any changes have been made since the last check. The most recent checksum is stored in the data.json file.

## Requirements

You need **python3** for this to work. Here's a easy to follow tutorial to install in on your mac: https://wsvincent.com/install-python3-mac/ You'll also need something to edit the code I recommend getting [**Visual Studio Code**](https://code.visualstudio.com/). 

## Changes You Need to Make Before Use

These are the things you need to change before using this project (all changes need to be made to class-site-update.py):

- Set the url(s) to the webpage(s) you wish to track. (Lines 32-35)
- Change the variable name(s) for each md5 token to match in their declaration (Lines 32-35), their use (Lines 40-51), and in the data.json file.
- Make sure all file paths are correct. (Lines: 37, 55, and 58)

## How to use on a mac (or linux)
1. Download this repo.
2. Unzip it.
3. Make sure you've already installed the Requirements and made the changes you need to make (see the above two sections of this doc).
4. Open Terminal. 
5. In Terminal type `cd ` (make sure there's a space after it) and then click and drag the folder into it. Then Press enter.
6. In Terminal type `python3 class-site-update.py` and press Enter.

### Potential Future Plans

If you can think of anything this program is missing, let me know.

- Setup a better notification system (maybe even using macOS's internal notices).
