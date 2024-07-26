# Line Slicer? 
This repository contains the source code for an attempted 24-hour solo game jam submission hosted at my university by Hack Sussex. 

Line slicer is the generic name I made for the game which I attempted to create in this 24 hours, unfortunately falling short of my aims and being abandoned.

# The Vision
The vision for this game was as a 2D slicing rhythm game. Players would slash their way through objects called 'gates' in a manner similar to Fruit Ninja.
These gates would need to be sliced in rhythm with a provided song, which would create gameplay style similar to osu!: rewarding well-timed slices, and punishing misses or badly timed slices.

All around, I had a pretty solid idea of what I wanted to do for this, as it's a form of gameplay I've wanted in osu! for a while.

# The Execution
I chose to use pygame in this project as I was very confident in my python skills, and had heard of pygame as a game development system using python. Development began, with me picking up pygame as I went, through trial and error and the use of wikis.

I went along. I quickly found that pygame was not as easy to use as I first expected, with it being more of a barebones game framework, rather than a fully fledged game engine. I honestly don't know what I expected from it, but I was still surprised by how barebones it actually was, giving me memories of using JavaFX while learning java.

Development continued into the night with several redbulls being drank. Assets were heavily leaning into the "programmer art" style and I was mainly focussing on making a minumum viable product as a proof of concept.

However, despite the simplistic aim of an MVP, the project ultimately failed.

# What Went Wrong
Using Pygame was a major mistake. 

The issue with Pygame lied in my inability to wrap my head around its drawing and timing systems. Each object on screen has to be manually drawn for each frame through a game loop system. 
Beginners typically struggle with controlling basic movement between frames, so attempting to create automatically moving objects, keep them in sync with the music, handle user input, and using that input to determine whether a 'slice' has been successful or not (all while incredibly sleep deprived) was a bit of a recipe for disaster.

The number of checks I'd have to perform to ensure that slices were successful or not ended up causing major performance issues. Python isn't great for real-time game performance - go figure.



# Lessons Learned
My choice of engine is realistically something that I should've done much more research on. There was a feeling of sunken cost (well, time) if I were to transition over to a game engine like Godoh or Unity, leaving the time I spent learning pygame during the jam as a bit of a waste.

Quite a bit of time has passed between my participation in the game jam, and the creation of this readme.  

This story of 'using pygame because it's python then finding out it's bit crap' is a story I've heard quite a few times now. I worked as a teaching assistant during my final year for a Software Engineering module, which involved a coursework tasking students to make a digital re-creation of the board game 'RISK!'.
Several Students decided to use Pygame due to their comfort with Python. Despite my warnings, many continued with it and found pygame to be clunky, difficult to work with, and generally just being a pain.

<br>

**The key point to take home? Do some research on the tools you're going to use before going out there and blindly using them!**


<br><br><br>

# What Next?
Nothing, I dislike pygame and will not be touching it ever again. 
