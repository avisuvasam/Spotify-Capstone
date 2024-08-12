# Spotify-Capstone

By: Ashton Visuvasam, David Firestone

## Note
This project is meant to be exploratory, focusing on the processes of collecting, storing, and analyzing data. There was no concern over the outcome of the analysis or whether we could draw meaningful conclusions. This project was completed for a course at the University of Florida, which is where most of the data was gathered.

## Question
The question we tried to answer was: Were there any relationships between Spotify audio features and the location or time of day people listened to the songs? While this was the main question, there was much more analysis done to get a complete view of the data.

## Data Collection
My partner, David Firestone, handled all of the data collection, although his code is not included in the repository. He created a website where people could recommend a song by inserting a Spotify link, and the song would automatically be added to the bottom of his Spotify queue. The song, along with the time of day and IP address, was collected and stored in a database labeled "test.db" in the repository. We advertised the website link to as many people as possible, with most submissions coming from Gainesville, Florida, where we focused our efforts.

## How the Code Works
The "RUN ONCE.py" file adds songs and audio features from the Spotify API into the database, creating the database used for analysis called "1.db". "RUN ONCE.py" imports from "functions.py" and "vars.py" to run properly. This file was worked on by both David and me.

The "Capstone Presentation.ipynb" is where all of the data analysis was conducted, along with presentation elements to explain the types of analysis done. This file was completed entirely by myself.
