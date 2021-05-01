# MAKE SURE PROJECT IS SET
# gcloud config set project PROJECT_ID
echo $GOOGLE_CLOUD_PROJECT

sudo pip3 install -r requirements.txt
python3 mars-local-stream.py
