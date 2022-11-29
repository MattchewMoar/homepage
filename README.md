# Personal Profile Page in Django
 This is basic and very as of now unfinished profile page done with Django the background image was produced by Dalle 2 with the prompt "“greyscale image fractal nodes of a network, impressionistic”. While basic and far from sophisticated this project might help some as a starting point for their
 own project if so note that in settings.py you should change the secrete key (this project defaults to changeme) to a secure one that you generate. 
 ```

from django.core.management.utils import get_random_secret_key

# print your random secret key 
print(get_random_secret_key())
 ```
 is an easy way from the python interpreter to generate a safe key to use in your own project
 ## Tips
 
 ### Migrations
 Any changes to any of your models must be followed by 
 ```
 $python manage.py makemigrations appname
 $python manage.py migrate
 ```
 if deploying to a service like pythonanywhere, you must also restart the web app for changes to apear. 
 ### Static Files
 
When searching through tutorials and documentations you will find many different directory structures for Django projects. The most frustrating problem i encountered setting up
this project was correctly setting path variables in setting.py so my app would correctly read static files. Most of these problems were caused by mixing code from multiple sources which were
setup with conflicting paths set in settings.py. My suggestion is to carefully reading and understand the sections of the offical django tutorial relating to path settings and
the suggested file structure for static files, also before any changes will be seen on the website you must have django collect these files with
```
$python manage.py collectstatic
```
Also to save yourself some hairpulling. Browsers often store website files in their cache, sometimes for a suprising amount of time. Remember that changes to images, scripts and css files may not appear unless you clear your browsers cached data. Personally I installed the chrome extention cache killer which when activated forces the bowser to reload resources on each refresh. 
 
 ## TODO
 1. Add user to add images to project posts.
 2. Make flex box format look better
 2. Make neat looking contact page. Shoot me a text button using twillo? Could this cause me huge problems?
 3. Add a page for my pet GIS project. Have you ever wanted to search open source Franklin County Auditor Data?! Well Look Out!
 
