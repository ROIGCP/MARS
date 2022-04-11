# MARS Demonstration
Monitoring, Auditing and Reporting System (MARS)
 
## Clone in the Repo
Open Cloud Shell\
Clone in the `https://github.com/ROIGCP/Mars` repo\
    Command: `git clone https://github.com/ROIGCP/Mars`\
    Command: `cd Mars`

## GETTING MARS WORKING IN CLOUDSHELL
Make sure you have a project set\
    Command: `gcloud config set project YOURPROJECTNAME`

Bucket named projectid-bucket\
    Command: `gsutil mb gs://$GOOGLE_CLOUD_PROJECT"-bucket"`
    
Dataflow API enabled  (enabled via script in run-cloud.sh)\
    Command: `gcloud services enable dataflow.googleapis.com`

BigQuery Dataset called "mars"\
    Command: `bq mk mars`

BigQuery Table called "activities" - starting schema\
    Command: `bq mk --schema timestamp:STRING,ipaddr:STRING,action:STRING,srcacct:STRING,destacct:STRING,amount:NUMERIC,customername:STRING -t mars.activities`
    
    `Schema: (if you want to create manually)
        timestamp:STRING,
        ipaddr:STRING,
        action:STRING,
        srcacct:STRING,
        destacct:STRING,
        amount:NUMERIC,
        customername:STRING`

Run the Local Version (in Cloud Shell)\
(also installs the required components - review the scripts and code before running)\
Command: `./run-local.sh`

Run the Cloud Version (in Cloud Shell)\
(also installs the required components - review the scripts and code before running)\
Command: `./run-cloud.sh`

Buckets with Moonbank Data\
Sample Data Bucket (7x small files): `gs://mars-sample`\
Production Data Bucket (300+ larger files): `gs://mars-production`

## Data Studio Dashboard 
Make a Copy of this Data Studio Dashboard and adjust to your project.dataset.table\
    URL: `https://datastudio.google.com/reporting/3f79b633-ac24-43b3-86c8-41f386ea514a`

## Conversion to Pub/Sub and BigQuery
The Streaming examples (located in `/streaming/`) have been adjusted to read a pub/sub topic and write into BigQuery\
However - they only write the data into a single column (`message:string`) in a table named `raw`\
Streaming inserts expect data formatted in JSON instead of CSV

## GETTING MARS STREAMING WORKING IN CLOUDSHELL
BigQuery Dataset called `mars` and a table `raw`\
Command: `bq mk mars`\
Command: `bq mk --schema message:STRING -t mars.raw`

Subscribe to the Mars Activity Topic\
Command: `gcloud pubsub subscriptions create mars-activities --topic projects/roi-mars/topics/activities`\
Alternate (if you don't have access to topic): create a pubsub topic and subscription in your own project, and post messages for testing

Run the Local Version (in Cloud Shell)\
(also installs the required components - Review the scripts and code BEFORE running)\
Command: `cd streaming`\
    Command: `./run-stream-local.sh`

Run the Cloud Version (in Cloud Shell)\
(also installs the required components)\
    (Review the script and mars-cloud.py BEFORE running)\
    Command: `./run-stream-cloud.sh`

## CHALLENGE
Adjust the transformation function (`processline`) to create the JSON that represents the row and adjust to insert the row into the `mars.activity` table

