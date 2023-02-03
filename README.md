# Tourus - Django API Interview: Music Library 

## Agenda
- 2min - Quick Introductions
- 5min - Interview Setup & Overview
- 40min - Technical Interview
- 5min - Questions
- 2min - Wrap up & next steps

## Rules
- You are allowed to use the internet: google, stackoverflow, chatgpt, etc.
- You can ask your interviewer clarifying questions 

## Tips
- Talk through your choices and decisions


----------------------------------------------------------------


# Technical Inteview
Below is an overview of the tech stack and the open tasks:

## Tech Stack
- Django
  - https://docs.djangoproject.com/en/4.1/
- Django Rest Framework
  - https://www.django-rest-framework.org/
- sqlite3 database

## Tasks
Review these tasks and complete them in order, you may not finish all tasks, that's ok.

### Django Startup
- [ ] Start the django application (click "Run" on the toolbar)
  - Django Admin:
    - https://Django-Interview-Music-Library.thalidanoel1.repl.co/admin/
      - Username: admin
      - Password: admin
  - APIs (using Django Rest Framework):
    - https://Django-Interview-Music-Library.thalidanoel1.repl.co/api/

### Django Models
- [ ] Update Album model to include the award received (Gold, Platinum, Diamond)

### Django Rest Framework
- [ ] Update /tracks GET request to include the track title
- [ ] Update /artist GET request to return a list of albums
- [ ] Update /album GET request to include the artist
- [ ] Update /album GET request to have a field with a list of all the featured artists (see Track Model)
- [ ] Hidden tracks are being returned by the API, fix the api to only return visible tracks
- [ ] Update album responses to include the number of tracks

### Django Admin
- [ ] Update tracks admin table to show the title, is_hidden, and list of the track artists
- [ ] On the album and track edit views show the artist name instead of id
- [ ] Add ability to manage tracks on an album from the album edit view

### Technical Architecture Discussion
- [ ] How would you update the models to specify the track order?
- [ ] What improvments would you make to the current codebase?
- [ ] How would you update the models to also support other people who need credit: songwriters, producers, etc.


----------------------------------------------------------------


# Using Replit
## Running the Django Server
- Click "Run" on the toolbar to start the Django Server

## Installing packages
To add packages to your repl, you can just import directly in the file you want to use the package in, and it will automatically be installed when you press the run button. Like below:
```python
import math
import pandas as pd
```

You could also install packages by using the Replit packager interface in the left sidebar.
