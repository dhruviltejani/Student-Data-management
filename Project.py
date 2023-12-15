import pandas as pd
import matplotlib.pyplot as graph
from tabulate import tabulate as tbl

#creating tables using list and then using tabulate to make tables
menutable=[['Enter 1 to insert data'],
          ['Enter 2 to search data'],
          ['Enter 3 to delete data'],
          ['Enter 4 to update data'],
          ['Enter 5 to plot a linear graph'],
          ['Enter 6 to plot a bar graph'],
          ['Enter 7 to get percentage histogram'],
          ['Enter 8 for Customer Care'],
          ['Enter 9 to exit']]

searchtable=[["Enter 1 to search on basis of Roll_number"],
            ["Enter 2 to search on basis of Name"],
            ['Enter 3 to search on basis of Subject wise marks'],
            ["Enter 4 to search on the basis of GR_no"],
            ['Enter 5 to search on the basis of Grade']]

subjecttable=[['''SUBJECTS'''],
              ['Maths'],
              ['English'],
              ['Physics'],
              ['Chemistry'],
              ['IP']]

deletetable=[["1)To delete student record with the help of Roll_no"],
            ["2)To delete student record with the help of Name"],
            ["3)To delete student record with the help of English marks"],
            ["4)To delete student record with the help of Math marks"],
            ["5)To delete student record with the help of IP marks"],
            ["6)To delete student record with the help of Physics marks"],
            ["7)To delete student record with the help of Chemistry marks"],
            ["8)To delete student record with the help of GR_no"]]

updatetable=[["Enter 1 to update field with the help of Roll_no"],
            ["Enter 2 to update field with the help of Name"]]

updatetable1=[["Enter 1 to update your Name field"],
             ["Enter 2 to update your English field"],
             ["Enter 3 to update your Maths field"],
             ['Enter 4 to update your IP field'],
             ['Enter 5 to update your Physics field'],
             ['Enter 6 to update your Chemistry field']]

updatetable2=[["Enter 1 to update your Roll_no field"],
            ["Enter 2 to update your English field"],
            ["Enter 3 to update your Maths field"],
            ['Enter 4 to update your IP field'],
            ['Enter 5 to update your Physics field'],
            ['Enter 6 to update your Chemistry field']]

linegraphtable=[["Enter 1 for Name vs English"],
               ["Enter 2 for Name vs Maths"],
               ["Enter 3 for Name vs Informatics Practices"],
               ["Enter 4 for Name vs Physics"],
               ["Enter 5 for Name vs Chemistry"]]

bargraphtable=[["Enter 1 for Name vs English"],
              ["Enter 2 for Name vs Maths"],
              ["Enter 3 for Name vs Informatics Practices"],
              ["Enter 4 for Name vs Physics"],
              ["Enter 5 for Name vs Chemistry"]]

servicetable=[['Customer Services Are open 24 x 7'],
             ['Contact us on our online website "www.studentinfosystem.support.com"'],
             ['Contact us through landline on 0471-2721601'],
             ['Contact us through Mobile_number on =91-9828644202'],
             ['Contact us through Gmail on "stuinfosyscustomercare2023@gmail.com"'],
             ['Give us feedbacks on Gmail account "stuinfosysfeedback2023@gmail.com"'],
             ["Hope that our customer care helped you"]]

#creating list for making dictionary and using dictionary to create dataframe
name=[]
roll=[]
grno=[]
english=[]
maths=[]
ip=[]
physics=[]
chemistry=[]
totalmarks=[]
percentage=[]
grade=[]

#Creating user define functions
def inst():
    print('='*156)
    a=str(input('''----->Enter no of student records you want to insert='''))
    if(a==""):
        print("!!!ERROR!!!")
        print("Enter number of students record you want to insert")
        a=0
    print('='*156)
    for i in range(int(a)):
#Reading CSV file
        dff=pd.read_csv("D:\\Codes\\Pyhton Codes\\Pandas\\School 12th project\\Students data management project\\Students Saved Info.csv")
#Generating Gr_no by its own
        grnew=[]
        for i in dff['Grno']:
            grnew.append(i)
        z=max(grnew)
        grn=z+1

        n1=input("----->Enter name=")
        if(n1==""):
            print("Name field is empty")
            break
        print('='*156)

        rp=[]
        n2=str(input("----->Enter roll_no="))
        print('='*156)
#Creating for loop for checking that roll no is not entered twice
        for i in dff['Roll_no']:
            rp.append(i)
        if(n2==""):
            print("!!!Error!!!")
            print("Roll_no field is empty")
            break
        elif(int(n2) in rp):
            print("This Roll_no exist")
            break

        n3=str(input("----->Enter marks of English="))
        if(n3==""):
            print("!!!ERROR!!!")
            print("English field is empty")
            break
        elif(int(n3)>100):
            print('!!Error!!')
            print('Please enter marks within 100')
            break

        print('='*156)
        n4=str(input("----->Enter marks of Maths="))
        if(n4==""):
            print("!!!ERROR!!!")
            print("Maths field is empty")
            break
        elif(int(n4)>100):
            print('!!Error!!')
            print('Please enter marks within 100')
            break
        print('='*156)

        n5=str(input("----->Enter marks of IP="))
        if(n5==""):
            print("!!!ERROR!!!")
            print("IP field is empty")
            break
        elif(int(n5)>100):
            print('!!Error!!')
            print('Please enter marks within 100')
            break
        print('='*156)

        n6=str(input("----->Enter marks of Physics="))
        if(n6==""):
            print("!!!ERROR!!!")
            print("Physics field is empty")
            break
        elif(int(n6)>100):
            print('!!Error!!')
            print('Please enter marks within 100')
            break
        print('='*156)

        n7=str(input("----->Enter marks of chemistry="))
        if(n7==""):
            print("!!!ERROR!!!")
            print("Chemistry field is empty")
            break
        if(int(n7)>100):
            print('!!Error!!')
            print('Please enter marks within 100')
            break
        print('='*156)

#Appending/adding values to created list 
        physics.append(int(n6))
        chemistry.append(int(n7))
        ip.append(int(n5))
        maths.append(int(n4))
        english.append(int(n3))
        roll.append(int(n2))
        grno.append(grn)
#Making name into uppercase to search, delete, update, etc.To fetch data eaisly
        name.append(n1.upper())
        total=int(n3)+int(n4)+int(n5)+int(n6)+int(n7)
        totalmarks.append(total)
        pr=total*100/500
        percentage.append(pr)

#By using if elif statements assigning grade to the records
        if(pr>=95):
            grade.append('A+')
        if(pr>=90 and pr<=94):
            grade.append('A')
        if(pr<=89 and pr>=80):
            grade.append('B+')
        if(pr>=75 and pr<=79):
            grade.append('B')
        if(pr>=70 and pr<=74):
            grade.append('C+')
        if(pr>=60 and pr<=69):
            grade.append('C')
        if(pr>=50 and pr<=59):
            grade.append('D+')
        if(pr>=40 and pr<=49):
            grade.append('D')
        if(pr>=33 and pr<=39):
            grade.append('E+')
        if(pr>=20 and pr<=32):
            grade.append('E')
        if(pr>=10 and pr<=19):
            grade.append('F+')
        if(pr>=0 and pr<=9):
            grade.append('F')

#Creating dictionary using list 
        dic={"GR_no":grno,
        "Name":name,
        "English":english,
        "Maths":maths,
        "IP":ip,
        "Physics":physics,
        "Chemistry":chemistry,
        "Total Marks":totalmarks,
        "Percentage":percentage,
        'Grade':grade}

#Creating dataframe using dictionary
        df=pd.DataFrame(dic,index=roll)
#Sending to CSV 
        df.to_csv("D:\\Codes\\Pyhton Codes\\Pandas\\School 12th project\\Students data management project\\Students Saved Info.csv",mode='a',header=False)
#Clear statement used to clear the list because if user wishes 
#to insert more data then the stored data into the list will not go second time in dictionary

        roll.clear()
        grno.clear()
        name.clear()
        english.clear()
        maths.clear()
        ip.clear()
        physics.clear()
        chemistry.clear()
        totalmarks.clear()
        percentage.clear()
        grade.clear()
#____________________________________________________________________________________________________________________________________________________________________________
#____________________________________________________________________________________________________________________________________________________________________________
def search():
    while True:
#Using tabulate module to create table from above created list
        print(tbl(searchtable,tablefmt='rounded_grid'))
        srch=str(input("Enter your searching choice="))
        df=pd.read_csv("D:\\Codes\\Pyhton Codes\\Pandas\\School 12th project\\Students data management project\\Students Saved Info.csv")
        if(srch==""):
            print("!!!ERROR!!!")
            print('please enter your searching choice')
            break
        if(int(srch)<=0 or int(srch)>=6):
            print("Enter with-in 1 to 5")
            break
        elif(int(srch)==1):
            print('='*156)
            sroll=str(input("Enter Roll_number you want to search="))
            print('='*156)
            chk=[]
            if(sroll==""):
                print('!!!ERROR!!!')
                print("please enter Roll_no to search")
                break
#Creating for loop for checking that the roll_no that user enter is in the dataframe(called from csv) or not
#created for loops for all the fields too
            for i in df['Roll_no']:
                chk.append(i)
#Saying user that there is no such roll no in dataframe(Called from csv) using not in aggeregate
            if(int(sroll) not in chk):
                print('No such Roll_no exist')
                break
            sr=df[df['Roll_no']==int(sroll)]  

        elif(int(srch)==2):
            print('='*156)
            nm=str(input("Enter name you want to search="))
            na=[] 
            print('='*156)
            for i in df['Name']:
                na.append(i)
            if(nm==""):
                print('Please enter Name to search')
                break
            elif(nm.upper() not in na):
                print("No such name exists")
                break
            sr=df[df['Name']==nm.upper()]
        elif(int(srch)==3):
            print(tbl(subjecttable,tablefmt='rounded_grid'))
            h=str(input('Enter your subject name='))

#Created because to check if user enters the correct subject
            sbj=['MATHS','MATH','PHYSICS','ENGLISH','IP','CHEMISTRY']
            if(h==""):
                print("!!!ERROR!!!")
                print("Please enter subject name")
                break

#Giving error if user enters mysterious subject using 'not in' function
            elif(h.upper() not in sbj):
                print("No such subject")
                break
#Converting subject name into uppercase beacuse user can enter in any ways
            elif(h.upper()=="ENGLISH"):
                print('='*156)
                print("Enter 1 to get students record greater then entered marks")
                print('='*156)
                print("Enter 2 to get students record less then entered marks")
                print('='*156)
                print("Enter 3 to get students record to equal to entered marks")
                print('='*156)
                z=str(input('Enter your choice='))
                if(z==""):
                    print('Please enter your choice')
                    break

                elif(int(z)<=0 or int(z)>=4):
                    print(f"There is no such choice like {z}")
                    print("Enter valid choice from 1 to 3!!!")
                    break

                elif(int(z)==1):
                    print('='*156)
                    eg=str(input("Enter marks of English to get students record="))
                    if(eg==""):
                        print("!!!ERROR!!!")
                        print('Please enter english marks to get record')
                        break

                    elif(int(eg)<0 or int(eg)>100):
                        print("!!!ERROR!!!")
                        print("To get data Enter marks with-in 0 to 100")
                        break
                    print('='*156)
                    sr=df[df['English']>int(eg)]

                elif(int(z)==2):
                    print('='*156)
                    eg=str(input("Enter marks of English to get students record="))
                    if(eg==""):
                        print("!!!ERROR!!!")
                        print('Please enter english marks to get record')
                        break

                    elif(int(eg)<0 or int(eg)>100):
                        print("!!!ERROR!!!")
                        print("To get data Enter marks with-in 0 to 100")
                        break
                    print('='*156)

                    sr=df[df['English']<int(eg)]
                elif(int(z)==3):
#Same as checking for roll_no
                    engm=[]
                    for i in df['English']:
                        engm.append(i)
                    print('='*156)

                    eg=str(input("Enter marks of English to get students record="))

                    if(eg==""):
                        print("!!!ERROR!!!")
                        print('Please enter english marks to get record')
                        break

                    elif(int(eg)<0 or int(eg)>100):
                        print("!!!ERROR!!!")
                        print("To get data Enter marks with-in 0 to 100")
                        break
#Giving error same as roll_no
                    elif(int(eg) not in engm):
                        print(f"No on gained {eg} marks")
                        break
                    print('='*156)
                    sr=df[df['English']==int(eg)]

            elif(h.upper()=="MATHS" or h.upper()=="MATH"):
                print('='*156)
                print("Enter 1 to get students record greater then entered marks")
                print('='*156)
                print("Enter 2 to get students record less then entered marks")
                print('='*156)
                print("Enter 3 to get students record to equal to entered marks")
                print('='*156)
                z=str(input('Enter your choice='))

                if(z==""):
                    print('Please enter your choice')
                    break

                elif(int(z)<=0 or int(z)>=4):
                    print(f"There is no such choice like {z}")
                    print("Enter valid choice from 1 to 3!!!")
                    break

                elif(int(z)==1):
                    print('='*156)
                    mt=str(input("Enter marks of Maths to get students record="))
                    
                    if(mt==""):
                        print("!!!ERROR!!!")
                        print('Please enter marks to get record')
                        break

                    elif(int(mt)<0 or int(mt)>100):
                        print("!!!ERROR!!!")
                        print("To get data Enter marks with-in 0 to 100")
                        break
                    print('='*156)
                    sr=df[df['Maths']>int(mt)]

                elif(int(z)==2):
                    print('='*156)
                    mt=str(input("Enter marks of Maths to get students record="))

                    if(mt==""):
                        print("!!!ERROR!!!")
                        print('Please enter marks to get record')
                        break

                    elif(int(mt)<0 or int(mt)>100):
                        print("!!!ERROR!!!")
                        print("To get data Enter marks with-in 0 to 100")
                        break
                    print('='*156)
                    sr=df[df['Maths']<int(mt)]

                elif(int(z)==3):
                    print('='*156)
                    mathm=[]
                    for i in df['Maths']:
                        mathm.append(i)

                    mt=str(input("Enter marks of Maths to get students record="))

                    if(mt==""):
                        print("!!!ERROR!!!")
                        print('Please enter marks to get record')
                        break

                    elif(int(mt)<0 or int(mt)>100):
                        print("!!!ERROR!!!")
                        print("To get data Enter marks with-in 0 to 100")
                        break

                    elif(int(mt) not in mathm):
                        print(f"No on gained {mt} marks")
                        break
                    print('='*156)
                    sr=df[df['Maths']==int(mt)]

            elif(h.upper()=="IP"):
                print('='*156)
                print("Enter 1 to get students record greater then entered marks")
                print('='*156)
                print("Enter 2 to get students record less then entered marks")
                print('='*156)
                print("Enter 3 to get students record to equal to entered marks")
                print('='*156)

                z=str(input('Enter your choice='))

                if(z==""):
                    print('Please enter your choice')
                    break

                elif(int(z)<=0 or int(z)>=4):
                    print(f"There is no such choice like {z}")
                    print("Enter valid choice from 1 to 3!!!")
                    break


                elif(int(z)==1):
                    print('='*156)
                    ipp=str(input("Enter marks of IP to get students record="))

                    if(ipp==""):
                        print("!!!ERROR!!!")
                        print('Please enter marks to get record')
                        break

                    elif(int(ipp)<0 or int(ipp)>100):
                        print("!!!ERROR!!!")
                        print("To get data Enter marks with-in 0 to 100")
                        break
                    print('='*156)
                    sr=df[df['IP']>int(ipp)]

                elif(int(z)==2):
                    print('='*156)
                    ipp=str(input("Enter marks of IP to get students record="))

                    if(ipp==""):
                        print("!!!ERROR!!!")
                        print('Please enter marks to get record')
                        break

                    elif(int(ipp)<0 or int(ipp)>100):
                        print("!!!ERROR!!!")
                        print("To get data Enter marks with-in 0 to 100")
                        break
                    print('='*156)
                    sr=df[df['IP']<int(ipp)]

                elif(int(z)==3):
                    print('='*156)
                    ipp=str(input("Enter marks of IP to get students record="))

                    ipm=[]
                    for i in df['IP']:
                        ipm.append(i)

                    if(ipp==""):
                        print("!!!ERROR!!!")
                        print('Please enter marks to get record')
                        break

                    elif(int(ipp)<0 or int(ipp)>100):
                        print("!!!ERROR!!!")
                        print("To get data Enter marks with-in 0 to 100")
                        break

                    elif(int(ipp) not in ipm):
                        print(f"No on gained {ipp} marks")
                        break

                    print('='*156)
                    sr=df[df['IP']==int(ipp)]

            elif(h.upper()=="CHEMISTRY"):
                print('='*156)
                print("Enter 1 to get students record greater then entered marks")
                print('='*156)
                print("Enter 2 to get students record less then entered marks")
                print('='*156)
                print("Enter 3 to get students record to equal to entered marks")
                print('='*156)
                z=str(input('Enter your choice='))

                if(z==""):
                    print('Please enter your choice')
                    break

                elif(int(z)<=0 or int(z)>=4):
                    print(f"There is no such choice like {z}")
                    print("Enter valid choice from 1 to 3!!!")
                    break

                elif(int(z)==1):
                    print('='*156)
                    chm=str(input("Enter marks of Chemistry to get students record="))

                    if(chm==""):
                        print("!!!ERROR!!!")
                        print('Please enter marks to get record')
                        break

                    elif(int(chm)<0 or int(chm)>100):
                        print("!!!ERROR!!!")
                        print("To get data Enter marks with-in 0 to 100")
                        break
                    print('='*156)
                    sr=df[df['Chemitry']>int(chm)]

                elif(int(z)==2):
                    print('='*156)
                    chm=str(input("Enter marks of Chemistry to get students record="))

                    if(chm==""):
                        print("!!!ERROR!!!")
                        print('Please enter marks to get record')
                        break

                    elif(int(chm)<0 or int(chm)>100):
                        print("!!!ERROR!!!")
                        print("To get data Enter marks with-in 0 to 100")
                        break
                    print('='*156)
                    sr=df[df['Chemistry']<int(chm)]

                elif(int(z)==3):
                    print('='*156)
                    chm=str(input("Enter marks of Chemistry to get students record="))

                    chemm=[]
                    for i in df['Chemistry']:
                        chemm.append(i)
                        
                    if(chm==""):
                        print("!!!ERROR!!!")
                        print('Please enter marks to get record')
                        break

                    elif(int(chm)<0 or int(chm)>100):
                        print("!!!ERROR!!!")
                        print("To get data Enter marks with-in 0 to 100")
                        break

                    elif(int(chm) not in chemm):
                        print(f"No on gained {chm} marks")
                        break
                    print('='*156)
                    sr=df[df['Chemistry']==int(chm)]

            elif(h.upper()=="PHYSICS"):
                print('='*156)
                print("Enter 1 to get students record greater then entered marks")
                print('='*156)
                print("Enter 2 to get students record less then entered marks")
                print('='*156)
                print("Enter 3 to get students record to equal to entered marks")
                print('='*156)
                z=str(input('Enter your choice='))

                if(z==""):
                    print('Please enter your choice')
                    break

                elif(int(z)<=0 or int(z)>=4):
                    print(f"There is no such choice like {z}")
                    print("Enter valid choice from 1 to 3!!!")
                    break

                elif(int(z)==1):
                    print('='*156)
                    phi=str(input("Enter marks of Physics to get students record="))

                    if(phi==""):
                        print("!!!ERROR!!!")
                        print('Please enter marks to get record')
                        break

                    elif(int(phi)<0 or int(phi)>100):
                        print("!!!ERROR!!!")
                        print("To get data Enter marks with-in 0 to 100")
                        break
                    print('='*156)
                    sr=df[df['Physics']>int(phi)]

                elif(int(z)==2):
                    print('='*156)
                    phi=str(input("Enter marks of Physics to get students record="))

                    if(phi==""):
                        print("!!!ERROR!!!")
                        print('Please enter marks to get record')
                        break

                    elif(int(phi)<0 or int(phi)>100):
                        print("!!!ERROR!!!")
                        print("To get data Enter marks with-in 0 to 100")
                        break
                    print('='*156)
                    sr=df[df['Physics']<int(phi)]

                elif(int(z)==3):
                    print('='*156)
                    phi=str(input("Enter marks of Physics to get students record="))

                    phym=[]
                    for i in df['Physics']:
                        phym.append(i)

                    if(phi==""):
                        print("!!!ERROR!!!")
                        print('Please enter marks to get record')
                        break

                    elif(int(phi)<0 or int(phi)>100):
                        print("!!!ERROR!!!")
                        print("To get data Enter marks with-in 0 to 100")
                        break

                    elif(int(phi) not in phym):
                        print(f"No on gained {phi} marks")
                        break
                    print('='*156)
                    sr=df[df['Physics']==int(phi)]


        elif(int(srch)==4):
            print('='*156)
            gn=str(input("Enter GR_no to get students record="))

            gchk=[]
            for i in df["Grno"]:
                gchk.append(i)

            if(gn==''):
                print('Please enter Gr_no')
                break 

            elif(int(gn) not in gchk):
                print('No such Gr_no in the data')
                break
            print('='*156)
            sr=df[df['Grno']==int(gn)]

        elif(int(srch)==5):
            print('='*156)
            gd=str(input("Enter Grade to get students record="))

            grdchk=[]
            for i in df['Grade']:
                grdchk.append(i)

            if(gd==''):
                print('Please enter Grade to get records')
                break

            elif(gd.upper() not in grdchk):
                print(f"No one got grade {gd}")
                break
            print('='*156)
            sr=df[df['Grade']==gd.upper()]
#printing data that user asked for
        print(sr)
        print('='*156)
        break
#____________________________________________________________________________________________________________________________________________________________________________
#____________________________________________________________________________________________________________________________________________________________________________
def dlte():
    while True:
#Creating table using tabulate 
        print(tbl(deletetable,tablefmt='rounded_grid'))
        dlt=input("Enter your choice for deletion process=")
#Reading CSV file 
        pdf=pd.read_csv("D:\\Codes\\Pyhton Codes\\Pandas\\School 12th project\\Students data management project\\Students Saved Info.csv")

        if(dlt==""):
            print("!!!ERROR!!!")
            print("Enter your deletion choice")
            break

        elif(int(dlt)<=0 or int(dlt)>8):
            print('!!!ERROR!!!')
            print('Enter valid choice')
            print(f"There no such choice like {dlt}")
            print('enter from 1 to 8 to delete record')
            break

        elif(int(dlt)==1):
            print('='*156)
            delete=input("Enter Roll_number of student to erase record=")
#Creating for loop for checking that the roll_no that user enter is in the dataframe(called from csv) or not
            rol=[]
            for i in pdf['Roll_no']:
                rol.append(i)

            if(delete==""):
                print("!!!ERROR!!!")
                print("Please enter roll_no to delete the record")
                break
#Giving error if roll_no is not in csv
            elif(int(delete) not in rol):
                print('No such Roll_no exists')
                break
            a=pdf[pdf['Roll_no']==int(delete)]
#Deleting data from csv using drop
            pdf=pdf.drop(a.index)

        elif(int(dlt)==2):
            print('='*156)
            delete=input("Enter Name of student to erase record=")

            nmchk=[]
            for i in pdf['Name']:
                nmchk.append(i)

            if(delete==""):
                print('!!!ERROR!!!')
                print("Please enter name")
                break

            elif(delete.upper() not in nmchk):
                print("No such Name exists")
                print('Therefore ,unable to delete record')
                break
            a=pdf[pdf['Name']==delete.upper()]
            pdf=pdf.drop(a.index)
        elif(int(dlt)==3):
            print('='*156)
            delete=input("Enter English marks of student to erase record=")

            engck=[]
            for i in pdf['English']:
                engck.append(i)

            if(delete==""):
                print("!!!ERROR!!!")
                print('Please enter english marks to delete record')
                break

            elif(int(delete) not in engck):
                print(f'No one gained  {delete}  marks')
                print("Therefore ,unable to delete record")
                break
            
            elif(int(delete)<0 or int(delete)>100):
                print('!!!ERROR!!!')
                print('Please enter marks from 1 to 100 to delete records')
                break
            a=pdf[pdf['English']==int(delete)]
            pdf=pdf.drop(a.index)

        elif(int(dlt)==4):
            print('='*156)
            delete=input("Enter Math marks of student to erase record=")

            mck=[]
            for i in pdf['Maths']:
                mck.append(i)

            if(delete==""):
                print("!!!ERROR!!!")
                print('Please enter Maths marks to delete record')
                break

            elif(int(delete) not in mck):
                print(f'No one gained  {delete}  marks')
                print("Therefore ,unable to delete record")
                break
            
            elif(int(delete)<0 or int(delete)>100):
                print('!!!ERROR!!!')
                print('Please enter marks from 1 to 100 to delete records')
                break
            a=pdf[pdf['Maths']==int(delete)]
            pdf=pdf.drop(a.index)

        elif(int(dlt)==5):
            print('='*156)
            delete=input("Enter IP marks of student to erase record=")

            ick=[]
            for i in pdf['IP']:
                ick.append(i)

            if(delete==""):
                print("!!!ERROR!!!")
                print('Please enter IP marks to delete record')
                break

            elif(int(delete) not in ick):
                print(f'No one gained  {delete}  marks')
                print("Therefore ,unable to delete record")
                break
            
            elif(int(delete)<0 or int(delete)>100):
                print('!!!ERROR!!!')
                print('Please enter marks from 1 to 100 to delete records')
                break
            a=pdf[pdf['IP']==int(delete)]
            pdf=pdf.drop(a.index)

        elif(int(dlt)==6):
            print('='*156)
            delete=input("Enter Physics marks of student to erase record=")

            pck=[]
            for i in pdf['Physics']:
                pck.append(i)

            if(delete==""):
                print("!!!ERROR!!!")
                print('Please enter Physics marks to delete record')
                break

            elif(int(delete) not in pck):
                print(f'No one gained  {delete}  marks')
                print("Therefore ,unable to delete record")
                break
            
            elif(int(delete)<0 or int(delete)>100):
                print('!!!ERROR!!!')
                print('Please enter marks from 1 to 100 to delete records')
                break
            a=pdf[pdf['Physics']==int(delete)]
            pdf=pdf.drop(a.index)

        elif(int(dlt)==7):
            print('='*156)
            delete=input("Enter Chemistry marks of student to erase record=")

            cmk=[]
            for i in pdf['Chemistry']:
                cmk.append(i)

            if(delete==""):
                print("!!!ERROR!!!")
                print('Please enter Chemistry marks to delete record')
                break
            
            elif(int(delete) not in cmk):
                print(f'No one gained  {delete}  marks')
                print("Therefore ,unable to delete record")
                break
            
            elif(int(delete)<0 or int(delete)>100):
                print('!!!ERROR!!!')
                print('Please enter marks from 1 to 100 to delete records')
                break
            a=pdf[pdf['Chemistry']==int(delete)]
            pdf=pdf.drop(a.index)

        elif(int(dlt)==8):
            print('='*156)
            delete=int(input("Enter GR_no of student to erase record="))  

            grk=[]
            for i in pdf['Grno']:
                grk.append(i)

            if(delete==""):
                print("!!!ERROR!!!")
                print('Please enter Gr_no  to delete record')
                break
            
            elif(int(delete) not in grk):
                print('Such Gr_no does not exists')
                print(f'Try to enter Gr_no from {min(pdf["Grno"])} to {max(pdf["Grno"])}')
                print("Therefore ,unable to delete record")
                break
            a=pdf[pdf['Grno']==delete]
            pdf=pdf.drop(a.index)
#Sending the undeleted data to CSV
        pdf.to_csv("D:\\Codes\\Pyhton Codes\\Pandas\\School 12th project\\Students data management project\\Students Saved Info.csv",header=True,index=False)
#Showing user the remaing data
        print(pdf)
        print('='*156)
        break
#____________________________________________________________________________________________________________________________________________________________________________
#____________________________________________________________________________________________________________________________________________________________________________
def upd():
    while True:
        print(tbl(updatetable,tablefmt='rounded_grid'))
        updt=input("Enter your updating choice=")
        pdf=pd.read_csv("D:\\Codes\\Pyhton Codes\\Pandas\\School 12th project\\Students data management project\\Students Saved Info.csv")
        df=pd.DataFrame(pdf)

        if(updt==''):
            print('!!!ERROR!!!')
            print('Please enter your updating choice')
            break

        elif(int(updt)<=0 or int(updt)>2):
            print("!!!ERROR!!!")
            print('Please enter your choice from 1 to 2')
            break

        elif(int(updt)==1):
            print(tbl(updatetable1,tablefmt='grid'))

            print('='*156)
            reply=input("Enter your choice=")
            print('='*156)
            roll1=df['Roll_no']
            df.set_index(roll1,inplace=True)

            if(reply==""):
                print('!!!ERROR!!!')
                print('Please enter your choice')
                break

            elif(int(reply)<=0 or int(reply)>6):
                print("!!!ERROR!!!")
                print("Please enter choice from 1 to 6")
                break

            elif(int(reply)==1):
                print(df)
                print('='*156)
                rl=input("roll=")

                rol=[]
                for i in pdf['Roll_no']:
                    rol.append(i)

                if(rl==''):
                    print("Please enter Roll_no")
                    break

                elif(int(rl) not in rol):
                    print('Roll no does not exists')
                    break

                print('='*156)
                nm=input("Enter new Name=")

                if(nm==""):
                    print('!!!Error!!!')
                    print('Please enter Name')
                    break
                print('='*156)
                df.loc[int(rl),'Name']=nm.upper()

            elif(int(reply)==2):
                print(df)
                print('='*156)
                rl=input("roll=")

                rol=[]
                for i in pdf['Roll_no']:
                    rol.append(i)
                    
                if(rl==''):
                    print("Please enter Roll_no")
                    break

                elif(int(rl) not in rol):
                    print('Roll no does not exists')
                    break

                print('='*156)
                em=input("Enter new English marks=")
                if(em==''):
                    print("!!!ERROR!!!")
                    print('Please enter english marks to update')
                    print('Unable to update record')
                    break
                
                elif(int(em)<0 or int(em)>100):
                    print('!!!ERROR!!!')
                    print('Enter marks from 1 to 100')
                    print('Unable to update record')
                    break
                print('='*156)
                df.loc[int(rl),'English']=int(em)

            elif(int(reply)==3):
                print(df)
                print('='*156)
                rl=input("roll=")

                rol=[]
                for i in pdf['Roll_no']:
                    rol.append(i)

                if(rl==''):
                    print("Please enter Roll_no")
                    break

                elif(int(rl) not in rol):
                    print('Roll no does not exists')
                    break

                print('='*156)
                m=input("Enter new Maths marks=")

                if(m==''):
                    print('!!!ERROR!!!')
                    print('Please enter Maths to update')
                    print('Unable to update record')

                elif(int(m)<0 or int(m)>100):
                    print('!!!ERROR!!!')
                    print('Enter marks from 1 to 100')
                    print('Unable to update record')
                print('='*156)
                df.loc[int(rl),'Maths']=int(m)
                
            elif(int(reply)==4):
                print(df)
                print('='*156)
                rl=input("roll=")

                rol=[]
                for i in pdf['Roll_no']:
                    rol.append(i)

                if(rl==''):
                    print("Please enter Roll_no")
                    break
                
                elif(int(rl) not in rol):
                    print('Roll no does not exists')
                    break

                print('='*156)
                i=input("Enter new IP marks=")

                if(i==''):
                    print('!!!ERROR!!!')
                    print('Please enter IP to update')
                    print('Unable to update record')

                elif(int(i)<0 or int(i)>100):
                    print('!!!ERROR!!!')
                    print('Enter marks from 1 to 100')
                    print('Unable to update record')
                print('='*156)
                df.loc[int(rl),'IP']=int(i)

            elif(int(reply)==5):
                print(df)
                print('='*156)
                rl=input("roll=")

                rol=[]
                for i in pdf['Roll_no']:
                    rol.append(i)

                if(rl==''):
                    print("Please enter Roll_no")
                    break

                elif(int(rl) not in rol):
                    print('Roll no does not exists')
                    break
                
                print('='*156)
                p=input("Enter new Physics marks=")

                if(p==''):
                    print('!!!ERROR!!!')
                    print('Please enter Physics to update')
                    print('Unable to update record')

                elif(int(p)<0 or int(p)>100):
                    print('!!!ERROR!!!')
                    print('Enter marks from 1 to 100')
                    print('Unable to update record')
                print('='*156)
                df.loc[int(rl),'Physics']=int(p)

            elif(int(reply)==6):
                print(df)
                print('='*156)
                rl=input("roll=")

                rol=[]
                for i in pdf['Roll_no']:
                    rol.append(i)

                if(rl==''):
                    print("Please enter Roll_no")
                    break

                elif(int(rl) not in rol):
                    print('Roll no does not exists')
                    break

                print('='*156)
                c=input("Enter new Chemistry marks=")

                if(c==''):
                    print('!!!ERROR!!!')
                    print('Please enter CHemistry to update')
                    print('Unable to update record')

                elif(int(c)<0 or int(c)>100):
                    print('!!!ERROR!!!')
                    print('Enter marks from 1 to 100')
                    print('Unable to update record')
                print('='*156)
                df.loc[int(rl),'Chemistry']=int(c)
    
            

#Updating total marks to dataframe
            df['TotalMarks']=df['English']+df['Maths']+df['IP']+df['Physics']+df['Chemistry']
#Updating Percentage to dataframe
            df['Percentage']=df['TotalMarks']*100/500
#Created list for updating the grades in dataframe
            new=[]
            for i in df['Percentage']:
                if(i>=95):
                    new.append('A+')
                elif(i>=90 and i<=94):
                    new.append('A')
                elif(i<=89 and i>=80):
                    new.append('B+')
                elif(i>=75 and i<=79):
                    new.append('B')
                elif(i>=70 and i<=74):
                    new.append('C+')
                elif(i>=60 and i<=69):
                    new.append('C')
                elif(i>=50 and i<=59):
                    new.append('D+')
                elif(i>=40 and i<=49):
                    new.append('D')
                elif(i>=33 and i<=39):
                    new.append('E+')
                elif(i>=20 and i<=32):
                    new.append('E')
                elif(i>=10 and i<=19):
                    new.append('F+')
                elif(i>=0 and i<=9):
                    new.append('F')
            df['Grade']=new
            
#Updated the record to CSV file
            pdf.to_csv("D:\\Codes\\Pyhton Codes\\Pandas\\School 12th project\\Students data management project\\Students Saved Info.csv",index=False)

        elif(int(updt)==2):
#Same as roll_no
            print(tbl(updatetable2,tablefmt='grid'))

            print('='*156)
            reply1=input("Enter your choice=")
            print('='*156)
            nme=df['Name']
            df.set_index(nme,inplace=True)

            nmchk=[]
            for i in df['Name']:
                nmchk.append(i)

            if(reply1==''):
                print("!!!ERROR!!!")
                print('Please enter your choice')
                break

            elif(int(reply1)<=0 or int(reply1)>6):
                print("!!!ERROR!!!")
                print("Please enter choice from 1 to 6")
                break

            elif(int(reply1)==1):
                print(df)
                nm=input("Name=")

                if(nm==''):
                    print('Please enter name')
                    break
                
                if(nm.upper() not in nmchk):
                    print('!!!ERROR!!!')
                    print('No such name exists')
                    break

                print('='*156)
                rl=input("Enter new Roll_no=")

                if(rl==''):
                    print('!!!ERROR!!!')
                    print('Please enter Roll_no to update')
                    print('Unable to update record')
                    break
                print('='*156)
                df.loc[nm.upper(),'Roll_no']=int(rl)
                
            elif(int(reply1)==2):
                print(df)
                nm=input("Name=")

                if(nm==''):
                    print('Please enter name')
                    break
                
                if(nm.upper() not in nmchk):
                    print('!!!ERROR!!!')
                    print('No such name exists')
                    print('Unable to update record')
                    break

                print('='*156)
                en=input("Enter new English marks=")
                
                if(en==''):
                    print('Please enter English marks')
                    break

                elif(int(en)<0 or int(en)>100):
                    print('!!!ERROR!!!')
                    print('Please enter marks from 0 to 100')
                    print('Unable to update record')
                    break
                print('='*156)
                df.loc[nm.upper(),'English']=int(en)

            elif(int(reply1)==3):
                print(df)
                nm=input("Name=")
                
                if(nm==''):
                    print('Please enter name')
                    break
                
                if(nm.upper() not in nmchk):
                    print('!!!ERROR!!!')
                    print('No such name exists')
                    print('Unable to update record')
                    break

                print('='*156)
                m=input("Enter new Maths marks=")

                if(m==''):
                    print('Please enter English marks')
                    break
                
                elif(int(m)<0 or int(m)>100):
                    print('!!!ERROR!!!')
                    print('Please enter marks from 0 to 100')
                    print('Unable to update record')
                    break
                print('='*156)
                df.loc[nm.upper(),'Maths']=int(m)
                
            elif(int(reply1)==4):
                print(df)
                nm=input("Name=")

                if(nm==''):
                    print('Please enter name')
                    break

                if(nm.upper() not in nmchk):
                    print('!!!ERROR!!!')
                    print('No such name exists')
                    print('Unable to update record')
                    break

                print('='*156)
                i=input("Enter new IP marks=")

                if(i==''):
                    print('Please enter English marks')
                    break

                elif(int(i)<0 or int(i)>100):
                    print('!!!ERROR!!!')
                    print('Please enter marks from 0 to 100')
                    print('Unable to update record')
                    break
                print('='*156)
                df.loc[nm.upper(),'IP']=int(i)

            elif(int(reply1)==5):
                print(df)
                nm=input("Name=")

                if(nm==''):
                    print('Please enter name')
                    break

                if(nm.upper() not in nmchk):
                    print('!!!ERROR!!!')
                    print('No such name exists')
                    print('Unable to update record')
                    break

                print('='*156)
                p=input("Enter new Physics marks=")

                if(p==''):
                    print('Please enter English marks')
                    break
                
                elif(int(p)<0 or int(p)>100):
                    print('!!!ERROR!!!')
                    print('Please enter marks from 0 to 100')
                    print('Unable to update record')
                    break
                print('='*156)
                df.loc[nm.upper(),'Physics']=int(p)

            elif(int(reply1)==6):
                print(df)
                nm=input("Name=")

                if(nm==''):
                    print('Please enter name')
                    break

                if(nm.upper() not in nmchk):
                    print('!!!ERROR!!!')
                    print('No such name exists')
                    print('Unable to update record')
                    break

                print('='*156)
                c=input("Enter new Chemistry marks=")
                
                if(c==''):
                    print('Please enter English marks')
                    break
                elif(int(c)<0 or int(c)>100):
                    print('!!!ERROR!!!')
                    print('Please enter marks from 0 to 100')
                    print('Unable to update record')
                    break
                print('='*156)
                df.loc[nm.upper(),'Chemistry']=int(c)

#Same uptading as done in roll_no option
            new1=[]
            df['TotalMarks']=df['English']+df['Maths']+df['IP']+df['Physics']+df['Chemistry']
            df['Percentage']=df['TotalMarks']*100/500

            for g in df['Percentage']:
                if(g>=95):
                    new1.append('A+')
                elif(g>=90 and g<=94):
                    new1.append('A')
                elif(g<=89 and g>=80):
                    new1.append('B+')
                elif(g>=75 and g<=79):
                    new1.append('B')
                elif(g>=70 and g<=74):
                    new1.append('C+')
                elif(g>=60 and g<=69):
                    new1.append('C')
                elif(g>=50 and g<=59):
                    new1.append('D+')
                elif(g>=40 and g<=49):
                    new1.append('D')
                elif(g>=33 and g<=39):
                    new1.append('E+')
                elif(g>=20 and g<=32):
                    new1.append('E')
                elif(g>=10 and g<=19):
                    new1.append('F+')
                elif(g>=0 and g<=9):
                    new1.append('F')

            df['Grade']=new1

#Updating to CSV
        pdf.to_csv("D:\\Codes\\Pyhton Codes\\Pandas\\School 12th project\\Students data management project\\Students Saved Info.csv",index=False)
        break
#____________________________________________________________________________________________________________________________________________________________________________
#____________________________________________________________________________________________________________________________________________________________________________
def linegraph():
    while True:
        print(tbl(linegraphtable,tablefmt='rounded_grid'))
        print('='*156)
        ask=input("Enter choice number for graph=")
        print('='*156)
#Reading CSV file
        pdf=pd.read_csv("D:\\Codes\\Pyhton Codes\\Pandas\\School 12th project\\Students data management project\\Students Saved Info.csv")
#Using CSV file to create linegraph by using matplotlib module
        if(ask==''):
            print('Please enter your choice')
            break

        elif(int(ask)<=0 or int(ask)>5):
            print('!!!ERROR!!!')
            print('Please enter choice from 1 to 5')
            break 

        elif(int(ask)==1):
            graph.plot(pdf["Name"],pdf["English"],'g')
            graph.xlabel("name")
            graph.ylabel("english")
            graph.title("marks of student")
            graph.show()

        elif(int(ask)==2):
            graph.plot(pdf["Name"],pdf["Maths"],'k')
            graph.xlabel("name")
            graph.ylabel("maths")
            graph.title("marks of student")
            graph.show()

        elif(int(ask)==3):
            graph.plot(pdf["Name"],pdf["IP"],'c.-')
            graph.xlabel("name")
            graph.ylabel("Informatics Practices")
            graph.title("marks of student")
            graph.show()

        elif(int(ask)==4):
            graph.plot(pdf["Name"],pdf["Physics"],'y')
            graph.xlabel("name")
            graph.ylabel("Physics")
            graph.title("marks of student")
            graph.show()

        elif(int(ask)==5):
            graph.plot(pdf["Name"],pdf["Chemistry"],'m')
            graph.xlabel("name")
            graph.ylabel("Chemistry")
            graph.title("marks of student")
            graph.show()

        break
#____________________________________________________________________________________________________________________________________________________________________________
#____________________________________________________________________________________________________________________________________________________________________________
def bargraph():
    while True:
        print(tbl(bargraphtable,tablefmt='rounded_grid'))
        print('='*156)
        ask1=input("Enter your choice=")
        print('='*156)
#Reading CSV file
        pdf=pd.read_csv("D:\\Codes\\Pyhton Codes\\Pandas\\School 12th project\\Students data management project\\Students Saved Info.csv")
#Using CSV file to create bargraph by using matplotlib module
        if(ask1==''):
            print('Please enter your choice')
            break

        elif(int(ask1)<=0 or int(ask1)>5):
            print('!!!ERROR!!!')
            print('Please enter choice from 1 to 5')
            break 

        elif(int(ask1)==1):
            graph.bar(pdf["Name"],pdf["English"],label="English")
            graph.xlabel("Name")
            graph.ylabel("Marks")
            graph.title("Students English marks")
            graph.show()

        elif(int(ask1)==2):
            graph.bar(pdf["Name"],pdf["Maths"],label="Maths")
            graph.xlabel("Name")
            graph.ylabel("Marks")
            graph.title("Students Maths marks")
            graph.show()

        elif(int(ask1)==3):
            graph.bar(pdf["Name"],pdf["IP"],label="Informatics practices")
            graph.xlabel("Name")
            graph.ylabel("Marks")
            graph.title("Students Informatics practices marks")
            graph.show()

        elif(int(ask1)==4):
            graph.bar(pdf["Name"],pdf["Physics"],label="Physics")
            graph.xlabel("Name")
            graph.ylabel("Marks")
            graph.title("Students Physics marks")
            graph.show()

        elif(int(ask1)==5):
            graph.bar(pdf["Name"],pdf["Chemistry"],label="Chemistry")
            graph.xlabel("Name")
            graph.ylabel("Marks")
            graph.title("Students Chemistry marks")
            graph.show()

        break
#____________________________________________________________________________________________________________________________________________________________________________
#____________________________________________________________________________________________________________________________________________________________________________
def histograph():
#Reading CSV files
        df=pd.read_csv("D:\\Codes\\Pyhton Codes\\Pandas\\School 12th project\\Students data management project\\Students Saved Info.csv")
#Using CSV file to create linegraph by using matplotlib module

        graph.hist(df["Percentage"],bins=5)
        graph.xlabel("percentage")
        graph.ylabel("No of student")
        graph.title("Percentage Histogram")
        graph.show()
#_______________________________________________________________________________________________________________________________________________________________________
#____________________________________________________________________________________________________________________________________________________________________________
print('''

                                                                12th Science Student Result System
                                                                            created by~
                                                                            Dhruvil Tejani
                                                                            Shofin Garasiya
                                                                            Rahul Khatri


                                                        ''')
while True:                                         
    print(tbl(menutable,tablefmt='double_grid'))
    k=str(input("=====>Enter your choice="))

    if(k==""):
        print("!!!ERROR!!!")
        print("Please enter choice")

    elif(int(k)>=10):
        print("!!ERROR!!")
        print("Enter choice with-in 1 to 9") 

    elif(int(k)<=0):
        print("!!ERROR!!")
        print("Enter choice with-in 1 to 9")    
#____________________________________________________________________________________________________________________________________________________________________________
    elif (int(k)==1):
#Calling user defined function which are created above
        inst()
#Created while loop because to ask user for going on or returning to main menu
        while True:
            left=str(input('Do you want to insert records (y/n)='))
            if(left=='y' or left=='Y'):
                inst() 
            if(left =='n' or left=='N'):
                break 
#_____________________________________________________________________________________________________________________________________________________________________________
    elif(int(k)==2):
#Calling user defined function which are created above
        search()
#Created while loop because to ask user for going on or returning to main menu
        while True:
            leave=str(input('Do you want to keep Searching (y/n)='))
            if(leave.upper()=='Y'):
                search() 
            elif(leave.upper()=='N'):
                break      
#____________________________________________________________________________________________________________________________________________________________________________
    elif(int(k)==3):
#Calling user defined function which are created above
        dlte()
#Created while loop because to ask user for going on or returning to main menu
        while True:
            erase=str(input('Do you want to delete more records (y/n)='))
            if(erase=='y' or erase=='Y'):
                dlte()    
            if(erase =='n' or erase=='N'):
                break
#_____________________________________________________________________________________________________________________________________________________________________________
    elif(int(k)==4):
#Calling user defined function which are created above
        upd()
#Created while loop because to ask user for going on or returning to main menu
        while True:
            quit=str(input('Do you want to keep updating (y/n)='))
            if(quit=='y' or quit=='Y'):
                upd()    
            if(quit=='n' or quit=='N'):
                break  
#____________________________________________________________________________________________________________________________________________________________________________
    elif(int(k)==5):
#Calling user defined function which are created above
        linegraph()
#Created while loop because to ask user for going on or returning to main menu
        while True:
            gone=str(input('Do you want to visualize linegraph (y/n)='))
            if(gone=='y' or gone=='Y'):
                linegraph()    
            if(gone=='n' or gone=='N'):
                break
#_____________________________________________________________________________________________________________________________________________________________________________
    elif(int(k)==6):
#Calling user defined function which are created above
        bargraph()
#Created while loop because to ask user for going on or returning to main menu
        while True:
            going=str(input('Do you want to visualize more bargraph (y/n)='))
            if(going=='y' or going=='Y'):
                bargraph()    
            if(going=='n' or going=='N'):
                break
#_____________________________________________________________________________________________________________________________________________________________________________
    elif(int(k)==7):
#Calling user defined function which are created above
        histograph()
#Created while loop because to ask user for going on or returning to main menu
        while True:
            bye=str(input('Do you want to visualize histogram again (y/n)='))
            if(bye=='y' or bye=='Y'):
                histograph()    
            if(bye=='n' or bye=='N'):
                break
#_____________________________________________________________________________________________________________________________________________________________________________
    elif(int(k)==8):
        print(tbl(servicetable,tablefmt='rounded_grid'))
#_____________________________________________________________________________________________________________________________________________________________________________
    elif(int(k)==9):
        print("Thanks for using my code")
        break
#_____________________________________________________________________________________________________________________________________________________________________________