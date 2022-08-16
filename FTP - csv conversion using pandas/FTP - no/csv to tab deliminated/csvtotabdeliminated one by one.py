#!/usr/bin/env python
import csv
import os
file='C:/Users/Administrator/Downloads/FTP - csv conversion using pandas/OH_IMPORT_Annex_MRO_As_Needed_Sheet1_2022-08-12 08 31 27'
with open(file+'.csv','r') as csv_file:
            csv_reader = csv.reader(csv_file)
            #csv_reader.next()  ## skip one line (the first one)
            newfile = file + '.txt'

            for line in csv_reader:
                with open(newfile, 'a') as new_txt:    #new file has .txt extn
                    txt_writer = csv.writer(new_txt, delimiter = '\t') #writefile
                    txt_writer.writerow(line)   #write the lines to file`