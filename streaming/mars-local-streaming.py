#!/usr/bin/env python3
import apache_beam as beam
import os


def processline(line):
    # TODO: Process the line as you need to
    print(line)
    yield line


def run():
    projectname = os.getenv('GOOGLE_CLOUD_PROJECT')
    subscription = 'projects/' + projectname + '/subscriptions/mars-activities'

    argv = [
        "--streaming"
    ]

    p = beam.Pipeline(argv=argv)

    input = 'sample/*.csv'
    output = 'output/output'
    
    (p
     | 'Read PubSub' >> beam.io.ReadFromPubSub(subscription=subscription).with_output_types(bytes)
     | 'View Lines' >> beam.FlatMap(lambda line: processline(line))
    #In order to write the output - you need to window the whole thing - but the View Lines will print each line for you
    #| 'Write Output' >> beam.io.WriteToText(output)
     )
    p.run().wait_until_finish()


if __name__ == '__main__':
    run()
