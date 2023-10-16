# MAKE SURE GCP PROJECT IS SET
# gcloud config set project PROJECT_ID
echo $GOOGLE_CLOUD_PROJECT

sudo pip3 install -r requirements.txt
gsutil -m cp gs://mars-sample/*.csv sample/
# Future: this should be replaced with gcloud storage cp gs://mars-sample/*.csv sample/
rm -R output
python3 mars-local.py
gsutil cp output/* gs://$GOOGLE_CLOUD_PROJECT"-bucket/local/"
bq load --replace=true mars.activities gs://$GOOGLE_CLOUD_PROJECT"-bucket/local/*" 
