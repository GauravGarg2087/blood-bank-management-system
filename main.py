import mysql.connector
a=mysql.connector.connect(host="localhost",user="root",password="root",port="3306",database="college")
b=a.cursor()
c=int(input("Enter 1 to donate blood ,2 to recieve blood and 3 to search blood availability and 4 to display blood bank: "))
if c==1:
    print ("ENTER DONOR DETAILS")
    name=input("Enter name: ")
    blood=input("Enter blood group: ")
    unit=int(input("Enter number of units donated: "))
    date=input("Enter date in format month_date_year eg: October_15_2025: ")
    age=int(input("Enter age: "))
    confirm=input("Enter 'Y' to save data or 'N' to cancel: ")
    if confirm=="Y":
        if blood=="A+":
            b.execute("select * from blood_data")
            z=b.fetchall()
            prev1=z[0][0]
            prev1=prev1+unit
            rev1=(prev1,)
            b.execute("update blood_data set units_A = %s",rev1)
            a.commit()
        if blood=="B+":
            b.execute("select * from blood_data")
            z=b.fetchall()
            prev2=z[0][1]
            prev2=prev2+unit
            rev2=(prev2,)
            b.execute("update blood_data set units_B = %s",rev2)
            a.commit()
        if blood=="AB+":
            b.execute("select * from blood_data")
            z=b.fetchall()
            prev3=z[0][2]
            prev3=prev3+unit
            rev3=(prev3,)
            b.execute("update blood_data set units_AB = %s",rev3)
            a.commit()
        data=(name,blood,unit,date,age)
        b.execute("INSERT INTO donar_data (name, blood_group, units_donated, date_donated, age) VALUES (%s, %s, %s, %s, %s)", data)
        a.commit()
        print("Data saved successfully")
    else:
        print ("Data not saved as per request")
if c==2:
    print ("ENTER PATIENT DETAILS")
    pname=input("Enter patient's name: ")
    hospital=input("Enter name of hospital in which patient has been admitted: ")
    punit=int(input("Enter no. of units of blood required: "))
    pblood=input("Enter blood group required: ")
    problem=input("Enter the problem eg:accident,surgery etc: ")
    page=int(input("Enter age of the patient"))
    totalcost=50*punit
    print ("Cost of one unit blood is rupees 50,so you are needed to pay rupees",totalcost)
    pconfirm=input("Enter 'Y' to confim order and 'X' to cancel: ")
    if pconfirm=="Y":
        b.execute("select * from blood_data")
        z=b.fetchall()
        A=z[0][0]
        B=z[0][1]
        AB=z[0][2]        
        if pblood=="A+":
            if punit<=A:
                data1=(pname,hospital,punit,problem,pblood,page)
                b.execute("insert into receiver_data (patient_name,hospital_name,units_required,problem,blood_group,age) values (%s,%s,%s,%s,%s,%s) ",data1)
                a.commit()
                b.execute("select * from blood_data")
                z=b.fetchall()
                PREV1=z[0][0]
                PREV1=PREV1-punit
                REV1=(PREV1,)
                b.execute("update blood_data set units_A = %s",REV1)
                a.commit()
                print ("ORDER PLACED SUCCESSFULLY")                
            else:
                print("ORDER FAILED:Enough blood not available")
        if pblood=="B+":
            if punit<=B:
                data1=(pname,hospital,punit,problem,pblood,page)
                b.execute("insert into receiver_data (patient_name,hospital_name,units_required,problem,blood_group,age) values (%s,%s,%s,%s,%s,%s) ",data1)
                a.commit()
                b.execute("select * from blood_data")
                z=b.fetchall()
                PREV2=z[0][1]
                PREV2=PREV2-punit
                REV2=(PREV2,)
                b.execute("update blood_data set units_B = %s",REV2)
                a.commit()
                print("ORDER PLACED SUCCESSFULLY")
            else:
                print("ORDER FAILED:Enough blood not available")
        if pblood=="AB+":
            if punit<=AB:
                data1=(pname,hospital,punit,problem,pblood,page)
                b.execute("insert into receiver_data (patient_name,hospital_name,units_required,problem,blood_group,age) values (%s,%s,%s,%s,%s,%s) ",data1)
                a.commit()
                b.execute("select * from blood_data")
                z=b.fetchall()
                PREV3=z[0][2]
                PREV3=PREV3-punit
                REV3=(PREV3,)
                b.execute("update blood_data set units_AB = %s",REV3)
                a.commit()
                print("ORDER PLACED SUCCESSFULLY")
            else:
                print ("ORDER FAILED:Enough blood not available")
    else:
        print ("ORDER CANCELLED SUCCESSFULLY")
if c==4:
    b.execute("select * from blood_data")
    z=b.fetchall()
    A=z[0][0]
    B=z[0][1]
    AB=z[0][2]
    print ("Number of units available for A+: ",A)
    print ("Number of units available for B+: ",B)
    print ("Number of units available for AB+: ",AB)
if c==3:
    sblood=input("Enter blood group: ")
    sunits=int(input("Enter number of units required: "))
    b.execute("select * from blood_data")
    z=b.fetchall()
    A=z[0][0]
    B=z[0][1]
    AB=z[0][2]
    if sblood=="A+":
        if sunits>A:
            print("SORRY:Enough blood not available")
        else:
            print("CONGRATS:Enough blood is available")
    if sblood=="B+":
        if sunits>B:
            print("SORRY:Enough blood not available")
        else:
            print("CONGRATS:Enough blood is available")
    if sblood=="AB+":
        if sunits>AB:
            print("SORRY:Enough blood not available")
        else:
            print("CONGRATS:Enough blood is available")            
            
    
    
