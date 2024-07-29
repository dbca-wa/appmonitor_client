"""APP Monitor Django Application Cron Jobs."""

# Standard
import logging

# Third-Party
from django import conf
from django.core import management
import django_cron

# Logging
log = logging.getLogger(__name__)

class CronJobAppMonitorClient(django_cron.CronJobBase):
    """Cron Job for the Catalogue Scanner."""
    RUN_ON_DAYS = [0,1,2,3,4,5]
    RUN_AT_TIMES = ['9:15']
    schedule = django_cron.Schedule(run_on_days=RUN_ON_DAYS,run_at_times=RUN_AT_TIMES)
    code = "appmonitor_client.appmonitor_check"

    def do(self) -> None:
        """Perform the Scanner Cron Job."""
        # Log
        log.info("Provide a list of package to appmonitor_client.")

        # Run Management Command
        management.call_command("appmonitor_check")
        return "Job Completed Successfully"
    
