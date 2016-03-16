import datetime
import mysql.connector

cnx = mysql.connector.connect(user='localread')
cursor = cnx.cursor()

query = ("SELECT News_Title, News_Content, DATE_FORMAT(CONVERT_TZ(FROM_UNIXTIME(News_Epoch),'America/Toronto','UTC'), '%H:%i %b %e,%Y') AS News_Epoch, 'Aurani' AS User_Name FROM ocm_generic.site_news WHERE News_Live <= UNIX_TIMESTAMP(NOW()) ORDER BY News_Epoch")

cursor.execute(query)
result = cursor.fetchall()


for (News_Title, News_Content, News_Epoch, User_Name) in enumerate(result,start=1):
	print(str(News_Title) + ":")
	print(str(News_Content))
	print("\t-- " + str(User_Name) + "\t" + str(News_Epoch))
	


cursor.close()
cnx.close()