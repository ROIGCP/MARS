#! /bin/bash
# MAKE SURE PROJECT IS SET
# gcloud config set project PROJECT_ID
if [[ -z "${GOOGLE_CLOUD_PROJECT}" ]]; then
    echo "Project has not been set! Please run:"
    echo "   gcloud config set project PROJECT_ID"
    echo "(where PROJECT_ID is the desired project)"
else
    echo "Project Name: $GOOGLE_CLOUD_PROJECT"
    gsutil mb gs://$GOOGLE_CLOUD_PROJECT"-bucket"
    gcloud services enable dataflow.googleapis.com
    bq mk mars
    bq mk --schema message:STRING -t mars.raw
    bq mk --schema timestamp:STRING,ipaddr:STRING,action:STRING,srcacct:STRING,destacct:STRING,amount:NUMERIC,customername:STRING -t mars.activities
fi