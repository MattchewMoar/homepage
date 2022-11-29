# homepage
django-homepage app
 This is basic and very as of now unfinished profile page done with Django the background image was produced by Dalle 2 with the prompt "“greyscale image fractal nodes of a network, impressionistic”. While basic and far from sophisticated this project might help some as a starting point for their
 own project. 
 ##Tips##
When searching through tutorials and documentations you will find many different directory structures for Django projects. The most frustrating problem i encountered setting up
this project was correctly setting path variables in setting.py so my app would correctly read static files. Most of these problems were caused by mixing code from multiple sources which were
setup with conflicting paths set in settings.py. My suggestion is to carefully reading and understand the sections of the offical django tutorial relating to path settings and
the suggested file structure for static files, also before any changes will be seen on the website you must have django collect these files with
'''
$python manage.py collectstatic
'''
 
 ##TODO##
 1. Add user to add images to project posts.
 2. Make neat looking contact page. Shoot me a text button using twillo? Could this cause me huge problems?
 3. Add a page for my pet GIS project. Have you ever wanted to search open source Franklin County Auditor Data?! Well Look Out!
 
