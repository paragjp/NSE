import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 2000)
pd.set_option('display.float_format', '{:20,.2f}'.format)
pd.set_option('display.max_colwidth', -1)


def write_to_html_file(df, title='', filename='out.html'):
    '''
    Write an entire dataframe to an HTML file with nice formatting.
    '''

    result = '''
<html>
<head>
<style>
    h2 {
        color: #cc00ff;
        text-align: center;
        font-family: Helvetica, Arial, sans-serif;
    }
    table { 
        margin-left: auto;
        margin-right: auto;
    }
    table, th, td {
        border: 1px solid black;
        border-collapse: collapse;
    }
    th {
       background-color:#0066ff;
       color:white;
    }
    th, td {
        padding: 5px;
        text-align: center;
        font-family: Helvetica, Arial, sans-serif;
        font-size: 90%;
        white-space: nowrap
    }
    table tbody tr:hover {
        background-color: #dddddd;
    }
    .wide {
        width: 100%; 

    }

</style>
</head>
<body>
    '''
    result += '<h2> %s </h2>\n' % title
    result += df.to_html(classes='wide', escape=False, index=False)
    result += '''
</body>
</html>
'''
    with open(filename, 'w') as f:
        f.write(result)


df = []
df = pd.read_excel('C:\\NSE\\outputs\Masters.xlsx', index_col=None)
df.columns = \
    df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
write_to_html_file(df, 'Master Log File', 'c:\\NSE\\outputs\\Masters.html')