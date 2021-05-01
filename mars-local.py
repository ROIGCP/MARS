#!/usr/bin/env python3
import apache_beam as beam


def processline(line):
    yield line


def run():
    argv = [
    ]

    p = beam.Pipeline(argv=argv)
    input = 'sample/*.csv'
    output = 'output/output'
    
    (p
     | 'Read Files' >> beam.io.ReadFromText(input)
     | 'Process Lines' >> beam.FlatMap(lambda line: processline(line))
     | 'Write Output' >> beam.io.WriteToText(output)
     )
    p.run()


if __name__ == '__main__':
    run()
