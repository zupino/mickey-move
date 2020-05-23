# mickey-move
OpenCV based movement detector.

## A programmable photo-trap
The script uses a camera to analyze a video stream and store an image screenshot only in case movement is detected, it is useful when you want to observe an area and take a screenshot only when something happen. 

This project was firstly created to collect evidence about mouse presence in our garage, became eventually useful to observe the behavior of some animals when they did not know to be observed. In the example below, you see a sequence of image of a bird stealing our strawberries

![Now I know your face](mickey-move-fragole.gif)

## Pre-requisite
This script needs Python3 and related OpenCV libraries. In my specific case, OpenCV has to be cross compiled for ARM to make it run on Raspberry Pi.

This program was tested using Python version of OpenCV 4.1.1.

Note: to run a service on RPi and let it run after disconnectin ssh session, look at `screen` https://www.tecmint.com/keep-remote-ssh-sessions-running-after-disconnection/

http://www.marcozunino.it/mickey-move/mickey-move-fragole.gif
