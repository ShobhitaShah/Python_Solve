import pandas as pd
import sys

input_file_path = sys.argv[1]
df = pd.read_csv(input_file_path) # importing the original csv file

df2 = df.drop('gene_biotype' , axis=1) # removing the string column as the numerical calculations don't work on strings.

df2.iloc[:, :-1]=df2.iloc[:, :-1].div(df2['total'], axis=0)*100   # converting in terms of percentage
df2.fillna(0,inplace=True)                                        # replacing the NaN values with 0 because when we divide by 0 we receive Nan.

for cols in df2.columns:
    if cols != 'total':                                                            # adding percentage symbol in front of all values
        df2[cols] = df[cols].apply( lambda x : str(x) + '%')
     
extracted_col = df['gene_biotype']                                # merging back the gene biotype column
df2.insert(0, 'gene_biotype', extracted_col)    

output_file_name = input_file_path.split("/")[-1][:-4] + "_percentage.csv"
output_file_path = sys.argv[2] + "/" + output_file_name
df2.to_csv(output_file_path, sep=',', encoding='utf-8')