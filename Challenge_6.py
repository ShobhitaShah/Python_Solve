import pandas as pd
import os
import sys
input_files_directory = sys.argv[1]

# creating a list of all the files to be processed and added to dataframe.
list_of_files_to_be_processed = []
for file in os.listdir(input_files_directory):
    path_to_append = input_files_directory + file
    list_of_files_to_be_processed.append(path_to_append)
    
# creating a empty dataframe which will be populated with values from  different files.
df = pd.DataFrame(columns=['sample_name','Name','RPKM'])

for individual_file in list_of_files_to_be_processed:
    df_temp = pd.read_excel(individual_file)
    df_temp = df_temp[['Name', 'RPKM']]
    sample_name = individual_file.split("/")[-1][:-5]
    df_temp['sample_name'] = sample_name
    df_temp = df_temp.sort_values(by=['RPKM'], ascending=False)
    df = df.append(df_temp)
    # if required to sort based on all samples.
    #df = df.sort_values(by=['FDR'], ascending=False)
output_file_name = "final_merged_files.csv"
output_file_path = sys.argv[2] + "/" + output_file_name
df.to_csv(output_file_path, sep=',', index=False, encoding='utf-8')