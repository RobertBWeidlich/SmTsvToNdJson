#!/bin/env python3
# note: if there is a '\ufeff' character, remove it from test file with vi using
# ":set nobomb" command
import sys
import re
import json


def main(tsv_file):
    # for each event in Sysmon file, some date is in tab-separated line, other
    # data is key-value pairs
    with open(tsv_file, 'r') as in_file:
        line_count = 0
        rec_dict_info_keys = []
        rec_dict = {} # hold all event record data
        for line in in_file:
            line = line.strip()
            line_count += 1
            # print(len(line.strip()))
            # the first non-empty line is expected to be a tab-separated
            # list of field names.
            if len(rec_dict_info_keys) < 1 and len(line.strip()) > 1:
                # print(f'1>>>{line}<<<')
                rec_dict_info_keys = line.split('\t')
                # print('rec_dict_info_keys:')
                # print(rec_dict_info_keys)
                continue
            elif re.match('^information', line, re.IGNORECASE):
                # todo: handle cases where new record does NOT begin with "Information"
                # look for tab-delimited lines??
                if len(rec_dict) > 0:
                    # print('rec_dict:')
                    print(json.dumps(rec_dict))
                    # break
                rec_dict_info_vals = line.split('\t')
                # print(f'2>>>{line}<<<')
                # print('rec_dict_info_vals:')
                # print(rec_dict_info_vals)
                rec_dict_info = dict(zip(rec_dict_info_keys, rec_dict_info_vals))
                # print('rec_dict_info:')
                # print(rec_dict_info)
                rec_dict = rec_dict_info.copy()
            else:
                # print(f'3>>>{line}<<<')
                # parse "Attribute: Value"
                colon_ind = line.index(':')
                # print(f'colon_ind: {colon_ind}')
                if colon_ind < 1 or colon_ind > len(line):
                    # todo: check for line = "key:"
                    # or line = "key: "
                    print("error: colon_ind out of bounds")
                else:
                    # todo: check for line = "key:", that is, value is undefined
                    key = line[0:colon_ind]
                    val = line[colon_ind+1:].strip()
                    # print(f'key: "{key}"')
                    # print(f'val: "{val}"')
                    rec_dict[key] = val
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