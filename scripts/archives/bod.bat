start "C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE" C:\\NSE\inputs\\NSEOptions.xlsm
start "C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE" C:\\NSE\inputs\\NSEIndices.xlsm

cd C:\NSE\scripts
python create_oi_log.py

pause
