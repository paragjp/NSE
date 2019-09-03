import win32com.client as win32

def refresh_excel():

    Xlsx = win32.DispatchEx('Excel.Application')
    Xlsx.DisplayAlerts = False
    Xlsx.Visible = True
    book = Xlsx.Workbooks.Open('C:\\NSE\\inputs\\watchlist.xlsx')
    # Refresh my two sheets
    book.RefreshAll()
    Xlsx.CalculateUntilAsyncQueriesDone()  # this will actually wait for the excel workbook to finish updating
    book.Save()
    book.Close()
    Xlsx.Quit()
    del book
    del Xlsx
