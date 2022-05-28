import mysql.connector

#Fetch binary file from sql DB and save it 
def write_file(data, filename):
    with open(filename, 'wb') as f:
        f.write(data)
def main():
    sampleNum = 0;
    db_config = mysql.connector.connect(user='root', password='', host='localhost',database='test')
    cursor = db_config.cursor()
    try:
        sampleNum=sampleNum+1;
        query = "SELECT doc_pdf FROM pdf_table WHERE id=%s"
        cursor.execute(query,(sampleNum,))
        file = cursor.fetchone()[0]
        write_file(file, 'User'+str(sampleNum)+'.xlsx')
    except AttributeError as e:
        print(e)
    finally:
        cursor.close()

if __name__ == '__main__':
	  main()
