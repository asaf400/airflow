from airflow import configuration
from airflow.configuration import conf
from base64 import b64decode
import json
CSRF_ENABLED = conf.get('webserver_fab', 'CSRF_ENABLED')
print(CSRF_ENABLED)
if conf.get('webserver_fab','OAUTH_PROVIDERS'):
    print(json.loads(b64decode(conf.get('webserver_fab','OAUTH_PROVIDERS')).decode('utf-8')))

print(conf.get('webserver_fab','AUTH_ROLE_PUBLIC'))
