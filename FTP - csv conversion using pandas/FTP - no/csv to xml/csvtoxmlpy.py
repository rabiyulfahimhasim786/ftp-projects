import csv  
import pandas as pd
            
f = open('./OH_IMPORT_Annex_MRO_As_Needed_Sheet1_2022-08-12 08 31 27.csv')
csv_f = csv.reader(f)   
data = []

for row in csv_f: 
   data.append(row)
f.close()

df = pd.read_csv('./OH_IMPORT_Annex_MRO_As_Needed_Sheet1_2022-08-12 08 31 27.csv')
header= list(df.columns)

def convert_row(row):
     str_row = """<%s>%s</%s> \n"""*(len(header)-1)
     str_row = """<%s>%s""" +"\n"+ str_row + """</%s>"""
     var_values = [list_of_elments[k] for k in range(1,len(header)) for list_of_elments in [header,row,header]]
     var_values = [header[0],row[0]]+var_values+[header[0]]
     var_values =tuple(var_values)
     return str_row % var_values

text ="""<collection shelf="New Arrivals">"""+"\n"+'\n'.join([convert_row(row) for row in data[1:]])+"\n" +"</collection >"
print(text)
with open('output.xml', 'w') as myfile: 
  myfile.write(text)