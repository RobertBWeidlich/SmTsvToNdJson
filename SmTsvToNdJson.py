#!/bin/env python3
import sys
import re


def main(tsv_file):
    # for each event in Sysmon file, some date is in tab-separated line, other
    # data is attribute-value pairs
    with open(tsv_file, 'r') as in_file:
        line_count = 0
        rec_dict_info_attributes = []
        rec_dict = {}
        for line in in_file:
            line = line.strip()
            line_count += 1
            print(len(line.strip()))
            if len(rec_dict_info_attributes) < 1 and len(line.strip()) > 1:
                print(f'1>>>{line}<<<')
                rec_dict_info_attributes = line.split('\t')
                print(rec_dict_info_attributes)
                continue
            elif re.match('^information', line, re.IGNORECASE):
                # todo: handle cases where new record does NOT begin with "Information"
                # look for tab-delimited lines??
                vals = line.split('\t')
                print(f'2>>>{line}<<<')
                print(vals)
                break

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