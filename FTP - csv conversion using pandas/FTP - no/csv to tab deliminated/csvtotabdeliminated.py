#!/usr/bin/env python
import csv
import os

dir_path='C:/Users/Administrator/Downloads/FTP requirement (1)/FTP requirement/FTP -No/'


for file in os.listdir(dir_path): 

    file_name, file_ext = os.path.splitext(file)

    if file_ext == '.csv':
        with open(file,'r') as csv_file:
            csv_reader = csv.reader(csv_file)

            #csv_reader.next()  ## skip one line (the first one)

            newfile = file + '.txt'

            for line in csv_reader:
                with open(newfile, 'a') as new_txt:    #new file has .txt extn
                    txt_writer = csv.writer(new_txt, delimiter = '\t') #writefile
                    txt_writer.writerow(line)   #write the lines to file`