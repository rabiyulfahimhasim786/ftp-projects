#import pandas as pd
#df= pd.read_csv('./OH_IMPORT_Annex_MRO_As_Needed_Sheet1_2022-08-12 08 31 27.csv')
#with open('outputf.xml', 'w') as myfile: 
#    myfile.write(df.to_xml())
#pip install lxml

import pandas as pd
df= pd.read_csv('./test.csv')
with open('outputf.xml', 'w') as myfile: 
    myfile.write(df.to_xml())