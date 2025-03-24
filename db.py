import sqlite3
import pandas as pd

conn = sqlite3.connect('test.db', check_same_thread=False)
cursor = conn.cursor()

# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS students(
#         sid TEXT primary key,
#         name text not null,
#         math_score int,
#         science_score int,
#         english_score int,
#         attendence float,
#         cgpa float 
#                )
# ''')

# cursor.execute('''
#     INSERT INTO students (sid, name, math_score, science_score, english_score, attendence, cgpa) 
#     VALUES
# ('S210001', 'Ravi Kumar', 78, 65, 82, 85.5, 8.1),
# ('S210002', 'Sunitha Reddy', 88, 90, 85, 92.4, 9.0),
# ('S210003', 'Vijay Varma', 26, 30, 28, 35.2, 4.0),
# ('S210004', 'Meghana P', 92, 95, 94, 97.1, 9.6),
# ('S210005', 'Rahul Das', 15, 18, 20, 22.0, 2.5),
# ('S210006', 'Anusha N', 84, 80, 86, 88.8, 8.7),
# ('S210007', 'Praveen S', 72, 68, 75, 80.3, 7.8),
# ('S210008', 'Harika M', 90, 92, 91, 95.0, 9.4),
# ('S210009', 'Suresh T', 12, 25, 18, 22.5, 2.0),
# ('S210010', 'Latha K', 77, 79, 82, 85.7, 8.2),
# ('S210011', 'Karthik R', 80, 75, 78, 83.2, 8.0),
# ('S210012', 'Divya M', 88, 85, 90, 91.4, 8.9),
# ('S210013', 'Nikhil V', 22, 20, 19, 25.1, 3.0),
# ('S210014', 'Swathi G', 95, 97, 96, 98.5, 9.8),
# ('S210015', 'Ajay S', 60, 65, 63, 72.0, 6.8),
# ('S210016', 'Pooja R', 85, 88, 87, 90.9, 8.8),
# ('S210017', 'Tarun P', 18, 21, 20, 24.3, 2.3),
# ('S210018', 'Shalini T', 91, 93, 92, 96.2, 9.5),
# ('S210019', 'Manoj B', 58, 55, 57, 69.7, 6.4),
# ('S210020', 'Sneha D', 83, 81, 84, 87.6, 8.4),
# ('S210021', 'Ramesh G', 75, 70, 73, 80.2, 7.7),
# ('S210022', 'Bhavana M', 89, 91, 90, 93.8, 9.1),
# ('S210023', 'Gopi K', 27, 29, 28, 32.0, 4.2),
# ('S210024', 'Anjali N', 96, 94, 97, 99.1, 9.7),
# ('S210025', 'Vamsi V', 59, 62, 61, 71.0, 6.6),
# ('S210026', 'Kavya P', 87, 86, 88, 89.5, 8.6),
# ('S210027', 'Sathish K', 71, 69, 70, 77.2, 7.4),
# ('S210028', 'Pavani R', 93, 92, 94, 96.8, 9.3),
# ('S210029', 'Rohit T', 22, 20, 19, 25.0, 3.0),
# ('S210030', 'Varsha M', 82, 84, 83, 88.0, 8.3),
# ('S210031', 'Chaitanya S', 74, 76, 77, 81.5, 7.9),
# ('S210032', 'Keerthi K', 90, 89, 91, 94.0, 9.0),
# ('S210033', 'Naveen B', 19, 22, 20, 23.7, 2.8),
# ('S210034', 'Sravani P', 94, 96, 95, 97.9, 9.4),
# ('S210035', 'Sandeep R', 62, 60, 61, 72.5, 6.7),
# ('S210036', 'Lavanya G', 86, 87, 85, 90.0, 8.7),
# ('S210037', 'Mahesh K', 73, 71, 74, 79.8, 7.6),
# ('S210038', 'Jyothi N', 97, 95, 96, 98.2, 9.6),
# ('S210039', 'Arjun T', 24, 23, 25, 30.0, 4.0),
# ('S210040', 'Shruthi M', 84, 83, 82, 87.4, 8.5),
# ('S210041', 'Kiran R', 77, 75, 76, 82.0, 7.9),
# ('S210042', 'Deepika S', 91, 93, 92, 95.6, 9.2),
# ('S210043', 'Surya B', 64, 62, 65, 72.9, 6.9),
# ('S210044', 'Sindhu K', 85, 86, 87, 89.3, 8.6),
# ('S210045', 'Venkat P', 16, 19, 18, 20.8, 2.2),
# ('S210046', 'Teja M', 95, 94, 96, 97.4, 9.5),
# ('S210047', 'Bhargavi R', 60, 58, 59, 70.3, 6.5),
# ('S210048', 'Lokesh T', 88, 87, 86, 90.6, 8.8),
# ('S210049', 'Harsha K', 72, 70, 73, 79.5, 7.7),
# ('S210050', 'Nithya S', 92, 93, 91, 95.2, 9.1),
# ('S210051', 'Sameer P', 20, 18, 22, 24.7, 2.9),
# ('S210052', 'Nayana G', 65, 68, 67, 73.2, 7.0),
# ('S210053', 'Vikram S', 58, 60, 59, 69.0, 6.5),
# ('S210054', 'Rekha M', 80, 82, 81, 85.0, 8.1),
# ('S210055', 'Rohini P', 25, 28, 26, 30.5, 4.1),
# ('S210056', 'Gautham K', 74, 76, 75, 80.2, 7.8),
# ('S210057', 'Anil R', 18, 20, 22, 23.8, 2.6),
# ('S210058', 'Bharath V', 87, 88, 85, 90.3, 8.6),
# ('S210059', 'Sangeetha S', 91, 92, 93, 95.9, 9.2),
# ('S210060', 'Raja Babu', 30, 29, 28, 34.2, 4.5),
# ('S210061', 'Vinay G', 61, 63, 62, 71.0, 6.7),
# ('S210062', 'Rajesh K', 75, 78, 77, 82.8, 7.9),
# ('S210063', 'Meena J', 88, 90, 89, 92.7, 9.0),
# ('S210064', 'Prathyusha T', 84, 86, 85, 89.8, 8.8),
# ('S210065', 'Charan V', 22, 24, 23, 26.0, 3.5),
# ('S210066', 'Krishna M', 96, 97, 98, 99.5, 9.7),
# ('S210067', 'Devi K', 60, 62, 61, 71.4, 6.6),
# ('S210068', 'Murali P', 82, 80, 84, 87.0, 8.4),
# ('S210069', 'Anitha N', 92, 95, 94, 97.3, 9.3),
# ('S210070', 'Ragini L', 19, 18, 20, 22.1, 2.7),
# ('S210071', 'Satya V', 58, 56, 57, 66.5, 6.2),
# ('S210072', 'Rohith R', 89, 87, 90, 92.0, 8.9),
# ('S210073', 'Preethi P', 71, 74, 73, 78.5, 7.5),
# ('S210074', 'Kushal B', 63, 65, 66, 72.8, 7.1),
# ('S210075', 'Neha S', 95, 94, 93, 97.0, 9.6),
# ('S210076', 'Sai Kumar', 33, 35, 32, 39.8, 5.0),
# ('S210077', 'Bhanu C', 85, 87, 88, 89.7, 8.7),
# ('S210078', 'Ramya G', 76, 74, 75, 80.1, 7.7),
# ('S210079', 'Madhu N', 90, 88, 89, 93.2, 9.1),
# ('S210080', 'Lakshmi R', 15, 17, 18, 19.5, 2.0),
# ('S210081', 'Pavan V', 68, 70, 67, 75.3, 7.3),
# ('S210082', 'Manisha P', 84, 86, 85, 89.2, 8.7),
# ('S210083', 'Tejaswi K', 90, 92, 91, 95.4, 9.2),
# ('S210084', 'Rakesh N', 57, 55, 56, 65.8, 6.3),
# ('S210085', 'Sharanya S', 77, 80, 79, 83.7, 8.0),
# ('S210086', 'Vijaya P', 60, 62, 61, 71.2, 6.5),
# ('S210087', 'Nikhitha M', 88, 87, 89, 91.8, 8.9),
# ('S210088', 'Yashwanth T', 40, 38, 42, 47.0, 5.5),
# ('S210089', 'Snehalatha D', 95, 96, 94, 97.6, 9.5),
# ('S210090', 'Dinesh S', 20, 22, 21, 24.5, 3.0),
# ('S210091', 'Sailaja K', 72, 74, 75, 79.3, 7.8),
# ('S210092', 'Jaya Surya', 86, 84, 85, 89.1, 8.6),
# ('S210093', 'Mallikarjun T', 19, 20, 18, 22.3, 2.6),
# ('S210094', 'Rajitha G', 98, 96, 97, 99.0, 9.8),
# ('S210095', 'Mahendra P', 55, 58, 57, 66.9, 6.3),
# ('S210096', 'Ashok V', 80, 78, 82, 85.5, 8.1),
# ('S210097', 'Ramya N', 91, 93, 92, 95.7, 9.2),
# ('S210098', 'Nani G', 60, 62, 61, 71.3, 6.6),
# ('S210099', 'Vani M', 85, 88, 87, 90.5, 8.8),
# ('S210100', 'Pandu K', 28, 30, 29, 34.0, 4.2);

# ''')



def get_top(col,top=1):
    col = col+'_score'
    result_df = pd.read_sql_query(f"SELECT * from students ORDER BY {col} DESC LIMIT {top}", conn)
    return result_df

def get_scores(sid, sub=[None, None, None]):
    sid = sid.upper()
    result_df = pd.read_sql_query(f"SELECT sid,math_score,science_score,english_score FROM students WHERE sid='{sid}'", conn)
    # print(result_df)
    return result_df

def get_details(sid):
    sid = sid.upper()
    result_df = pd.read_sql_query(f"SELECT * FROM students WHERE sid='{sid}'", conn)
    # print(result_df)
    return result_df

get_details('S210894')
# print("commiting started bro")
conn.commit()

# print("commiting done bro")
