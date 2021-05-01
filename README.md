# MARS Demonstration
Monitoring, Auditing and Reporting System (MARS)\
NOTE: there seems to be a bug in one of the dependancies for Apache Beam.\
I've updated the `requirements.txt` to pin `apache-beam[gcp]==2.8.0` which will resolve the issue.
 
## Clone in the Repo (example using Google Cloud Shell.)
Open Cloud Shell\
Clone in the `https://github.com/ROIGCP/Mars` repo\
    `Command: git clone https://github.com/ROIGCP/Mars`\
    `Command: cd Mars`

## GETTING MARS WORKING IN CLOUDSHELL
Make sure you have a project set\
    `Command: gcloud config set project YOURPROJECTNAME`

Bucket named projectid-bucket\
    `Command: gsutil mb gs://$GOOGLE_CLOUD_PROJECT"-bucket"`
    
Dataflow API enabled  (enabled via script in run-cloud.sh)\
    `Command: gcloud services enable dataflow.googleapis.com`

BigQuery Dataset called "mars"\
    `Command: bq mk mars`

BigQuery Table called "activities" - starting schema\
    `Command: bq mk --schema timestamp:STRING,ipaddr:STRING,action:STRING,srcacct:STRING,destacct:STRING,amount:NUMERIC,customername:STRING -t mars.activities`
    
    `Schema: (if you want to create manually)
        timestamp:STRING,
        ipaddr:STRING,
        action:STRING,
        srcacct:STRING,
        destacct:STRING,
        amount:NUMERIC,
        customername:STRING`

Make a Copy of this Data Studio Dashboard and adjust to your project.dataset.table\
    `URL: https://datastudio.google.com/reporting/3f79b633-ac24-43b3-86c8-41f386ea514a`

Clone this Git Repository into your Cloud Shell\
    `Command: git clone https://github.com/ROIGCP/Mars`\
    `Command: cd Mars`

Run the Local Version (in Cloud Shell)\
(also installs the required components)\
    (Review the script and mars-local.py BEFORE running)\
    `Command: ./run-local.sh`

Run the Cloud Version (in Cloud Shell)\
(also installs the required components)\
    (Review the script and mars-cloud.py BEFORE running)\
    `Command: ./run-cloud.sh`


Buckets with Moonbank Data\
Sample Data (2x small files): `gs://roi-mars/sample`\
Production Data (30x large files): `gs://roi-mars/production`


## CONVERSION TO PUB/SUB

Subscribe to the Mars Activity Topic\
`command: gcloud pubsub subscriptions create mars-activities --topic projects/roi-mars/topics/activities`

To include google-cloud-pubsub - add the following line to `requirements.txt`\
    `Line to add: google-cloud-pubsub==1.7.0`

The Challenge: Convert to processing the newly created Subscription instead of the files in GCS\
Hints are located in the streaming folder of this git repo.
