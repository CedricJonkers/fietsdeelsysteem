import pandas as pd
price_list = [1,2,3,4]
df = pd.DataFrame({'Stations':['apples','oranges','pears','avocados'],'slots':price_list})

def create_html_table(x):
    
    row_data = ''

    for i in range(x.shape[0]):

        for j in range(x.shape[1]):        
            if ((i % 2) != 0) & (j == 0): #not an even row and the start of a new row
                row_data += '\n<tr style="background-color:#f2f2f2"> \n <td class = "text_column">'+str(x.iloc[i,j])+'</td>'

            elif j == 0: #The first column
                row_data += '\n<tr> \n <td class = "text_column">'+str(x.iloc[i,j])+'</td>'
            
            elif j == 1: #second column
                row_data += '\n <td class = "number_column">'+str(x.iloc[i,j])+'</td>'
            
            elif j == 2: #third column and our last column in my example
                row_data += ' <td class = "number_column">'+str(x.iloc[i,j])+'</td> \n </tr>'

            else:
                row_data += '\n <td class = "number_column">'+str(x.iloc[i,j])+'</td>'
                
    return row_data

html_table = create_html_table(df)

# html_file = '''

# <!DOCTYPE html>
# <html>
# <head>
# <style>
# table {
#   border-collapse: collapse;
#   width: 30%;
# }

# th, td {
#   padding: 6px;
#   font-family: Helvetica, Arial, Helvetica;
#   font-size: 12px;
# }


# .header {
#   color: white;
#   background-color: black;
#   border-bottom:1pt solid black;
# }

# .text_column {
#   text-align: left;
# }

# .number_column {
#   text-align: right;
# }

# .even_row {
#   background-color: #f2f2f2;
# }

# </style>
# </head>

# <body>
#   <h1>HTML Table From a Pandas DataFrame!</h1>

# <div style="overflow-x:auto;">

# <table>
#   <thead>
#     <tr class = "header">
#       <th class = "text_column">'''+df.columns[0]+'''</th>
#       <th class = "number_column">'''+df.columns[1]+'''</th>
#     </tr>
#   </thead>
#   <tbody>
# ''' +html_table+ '''
#   </tbody>
#   </table>

# </div>

# </div>
# </body>
# </html>

# '''
# with open('df_from_loop.html', 'a') as f:
#     f.write(html_file)