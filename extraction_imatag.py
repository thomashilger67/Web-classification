import gzip
import json
import pandas as pd

##text=List of strings to be written to file
with open('data/imatag.csv','w') as csv_file:
    csv_file.write(
        "created\tupdated\tquery.source\tpage.page_url\tpage.image_url\tmedia_count\n"
    )
    csv_file.write('\n')
    #Open the data
    with gzip.open("raw_data/sites-projet ensai.json.gz", 'rt', encoding='UTF-8') as fin:
        #Count the number of lines in the file
        # for i, l in enumerate(fin):
        #     pass
        # i += 1
        # number_of_lines = i
        # print(number_of_lines) # 758486
        for i in range(758486):# hardcode : rajouter un enumerate
            json_line_str = fin.readline()
            json_line_dict = json.loads(json_line_str)
            json_line_id = list(json_line_dict.keys())[0]
            json_line_dict = json_line_dict[json_line_id]
            print(json_line_dict["query"]["source"])
            data_list = [
                            json_line_dict["created"],
                            json_line_dict["updated"],
                            json_line_dict["query"]["source"],
                            json_line_dict["page"]["page_url"],
                            json_line_dict["page"]["image_url"],
                            str(json_line_dict["media_count"])
                        ]
            data_str = '\t'.join(data_list)
            csv_file.write(data_str)
            csv_file.write('\n')

