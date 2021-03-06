#!/usr/bin/python

##https://cloud.google.com/compute/docs/tutorials/python-guide
##centos7

from oauth2client.client import GoogleCredentials
from googleapiclient import discovery

import googleapiclient
import pprint
import json
#import create_ldap
#from cretae_ldap import create_instance

credentials = GoogleCredentials.get_application_default()
compute = googleapiclient.discovery.build('compute','v1', credentials=credentials)

project = "artful-sled-217801"
zone = "us-east1-b"

#machine type requested and name
#machine type helps derive name

name = "final-project-trouble-c"

def list_instances(compute, project, zone):
    result = compute.instances().list(project=project, zone=zone).execute()
    return result['items']
  
def create_instance(compute, project, zone, name):
    # Configure the machine
    startup_script = open('startup-script-apache.sh', 'r').read()
    image_response = compute.images().getFromFamily(project='centos-cloud', family='centos-7').execute()

    source_disk_image = image_response['selfLink']
    machine_type = "zones/%s/machineTypes/f1-micro" % zone
    
    config = {
        'name': name,
        'machineType': machine_type,
        
        # Specify the boot disk and the image to use as a source.
        'disks': [
            {
                'boot': True,
                'autoDelete': True,
                'initializeParams': {
                    'sourceImage': source_disk_image,
                }
            }
        ],

        # Specify a network interface with NAT to access the public
        # internet.
        'networkInterfaces': [{
            'network': 'global/networks/default',
            'accessConfigs': [
                {'type': 'ONE_TO_ONE_NAT', 'name': 'External NAT'}
            ]
        }],

        # Allow the instance to access cloud storage and logging.
        'serviceAccounts': [{
            'email': 'default',
            'scopes': [
                'https://www.googleapis.com/auth/devstorage.read_write',
                'https://www.googleapis.com/auth/logging.write'
            ]
        }],

        #Enable https/http for select instances
        "labels": {
        "http-server": "",
        "https-server": ""
        },
        
        "tags": {
        "items": [
        "http-server",
        "https-server"
        ]
        },
        
        # Metadata is readable from the instance and allows you to
        # pass configuration from deployment scripts to instances.
        'metadata': {
            'items': [{
                # Startup script is automatically executed by the
                # instance upon startup.
                'key': 'startup-script',
                'value': startup_script
           # }, {
               # 'key': 'url',
                #'value': 'IMAGE_URL'
           # }, {
            #    'key': 'text',
             #   'value': 'TEXT'
           # }, {
            #    'key': 'bucket',
             #   'value': 'CS_BUCKET'
            }]
        }
    }

    return compute.instances().insert(
        project=project,
        zone=zone,
        body=config).execute()

newinstance = create_instance(compute,project, zone, name)
instance = list_instances(compute, project, zone)

pprint.pprint(newinstance)
pprint.pprint(instance)
