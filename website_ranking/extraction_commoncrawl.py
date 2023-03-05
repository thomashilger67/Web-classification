import gzip
import json
import pandas as pd

##text=List of strings to be written to file
with open('data/rank.csv','w') as csv_file:
    #Open the data
    with gzip.open("raw_data/cc-main-2022-may-jun-aug-domain-ranks.txt.gz", 'rt', encoding='UTF-8') as fin:
        for i, l in enumerate(fin):
            json_line_str = l
            data_list = json_line_str.split()
            # Reverse the domain name
            data_list[4] = '.'.join(data_list[4].split(".")[::-1])
            print(data_list[0])
            data_str = '\t'.join(data_list)
            csv_file.write(data_str)
            csv_file.write('\n')
csv_file.close()
