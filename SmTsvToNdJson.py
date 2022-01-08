#!/bin/env python3
import sys


def main(tsv_file):
    # explain structure of Sysmon file...
    with open(tsv_file, 'r') as in_file:
        line_count = 0
        for line in in_file:
            line = line.strip()
            line_count += 1
            if line_count == 1:
                print(f'>>>{line}<<<')
                tabsep_fields = line.split('\t')
                print(tabsep_fields)
                continue
        pass

    return(None)


if __name__ == '__main__':
    argc = len(sys.argv)
    if (argc < 2):
        print(f'usage: {sys.argv[0]} file')
        sys.exit(1)
    sm_path = sys.argv[1]
    main(sm_path)
    sys.exit(0)