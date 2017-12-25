# -*- coddata = f.read()ing: utf-8 -*- 

import MySQLdb
import datetime
import time

k = 5
total = 0
ksum = 0 
match =0

db = MySQLdb.connect(host="163.21.245.147", user="solitude6060", passwd="1234567890", db="project")

cursor = db.cursor()
db.set_character_set('utf8')

curtime = datetime.datetime.strptime(datetime.datetime.now().isoformat(), '%Y-%m-%dT%H:%M:%S.%f').strftime('%Y-%m-%d')
curHMS = datetime.datetime.strptime(datetime.datetime.now().isoformat(), '%Y-%m-%dT%H:%M:%S.%f').strftime('%H:%M:%S')


sql_meeting_today = "SELECT * from Meeting where Meeting_date = '" + str(curtime) + "' AND Meeting_startTime <= '"+str(curHMS)+"' AND Meeting_endTime >= '"+str(curHMS)+"'"
cursor.execute(sql_meeting_today)
db.commit()
meeting_all_today = cursor.fetchall()

for meeting in meeting_all_today:
    
    sql_seating = "SELECT * from Seating where room_id = '" + str(meeting[3])+"'"
    cursor.execute(sql_seating)
    db.commit()
    seat_for_meeting = cursor.fetchall()

    sql_seating_x = "SELECT * from Seating where room_id = '" + str(meeting[3]) + "' ORDER BY Seat_xid DESC LIMIT 1"
    cursor.execute(sql_seating_x)
    db.commit()
    max_x = 0
    max_y = 0
    x_x = cursor.fetchall()
    for xx in x_x:
        if xx is not None:
            max_x = xx[2]
            #print(max_x)

    sql_seating_y = "SELECT * from Seating where room_id = '" + str(meeting[3]) + "' ORDER BY Seat_yid DESC LIMIT 1"
    cursor.execute(sql_seating_y)
    db.commit()
    y_y = cursor.fetchall()
    #print(y_y)
    for yy in y_y:
        if yy is not None:
            max_y = yy[3]
            #print(max_y)

    sql_checkin = "SELECT * from Check_in where Meeting_id = " + str(meeting[1])
    cursor.execute(sql_checkin)
    db.commit()
    checkMem_for_meeting = cursor.fetchall()

    #for seat in seat_for_meeting:

    for mem in  checkMem_for_meeting:
        
        sql_position_t = "SELECT * from Positioning where Member_email = '" + str(mem[2]) + "' AND MeetingRoom_id = '" + str(meeting[3])+ "' ORDER BY wifi_time DESC LIMIT 1"
        cursor.execute(sql_position_t)
        db.commit()
        mem_pos = cursor.fetchall()
        LastTime = datetime.datetime(2017, 11, 14, 9, 50, 54)
        for m in mem_pos:
            LastTime = m[6]
        

        sql_position= "SELECT * from Positioning where Member_email = '" + str(mem[2]) + "' AND MeetingRoom_id = '" + str(meeting[3])+ "' AND wifi_time = '"+str(LastTime)+"'"
        cursor.execute(sql_position)
        db.commit()
        mem_position = cursor.fetchall()


        Matrix = [[0 for y in range(int(max_y)+1)] for x in range(int(max_x)+1)] 

        for x in range(1, max_x+1):
            for y in range(1, max_y+1):
                for pos in mem_position:
                    
                    mac = pos[5]
                    wifi = pos[3]         
                    seat_wifi = [item for item in seat_for_meeting if item[6] == mac and item[2] == x and item[3]==y]
                    if seat_wifi is not None:
                        for i in seat_wifi:
                            s_wifi = i[5]
                            weight = s_wifi*-1*0.0001
                            dis = ((s_wifi - wifi)**2)*weight
                            Matrix[x][y] = dis

        small = 1000000000
        smallX = 0
        smallY = 0
        for x in range(1, max_x+1):
            for y in range(1, max_y+1):
                if Matrix[x][y] <= small:
                    small = Matrix[x][y]
                    smallX = x
                    smallY = y

        sql_update = "UPDATE Check_in SET Seat_xid = %s, Seat_yid = %s WHERE Meeting_id = " + str(meeting[1]) + " AND Member_email = '" + str(mem[2])+"'"
        cursor.execute(sql_update, (smallX, smallY))
        db.commit()


cursor.close()
db.close()

