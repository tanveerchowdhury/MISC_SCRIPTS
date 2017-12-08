#!/bin/sh

# this script will give the list of all the QualysGuard vulnerability
# scans that finished the day before.

LOGIN=username	
PASSWORD=password
APIFQDN=qualysguard.qg2.apps.qualys.com
FINISHED=./finished_scans.csv
RUNNING=./running_scans.csv
OUTPUTDIR=./scan_results
# NDAYS defines the number of days you want to look back to get the finished scans.
# Typically NDAYS should be the maximum number of days that the longest scans is supposed to run in your organisation
NDAYS=5
TMPFILE=./tmp

# set the date of yesterday in a QG readable format YYYY-mm-dd
# YESTERDAY is automatically set to the date of yesterday at midnight (UTC)
# WARNING:
# if running on Linux use :             YESTERDAY=`date -u -d "-1 days" +%Y-%m-%dT00:00:00Z`
YESTERDAY=`date -u -d "-40 days" +%Y-%m-%dT00:00:00Z`
TODAY=`date -u +%Y-%m-%dT%H:%M:%SZ`
FROMDATE=`date -u -v-${NDAYS}d +%Y-%m-%dT00:00:00Z`

# get the list of FInished scans launched yesterday 
echo "Getting the list of FINISHED scans launched after ${YESTERDAY}"
for scanref in `curl -H "X-Requested-With: curl" -u "${LOGIN}:${PASSWORD}" "https://${APIFQDN}/api/2.0/fo/scan/?action=list&state=Finished&show_status=1&launched_after_datetime=${YESTERDAY}&echo_request=1" | grep '<REF>' | sed 's/.*\<REF\>\(.*\)\<\/REF\>/\1/g'`; do
	echo "${scanref}" >> ${FINISHED}
done


# do some cleaning
#sort ${FINISHED} | uniq > ${FINISHED}.tmp && mv ${FINISHED}.tmp ${FINISHED}
#sort ${RUNNING} | uniq > ${RUNNING}.tmp && mv ${RUNNING}.tmp ${RUNNING}

#rm -f ${TMPFILE}

