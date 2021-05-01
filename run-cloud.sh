# MAKE SURE PROJECT IS SET
# gcloud config set project PROJECT_ID
echo $GOOGLE_CLOUD_PROJECT
gcloud services enable dataflow.googleapis.com

sudo pip3 install -r requirements.txt
python3 mars-cloud.py 
read -p "Wait for Dataflow Job to Finish and then press enter"
bq load mars.activities gs://"$GOOGLE_CLOUD_PROJECT""-bucket"/output/output*