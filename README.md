# App Monitor client.
Purpose of this module is to extract system python package versions, System OS/Version and Django version.

# Requirements
- Python (3.x.x)


# Environment settings

These configuration settings provided by the appmonitor system. 

    APP_MONITOR_URL=
    APP_MONITOR_PLATFORM_ID=
    APP_MONITOR_APIKEY=
    APP_MONITOR_AUTH_ENABLED=False
    APP_MONITOR_AUTH_USER=
    APP_MONITOR_AUTH_PASS=

# Management Script

```
[appmonitor_client]   
    appmonitor_check   

```

# Python (PIP) dependencies 

```
    python-decouple==3.8
    git+https://github.com/dbca-wa/appmonitor_client.git#egg=appmonitor_client
```
# Python (Poetry) dependencies 

```
    python-decouple = "^3.8"
    appmonitor_client = {git = "https://github.com/dbca-wa/appmonitor_client.git", rev="main"}
```



# django INSTALLED_APPS

```
INSTALLED_APPS = [
    'appmonitor_client'
]
```

# Cron job

```
CRON_CLASSES = [
    'appmonitor_client.cron.CronJobAppMonitorClient',
]

```
# Management Script 

This management script is called by the cron job sync the system with the App Monitor.   

```
python manage.py appmonitor_check

```
