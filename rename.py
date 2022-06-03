from fileinput import filename
import os

folderPath = r'C:\Users\User\Downloads\profolio\img\film\New'
fn = 68

for fn in os.listdir(folderPath):
    os.rename(folderPath + '\\' + filename, folderPath + '\\' + "f" + str(fn))
    fn +=1