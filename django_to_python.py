#!usr/bin/python
    
import os
    
os.system('yum -y install python-pip')
os.system('pip install virtualenv')
os.system('pip install --upgrade pip')
   
##mkdir and cd into
os.mkdir('/opt/django')
os.chdir('/opt/django/')
    
##running python 2 but want 3.6
os.system('yum -y install python36')
os.system('virtualenv -p python36 django')
print("Good-to-Go")   
os.system('source /opt/django/django/bin/activate && pip install django')
print("Good-to-Go")
    
##still in 2.7.5 && need to source to 3.6
os.chdir('/opt/django')
print("Good-to-Go")
os.system('source /opt/django/django/bin/activate ' + \
          '&& django-admin --version ' + \
          '&& django-admin startproject project1')
print("Good-to-Go")   
##start project
    
##change ownership from root to a user
os.system('chown -R g42dfyt /opt/django')  ##if you don't know this--: who
print("Good-to-Go")
os.system('chown -R g42dfyt /opt/django/project1')
print("Good-to-Go")
os.system('sudo -u g42dfyt  sh -c "source /opt/django/django/bin/activate && python /opt/django/project1/manage.py runserver 0.0.0.0:8000&" ')
print("Good-to-Go")   
##activate django install and run server
