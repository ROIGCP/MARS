#!/usr/bin/env python3
import apache_beam as beam
import os
import datetime
import csv
from google.cloud import bigquery

table_id = "mars.rawmessages"

def processline(line):
    yield line


def run():
    projectname = os.getenv('GOOGLE_CLOUD_PROJECT')
    bucketname = os.getenv('GOOGLE_CLOUD_PROJECT') + '-bucket'
    subscription = 'projects/' + projectname + '/subscriptions/mars-activities'
    jobname = 'mars-job' + datetime.datetime.now().strftime("%Y%m%d%H%m")
    region = 'us-central1'

    argv = [
      '--runner=DataflowRunner',
      '--project=' + projectname,
      '--job_name=' + jobname,
      '--region=' + region,
      '--streaming',
      '--staging_location=gs://' + bucketname + '/staging/',
      '--temp_location=gs://' + bucketname + '/temploc/',
      '--save_main_session'
    ]

    p = beam.Pipeline(argv=argv)
    topic = 'projects/' + projectname + '/topics/newactivities'
    output = 'gs://' + bucketname + '/output/output'

    (p
     | 'Read Pubsub' >> beam.io.ReadFromPubSub(subscription=subscription).with_output_types(bytes)
     | 'Process Lines' >> beam.FlatMap(lambda line: processline(line))
     | 'Write Row to BigQuery' >> beam.io.WriteToBigQuery(table_id)
     )
    p.run()


if __name__ == '__main__':
    run()
