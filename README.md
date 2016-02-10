# ldap-app

##How to run

```
git clone https://github.com/mooreandrew/ldap-app
```

```
cd ldap-app
```

```
vagrant up
```

```
vagrant ssh
```

```
cd /vagrant
```

```
virtualenv -p python3 ldap-app-venv
source ./ldap-app-venv/bin/activate
```

```
./ldap-app-venv/bin/pip install -r requirements.txt
```

```
export SETTINGS='config.DevelopmentConfig'
export LDAP_HOST=""
export LDAP_BASE_DN=""
export LDAP_USER_DN=""
export LDAP_GROUP_DN=""
export LDAP_USER_RDN_ATTR=""
export LDAP_USER_LOGIN_ATTR=""
```

```
./run.sh
```

Repeat the last 2 steps to change the environment variables (don't change the settings value).

To check if it is working, visit in the browser:

```
http://192.168.42.11:5000/<username>/<password>
```
