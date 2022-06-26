#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def tail(some_file):
    this_file = open(some_file)
    # Go to the end of the file
    this_file.seek(0, 2)

    while True:
        line = this_file.readline()
        if line:
            yield line
        yield None

def main():

    log_file = "testing.log"
    log_data = tail(log_file)
    
    print(log_data)


if __name__ == '__main__':
    main()