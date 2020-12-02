#Time_Display,
Django project with a single app called time_display, it renders a template displaying server current date and time.
When you go to localhost:8000 or localhost:8000/time_display, this should run a method in your controller file (views.py) that renders a template displaying server current date and time. There are many ways to get the current time in Python. For example, you could have views.py import gmtime, strftime from 'time' and pass the appropriate string to the render method. In this small project we use strftime.
#1. The root route ('/') displays the current date and time. For Example: Time: Dec-02-2020 04:33 AM
#2. Own custom stylesheet ('/time2'), a different way to retrieve the datetime, Time: 04:33:01 Wed, 02 Dec 2020

