import sys
import pandas as pd
import os
import shutil

csv_path = 'C:/Users/Harsh/Desktop/data/FER2013Train/label.csv'
src_path='C:/Users/Harsh/Desktop/Generated/FER2013Train'
dest_path='C:/Users/Harsh/Desktop/Classified/FER2013Train'
for i in range(0,9):
    folder_path = os.path.join(dest_path, str(i))
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

labels=pd.read_csv(csv_path)

lts=[]
for i in labels.index:
    lts=[labels.iat[i,2],labels.iat[i,3],labels.iat[i,4],labels.iat[i,5],labels.iat[i,6],labels.iat[i,7],labels.iat[i,8],labels.iat[i,9],labels.iat[i,10]]
    ind=0
    m = max(lts)
    for j in range(0, 9):
        if lts[j]==m:
            ind=j
    k=labels.at[i,'Image Name']
    if len(k)>0:
        source = folder_path = os.path.join(src_path, k)
        target = os.path.join(dest_path, str(ind))

        try:
            shutil.copy(source, target)
        except IOError as e:
            print("Unable to copy file. %s" % e)
        except:
            print("Unexpected error:", sys.exc_info())

        print("File %s copied!" %k)
    else:
        print("No Image")

print("All Images copied successfully in their respective folder....")



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    
    parser.add_argument("-s", 
                    "--src_folder", 
                    type = str,
                    help = "Path to the folder containing images in png format.",
                    required = True)  
    parser.add_argument("-d", 
                        "--dest_folder", 
                        type = str, 
                        help = "Destination folder. You have to create differnet folder for Training, Tesing and Valiadtion folders first.", 
                        required = True)    
    parser.add_argument("-fer", 
                        "--fer_path", 
                        type = str,
                        help = "Path to the fer+ csv file from microsoft's fer+ repo.",
                        required = True)
                                              

    args = parser.parse_args()
    main(args.src_folder, args.dest_folder, args.fer_path)
