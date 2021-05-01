#!/usr/bin/env python3
import apache_beam as beam
import os
import datetime


def processline(line):
    yield line


def run():
    projectname = os.getenv('GOOGLE_CLOUD_PROJECT')
    bucketname = os.getenv('GOOGLE_CLOUD_PROJECT') + '-bucket'
    jobname = 'mars-job' + datetime.datetime.now().strftime("%Y%m%d%H%m")
    region = 'us-central1'

    argv = [
      '--runner=DataflowRunner',
      '--project=' + projectname,
      '--job_name=' + jobname,
      '--region=' + region,
      '--staging_location=gs://' + bucketname + '/staging/',
      '--temp_location=gs://' + bucketname + '/temploc/',
      '--save_main_session'
    ]

    p = beam.Pipeline(argv=argv)
    input = 'gs://moonbank-mars-sample/*.csv'
    output = 'gs://' + bucketname + '/output/output'

    (p
     | 'Read Files' >> beam.io.ReadFromText(input)
     | 'Process Lines' >> beam.FlatMap(lambda line: processline(line))
     | 'Write Output' >> beam.io.WriteToText(output)
     )
    p.run()


if __name__ == '__main__':
    run()
