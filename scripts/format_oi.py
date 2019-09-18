import win32com.client as win32
def format_oi():

    Xlsx = win32.DispatchEx('Excel.Application')
    Xlsx.DisplayAlerts = True
    Xlsx.Visible = True
    book = Xlsx.Workbooks.Open('C:\\NSE\\outputs\\OILog.xlsx')
    ws = book.Worksheets("Sheet1")
    ws.Columns.NumberFormat = "0,0"
    ws.Columns.AutoFit()
    ws.Range("A1:Z1").Interior.ColorIndex = 20
    book.Save()
    book.Close()
    Xlsx.Quit()
    del book
    del Xlsx
