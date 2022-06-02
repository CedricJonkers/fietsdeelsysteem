import pandas as pd

class htmlWriter():
    def __init__(self):
        self
    
    def create_html_table(self, x):
        row_data = ''
        for i in range(x.shape[0]):
            for j in range(x.shape[1]):
                if ((i % 2) != 0) & (j == 0):
                    row_data += '\n<tr style="background-color:#f2f2f2"> \n <td class = "text_column">' + \
                        str(x.iloc[i, j])+'</td>'
                elif j == 0:
                    row_data += '\n<tr> \n <td class = "text_column">' + \
                        str(x.iloc[i, j])+'</td>'
                elif j == 1:
                    row_data += '\n <td class = "number_column">' + \
                        str(x.iloc[i, j])+'</td>'
                elif j == 2:
                    row_data += ' <td class = "number_column">' + \
                        str(x.iloc[i, j])+'</td> \n </tr>'
                else:
                    row_data += '\n <td class = "number_column">' + \
                        str(x.iloc[i, j])+'</td>'
        return row_data
    def create_html_page(self, html_table, df, map, button_link, button_name):
        html_file = '''

<!DOCTYPE html>
<html>
<head>
<style>
table {
  border-collapse: collapse;
  width: 30%;
}

th, td {
  padding: 6px;
  font-family: Helvetica, Arial, Helvetica;
  font-size: 12px;
}


.header {
  color: white;
  background-color: red;
  border-bottom:1pt solid black;
}

.text_column {
  text-align: left;
}
button{
  display: block;
  margin-left: auto;
  margin-right: 0;
}

.number_column {
  text-align: right;
}

.even_row {
  background-color: #f2f2f2;
}

</style>
</head>

<body>
  <h1>Welcome bij A Velo</h1>

<div style="overflow-x:auto;">

<table>
  <thead>
    <tr class = "header">
      <th class = "text_column">'''+df.columns[0]+'''<button type="button" onclick="window.location.href='http://localhost:5500/_site/''' + str(button_link) + '''.html'">'''+str(button_name)+'''</button></th>
    </tr>
  </thead>
  <tbody>
''' + html_table + '''
  </tbody>
  </table>
</div>

</div>
</body>
</html>

'''
        with open(f'_site\{map}.html', 'a') as f:
            f.write(html_file)

# <th class = "number_column">'''+df.columns[1]+'''</th>
