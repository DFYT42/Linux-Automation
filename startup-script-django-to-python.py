#!usr/bin/python

#import time
import os

#time.sleep(60.0)

os.system('yum -y install python-pip')
os.system('pip install virtualenv')
os.system('pip install --upgrade pip')
   
##mkdir and cd into
os.mkdir('/opt/django')
os.chdir('/opt/django/')
    
##running python 2 but want 3.6
os.system('yum -y install python36')
os.system('virtualenv -p python36 django')
    
##start project
os.system('source /opt/django/django/bin/activate && pip install django' + \
          '&& django-admin --version ' + \
          '&& django-admin startproject project1')
    
##change ownership from root to a user
os.system('chown -R g42dfyt /opt/django')  ##if you don't know this--: who
#os.system('chown -R g42dfyt /opt/django/project1')
#seek current ip and place in ALLOWED HOSTS
os.system("myip=$(curl -s checkip.dyndns.org | sed -e 's/.*Current IP Address: //' -e 's/<.*$//') && sed -i \"s/ALLOWED_HOSTS = \[\]/ALLOWED_HOSTS = \[\'$myip\'\]/g\" /opt/django/project1/project1/settings.py")
os.system('sudo -u g42dfyt  sh -c "source /opt/django/django/bin/activate && python /opt/django/project1/manage.py runserver 0.0.0.0:8000&" ')

##activate django install and run server
