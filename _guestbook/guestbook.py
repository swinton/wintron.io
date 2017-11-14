#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os


def handler(event, context):
    return "hello world"


if __name__ == "__main__":
    # Read event, context from sys.argv
    args = sys.argv[1:2]

    # Provide None for event, context if not provided
    while len(args) < 2:
        args.append(None)

    # Print the output
    print handler(*args)
