# Snake - My interpretation of the classic Snake game 
Introduced by the Nokia 6110 in 1997, Snake is a classic retro game where you are a snake who must eat food to grow larger. I wrote the game to get better at OOP (Object-Oriented-programming) and to get a feel as to what to excpect from bigger projects. I also made multiple menus in the game where you can do diffrent actions by clicking buttons on the screen whom I have all made my myself even the buttons and images scatterted around the game. I have already finished this project at the time of making this repository so I made this repository solely for the purpse of showing off my game.

## Overview

### You can pick a speed: 
![](https://media.giphy.com/media/TZnc5GzsOotcJw3pik/giphy.gif)

### The two types of Game Over are: 
![](https://media.giphy.com/media/1OS6sC6roMBzoAXhDQ/giphy.gif) 

and 

![](https://media.giphy.com/media/fGlr3jYb6EpcQawd3M/giphy.gif)

# Installation
This game was made in python `3.10` but im sure other versions work as well cause its not that complicated. Click the green **Code** button at the top and in a dropdown menu click **Download Zip**. 

<arrow pointing at download zip>

Extract the newly downloaded folder and inside of the folder (the parent folder of where the code is) create a [virtual environment](https://github.com/pypa/virtualenv) and pip install [pygame](https://github.com/pygame/), put the folder with the code inside of the newly created venv(virtual environment) and run the .py file labeled **main**. 

<Arrow pointing at main> 

To install pygame run the following command in your shell/bash/terminal:
```bash
pip install pygame
```
Now enjoy playing the awesome game!

# Gameplay:
https://user-images.githubusercontent.com/123867128/217765330-1df5bc8e-12a5-4ad2-85ca-a4827d1033a4.mp4

This is a real game I played on speed mode. btw if you were wondering my record is 276 I have played this game quite a lot cause its super fun.

# The snake and turning
The snake turns very smoothely and even if you click two keys at the same time it will turn both ways in order of how you pressed because I added that functionality to make the snake smoother; when I didnt have it in, it felt choppy and you couln't do those quick rotations or make a staircase but now you can. Another feature that makes the game really come together is the fact that the snake body is seperated instead of clumped together as one big blue blob, it allows better see where the snake body is headed as well as where the tail is and where the tail is going. It is especially helpful when your snake is larger so you can see which paths take you to safety and which do not. For example here we know that we should not take that slim and treacherous path at the top because there is currently no escape and if we look at the path that the snake tail is taking then we know that the path will not open up in time for our arrival.

![](https://user-images.githubusercontent.com/123867128/217461218-aaa110a3-2762-4a78-a2ea-b2ee4825279f.png)

Nonetheless that is the path I took in the example gameplay above and lost.
## Other
#### PS
The game isnt really finished the Rules button in the menu has no function, the AI button neither and I don't plan on finishing them any time soon.

#### PPS 
This is my first github repository im very new to github so sorry if my readme is jumbled and all over the place im still learning.

#### PPPS
The code does used in this game is old and not properly show off my actual skill so just bear that in mind when reading the spaghetti code.

#### PPPPS
I made this game completely on my own and only had breif help on specific issues and errors through the Python Discord help channels. I followed no tutorial whatsoever for any of the code used in this game it is all completely made from scratch.
