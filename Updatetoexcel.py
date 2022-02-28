import pandas as pd

class Updatetoexcel:
    def __init__(self,data1):
        self.df = pd.DataFrame(data=data1)
       
    def GetToExcelData(self):
        readDf = pd.read_excel(r"Dabt.xlsx") 
        frame = [readDf,self.df]
        result = pd.concat(frame)
        writer = pd.ExcelWriter("Dabt.xlsx",engine="xlsxwriter")
        result.to_excel(writer,sheet_name="sheet 1",index=False)
        writer.save()
    