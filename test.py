#!/usr/bin/env python

import argparse
import yaml
import json


def csv_to_str(csv_str):
    """Convert csv string to list."""
    return [x.strip() for x in csv_str.split(',')]


def load_json(jtext):
    try:
        return json.loads(jtext)
    except Exception:
        return jtext


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', dest='mapping', type=str,
                        default='secretsMapping', help='mapping type')
    parser.add_argument('-c', dest='cfg_path', type=str, default=None,
                        help='config path')
    parser.add_argument('-n', dest='namespaces', type=str, default=None,
                        help='namespaces')
    parser.add_argument('-s', dest='scope', type=str, default='global',
                        help='config scope')
    parser.add_argument('-k', dest='key', type=str, default=None,
                        help='config key')
    parser.add_argument('-v', dest='value', type=str, default=None,
                        help='config value')
    parser.add_argument('-t', dest='datatype', type=str, default='str',
                        help='config data type')
    parser.add_argument('-d', dest='delete', action='store_true',
                        default=False,
                        help='config delete')
    parser.add_argument('-o', dest='outfile', type=str, default='patch.yaml',
                        help='output file path')
    args = parser.parse_args()

    # Generate patch dict
    patch_dict = {
        args.mapping: {
            args.cfg_path: {
                'namespaces': csv_to_str(args.namespaces),
                'scope': {
                    args.scope: {
                        args.key: {
                            'dtype': args.datatype,
                            'key': args.key,
                            'value': load_json(args.value)
                        }
                    }
                }
            }
        }
    }

    # Generate Yaml file
    with open(args.outfile, 'w') as fh:
        yaml.dump(patch_dict, fh)

