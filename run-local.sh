# MAKE SURE PROJECT IS SET
# gcloud config set project PROJECT_ID
echo $GOOGLE_CLOUD_PROJECT

sudo pip3 install -r requirements.txt
gsutil cp gs://moonbank-mars-sample/*.csv sample/
rm -R output
python3 mars-local.py
gsutil cp output/* gs://$GOOGLE_CLOUD_PROJECT"-bucket/local/"
bq load --replace=true mars.activities gs://$GOOGLE_CLOUD_PROJECT"-bucket/local/*" 