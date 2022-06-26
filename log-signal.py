#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def tail(some_file):
    this_file = open(some_file)
    # Go to the end of the file
    this_file.seek(0, 2)

    while True:
        line = this_file.readline()
        print(line)
        if line:
            yield line
        yield None

def main():

    log_file = "testing.log"
    log_data = tail(log_file)
    
    for i in log_data:
        if i == "test1":
            print(i)
        elif i == "test2":
            print(i)


if __name__ == '__main__':
    main()