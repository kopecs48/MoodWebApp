# MoodWebApp
MoodWebApp allows for users to create new accounts, login, and create mood posts. Each mood post displays a title, body, and streak field after being created by posting to the /mood endpoint. The streak field increaments from the user's most recent post only if the post is from the day before, otherwise it breaks the current streak.

The app is deployed at https://skopec.pythonanywhere.com/ using a free account on pythonanywhere, allowing for a fully functioning Mood API that can be reach from any computer.

The Free version of pythonanywhere allows for the app to utilize: 
* Up to 100 seconds of CPU processing a day 
* Up to 512 MB File Storage

This free version was the most practical choice as it allowed for easy deployment at no cost. If the user pool was scaled up and started to outgrow the current hosting version, there are plenty of options within pythonanywhere to choose from. These options range anywhere from $5 a month with enough power to handle 100,000 hits per day, all the way up to $500 a month which allows you to go well over 1,000,000 hits per day. If a web app was to outgrow pythonanywhere as a whole, there are other viable options like AWS Elastic Beanstalk, Heroku, Google Cloud, and many others.

The tech stack that I opted in for was:
* Python 3.10
* Django Framework
* Django Rest Framework

These specific frameworks were chosen because I have prior experience with them. The DjangoSpotify repository was my senior project for my computer science degree. Django is an excellent framework to build web applications and/or RESTful API's. It is great for building object oriented, multi-paged applications. I chose this over the FLASK framework because it enabled me to build out a more well rounded web app and has a built in database management system support for SQL.

Django's default database is SQLite3. This works perfectly for the project specifactions with a small user pool. It is a server-less database and self contained, however it doesn't have any specific user management functionality making it not the best choice for multiple user access(High write volumes). If the user pool was to be scaled up, the current implementation would prove to be insufficient. On the plus side Django supports PostgreSQL, MariaDB, MySQL, and Oracle. It is possible to swap between any of these making it a perfect fit for most projects. To account for the high write volumes in production, I would opt into PostgreSQL to handle larger write volume, maintain data integrity, and utilize the robust feature set


# Installation
clone this repository using
<pre><code>git clone https://github.com/kopecs48/MoodWebApp.git</code></pre>

Then cd into the directory and create a virtual environment using python
<pre><code>python3 -m venv env</code></pre>

After it is created run the script to activate the virtual environment
* Windows:
  * CMD: <pre><code>env\bin\activate.bat</code></pre>
  * PowerShell <pre><code>env\bin\Activate.ps1</code></pre>
* Linux and Mac
  * <pre><code>source env/bin/activate</code></pre>

Then install all requirements for the project by running:
<pre><code>pip install -r requirements.txt</code></pre>

Lastly to run the project on localhost use:
<pre><code>python .\manage.py runserver</code></pre>

