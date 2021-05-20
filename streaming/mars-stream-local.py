#!/usr/bin/env python3
# SAMPLE
import apache_beam as beam
import os

def processline(line):
    outputrow = {'message' : line}
    yield outputrow


def run():
    projectname = os.getenv('GOOGLE_CLOUD_PROJECT')
    
    argv = [
        '--streaming'
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
    p.run().wait_until_finish()


if __name__ == '__main__':
    run()