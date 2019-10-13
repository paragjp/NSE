import win32com.client as win32

def format_excels_cepe():
    Xlsx = win32.DispatchEx('Excel.Application')
    Xlsx.DisplayAlerts = True
    Xlsx.Visible = True
    book = Xlsx.Workbooks.Open('C:\\NSE\\outputs\\CEPElog.xlsx')
    ws = book.Worksheets("Sheet1")
    ws.Range("A2:C99999").NumberFormat = "0"
    ws.Range("D2:T99999").NumberFormat = "0.00"
    # ws.Columns.NumberFormat = "0,0"
    ws.Columns.AutoFit()
    ws.Range("A1:T1").Interior.ColorIndex = 20
    book.Save()
    book.Close()
    Xlsx.Quit()
    del book
    del Xlsx

    Xlsx = win32.DispatchEx('Excel.Application')
    Xlsx.DisplayAlerts = True
    Xlsx.Visible = True
    book = Xlsx.Workbooks.Open('C:\\NSE\\inputs\\cepebasefile.xlsx')
    ws = book.Worksheets("Sheet1")
    ws.Range("A2:C99999").NumberFormat = "0"
    ws.Range("D2:T99999").NumberFormat = "0.00"
    # ws.Columns.NumberFormat = "0,0"
    ws.Columns.AutoFit()
    ws.Range("A1:T1").Interior.ColorIndex = 20
    book.Save()
    book.Close()
    Xlsx.Quit()
    del book
    del Xlsx