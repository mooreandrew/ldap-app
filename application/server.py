from application import app
import os
from flask import Flask
from flask_ldap3_login import LDAP3LoginManager

@app.route('/<username>/<password>')
def index(username, password):

    config = dict()

    # Setup LDAP Configuration Variables. Change these to your own settings.
    # All configuration directives can be found in the documentation.
    config['LDAP_HOST'] = os.environ.get('LDAP_HOST')             # Hostname of your LDAP Server
    config['LDAP_BASE_DN'] = os.environ.get('LDAP_BASE_DN')      # Base DN of your directory
    config['LDAP_USER_DN'] = os.environ.get('LDAP_USER_DN')                 # Users DN to be prepended to the Base DN
    config['LDAP_GROUP_DN'] = os.environ.get('LDAP_GROUP_DN')              # Groups DN to be prepended to the Base DN

    config['LDAP_USER_RDN_ATTR'] = os.environ.get('LDAP_USER_RDN_ATTR')                 # The RDN attribute for your user schema on LDAP
    config['LDAP_USER_LOGIN_ATTR'] = os.environ.get('LDAP_USER_LOGIN_ATTR')             # The Attribute you want users to authenticate to LDAP with.
    config['LDAP_BIND_USER_DN'] = None                  # The Username to bind to LDAP with
    config['LDAP_BIND_USER_PASSWORD'] = None            # The Password to bind to LDAP with


    ldap_manager = LDAP3LoginManager()          # Setup a LDAP3 Login Manager.
    ldap_manager.init_config(config)            # Init the mamager with the config since we aren't using an app

    # Check if the credentials are correct
    response = ldap_manager.authenticate(username,password)
    return str(response.status)


@app.route('/simple/<username>/<password>')
def simple(username, password):

    config = dict()

    config['LDAP_HOST'] = os.environ.get('LDAP_HOST')
    ldap_manager = LDAP3LoginManager()
    ldap_manager.init_config(config)

    response = ldap_manager.authenticate_direct_credentials(username,password)
    return str(response.status)
