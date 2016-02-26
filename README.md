# Voice Assistant

## Table of Contents:

 **I. Introduction**
 
 **II. Requirements**
 
 **III. Dependencies**
 
 **IV. Features**

 **V. Install**

 **VII. Contributing**

 **VII. License**

---------------------
## I. Introduction

**Voice Assistant** is a "*voice-controlled personal assistant"* designed for the Linux platform
It is a tool that provides a platform to execute and control some basic tasks on the Linux platform, entirely through voice input.

Source code used in the software can be 
obtained with this URL:<https://gitlab.com/prateek_vij/team12cs243>

## II. Requirements
These following requirements need to be fulfilled if you want to use this package the package

**Operating System :** Ubuntu 14.04

**Hardware :** Microphone or Headphones (for voice input), Speaker(optional)

**Python :** Version 2.7 or higher

**Applications :** The tool is developed for certain application that come along as Default in Ubuntu. 
List of such applications required are:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1. Rhythmbox -  music player (along with required GStreamer Plugins)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2. Videos - default video player for Ubuntu

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3. Document Viewer - Default pdf viewer

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4. Firefox - Mozilla firefox ( Chrome is not supported yet)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Other applications will be added as support for them would be made available

## III. Dependencies
All dependencies are listed in the DEPENDENCIES file.

## IV. Features
The user can access and control multiple applications and features simply through voice input. The tool can take input through microphone in natural language and understand it (only upto certain extent) to perform the expected function. The features include:

1. **Control Media player** and navigate through the Music/Movie Library using voice commands such as 
play and pause a song, change the volume, stop song, next and previous song, shuffle, fast forward, rewind, increase/decrease speed.
2.  **Control basic functions of the Web Browser**  such as 
access tabs, close browser, scroll and search page, zoom, bookmark, back and forward, search a keyword using default search engine.
3. **Navigate the default File Browser**, and perform basic file management operations such as
copy and move file, switching directories, create new directory, open directory, open file, delete files and directories, search current directory.
4. **Access functionalities** that are generally executable only through the terminal such as update system, etc.

A detailed list of specific functionalities shall be included soon after implementation.

##V. Install
To install the package, run 
"python setup.py install"

in the package directory.
Add sudo before the command if needed. The file setup.py is yet to be added.


## VI. Contributing
Please see Authors.txt for the list of Contributors

## VII. License
This application shall be released under GNU GPL v3.