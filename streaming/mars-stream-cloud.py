#!/usr/bin/env python3
import apache_beam as beam
import os
import datetime

def processline(line):
    outputrow = {'message' : line}
    yield outputrow


def run():
    projectname = os.getenv('GOOGLE_CLOUD_PROJECT')
    bucketname = os.getenv('GOOGLE_CLOUD_PROJECT') + '-bucket'
    jobname = 'mars-job-' + datetime.datetime.now().strftime("%Y%m%d%H%m")
    region = 'us-central1'

    argv = [
      '--streaming',
      '--runner=DataflowRunner',
      '--project=' + projectname,
      '--job_name=' + jobname,
      '--region=' + region,
      '--staging_location=gs://' + bucketname + '/staging/',
      '--temp_location=gs://' + bucketname + '/temploc/',
      '--save_main_session'
    ]

    p = beam.Pipeline(argv=argv)
    subscription = "projects/" + projectname + "/subscriptions/mars-activities"
    outputtable = projectname + ":mars.raw"
    
    print("Starting Beam Job - next step start the pipeline")
    (p
     | 'Read Messages' >> beam.io.ReadFromPubSub(subscription=subscription)
     | 'Process Lines' >> beam.FlatMap(lambda line: processline(line))
     | 'Write Output' >> beam.io.WriteToBigQuery(outputtable)
     )
    p.run()


if __name__ == '__main__':
    run()