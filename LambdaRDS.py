import pymysql
endpoint = 'ipl-dataset.cmm8chk8y9zp.us-east-1.rds.amazonaws.com'
username = 'admin'
password = 'gravitaschatbot'
database_name = 'GRAVITAS_IPL'
 
#Connection
connection = pymysql.connect(endpoint, user=username,
    passwd=password, db=database_name)
 
def lambda_handler(event,context):
    cursor = connection.cursor()
    cursor.execute('SELECT * from IPL')
 
    rows = cursor.fetchall()
 
    for row in rows:
        print("{0} {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12} {13} {14} {15} {16} {17} ".format(row[0], row[1], row[2],row[3],
         row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17]))
