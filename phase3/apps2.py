
from flask import Flask, render_template, request, make_response
import sqlite3

app = Flask(__name__)

@app.route('/home.html',methods=['GET'])
def home():
    return render_template('home.html')
@app.route('/about.html',methods=['GET'])
def about():
    return render_template('about.html')
@app.route('/search.html',methods=['GET'])
def search():
    return render_template('search.html')
@app.route('/artists.html',methods=['GET'])
def artists():
    return render_template('artists.html')
@app.route('/artiststoplight.html',methods=['GET'])
def artiststoplight():
    return render_template('artiststoplight.html')
@app.route('/Biggie.html',methods=['GET'])
def biggie():
    return render_template('Biggie.html')
@app.route('/Ice_Cube.html',methods=['GET'])
def Ice():
    return render_template('Ice_Cube.html')
@app.route('/Kanye_West.html',methods=['GET'])
def Kanye():
    return render_template('Kanye_West.html')
@app.route('/Slayer.html',methods=['GET'])
def Slayer():
    return render_template('Slayer.html')
@app.route('/Kendrick_Lamar.html',methods=['GET'])
def Lamar():
    return render_template('Kendrick_Lamar.html')
playlist = []
@app.route('/songs-Biggie-Born_Again.html', methods=['POST','GET'])
def submit1():
    dict={"1":"Rap Phenomenon(4:02)","2":"Hope You Niggas Sleep(4:10)","3":"Dead Wrong(4:57)","4":"Come On(4:36)","5":"Can I Get Wit Cha(3:37)"}
    if request.method=='POST':
        button_value=request.form['name']    
        if button_value=='1':    
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message1="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',1)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Biggie-Born_Again.html',message1=message1)
            else:
                message1="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Biggie-Born_Again.html',message1=message1)
        if button_value=='2': 
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message2="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',2)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Biggie-Born_Again.html',message2=message2)
            else:
                message2="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Biggie-Born_Again.html',message2=message2)
        if button_value=='3':  
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message3="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',3)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Biggie-Born_Again.html',message3=message3)
            else:
                message3="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Biggie-Born_Again.html',message3=message3)

        if button_value=='4':    
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message4="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',4)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Biggie-Born_Again.html',message4=message4)
            else:
                message4="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Biggie-Born_Again.html',message4=message4)

        if button_value=='5': 
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message5="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',5)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Biggie-Born_Again.html',message5=message5)
            else:
                message5="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Biggie-Born_Again.html',message5=message5)
    else:
        return render_template('songs-Biggie-Born_Again.html')
@app.route('/songs-Biggie-Duets.html', methods=['POST','GET'])
def submit2():
    dict={"1":"Hold Ya Head(2:46)","2":"Nasty Girl(4:46)","3":"1970 Somethin(3:26)","4":"Wake Up(3:36)","5":"Beef(4:57)"}
    if request.method=='POST':
        button_value=request.form['name']    
        if button_value=='1':    
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message1="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',6)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Biggie-Duets.html',message1=message1)
            else:
                message1="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Biggie-Duets.html',message1=message1)
    
        if button_value=='2': 
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message2="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',7)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Biggie-Duets.html',message2=message2)
            else:
                message2="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Biggie-Duets.html',message2=message2)
        if button_value=='3':  
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message3="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',8)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Biggie-Duets.html',message3=message3)
            else:
                message5="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Biggie-Duets.html',message3=message3)
        if button_value=='4':    
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message4="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',9)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Biggie-Duets.html',message4=message4)
            else:
                message4="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Biggie-Duets.html',message4=message4)
        if button_value=='5': 
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message5="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',10)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Biggie-Duets.html',message5=message5)
            else:
                message5="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Biggie-Duets.html',message5=message5)
    else:
        return render_template('songs-Biggie-Duets.html')

@app.route('/songs-Biggie-Life_After_Death.html', methods=['POST','GET'])
def submit5():
    dict={"1":"Last Day(4:20)","2":"Skys The Limit(5:30)","3":"My Downfall(5:27)","4":"Another(4:15)","5":"Fuck You(5:46)"}
    if request.method=='POST':
        button_value=request.form['name']    
        if button_value=='1':    
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message1="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',11)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Biggie-Life_After_Death.html',message1=message1)
            else:
                message1="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Biggie-Life_After_Death.html',message1=message1)
        if button_value=='2': 
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message2="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',12)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Biggie-Life_After_Death.html',message2=message2)
            else:
                message2="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Biggie-Life_After_Death.html',message2=message2)
        if button_value=='3':  
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message3="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',13)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Biggie-Life_After_Death.html',message3=message3)
            else:
                message3="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Biggie-Life_After_Death.html',message3=message3)
        if button_value=='4':    
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message4="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',14)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Biggie-Life_After_Death.html',message4=message4)
            else:
                message4="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Biggie-Life_After_Death.html',message4=message4)
        if button_value=='5': 
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message5="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',15)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Biggie-Life_After_Death.html',message5=message5)
            else:
                message5="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Biggie-Life_After_Death.html',message5=message5)
    else:
        return render_template('songs-Biggie-Life_After_Death.html')

@app.route('/songs-Biggie-Notorious.html', methods=['POST','GET'])
def submit4():
    dict={"1":"The Notorious Theme(2:07)","2":"Letter to B.I.G.(4:00)","3":"Brooklyn Go Hard(3:59)","4":"Notorious Thugs(3:36)","5":"The World Is Filled(4:55)"}
    if request.method=='POST':
        button_value=request.form['name']    
        if button_value=='1':    
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message1="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',16)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Biggie-Notorious.html',message1=message1)
            else:
                message1="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Biggie-Notorious.html',message1=message1)
        if button_value=='2': 
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message2="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',17)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Biggie-Notorious.html',message2=message2)
            else:
                message2="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Biggie-Notorious.html',message2=message2)
        if button_value=='3':  
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message3="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',18)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Biggie-Notorious.html',message3=message3)
            else:
                message3="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Biggie-Notorious.html',message3=message3)
        if button_value=='4':    
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message4="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',19)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Biggie-Notorious.html',message4=message4)
            else:
                message4="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Biggie-Notorious.html',message4=message4)
        if button_value=='5': 
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message5="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',20)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Biggie-Notorious.html',message5=message5)
            else:
                message5="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Biggie-Notorious.html',message5=message5)
    else:
        return render_template('songs-Biggie-Notorious.html')
@app.route('/songs-Biggie-Ready_to_Die.html', methods=['POST','GET'])
def submit3():
    dict={"1":"The What(3:57)","2":"One More Chance(4:43)","3":"Everyday Struggle(5:19)","4":"Respect(5:21)","5":"Unbelievable(3:44)"}
    if request.method=='POST':
        button_value=request.form['name']    
        if button_value=='1':    
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message1="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',21)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Biggie-Ready_to_Die.html',message1=message1)
            else:
                message1="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Biggie-Ready_to_Die.html',message1=message1)
        if button_value=='2': 
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message2="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',22)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Biggie-Ready_to_Die.html',message2=message2)
            else:
                message2="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Biggie-Ready_to_Die.html',message2=message2)
        if button_value=='3':  
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message3="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',23)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Biggie-Ready_to_Die.html',message3=message3)
            else:
                message3="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Biggie-Ready_to_Die.html',message3=message3)
        if button_value=='4':    
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message4="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',24)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Biggie-Ready_to_Die.html',message4=message4)
            else:
                message4="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Biggie-Ready_to_Die.html',message4=message4)
        if button_value=='5': 
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message5="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',25)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Biggie-Ready_to_Die.html',message5=message5)
            else:
                message5="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Biggie-Ready_to_Die.html',message5=message5)
    else:
        return render_template('songs-Biggie-Ready_to_Die.html')

@app.route('/songs-Ice_Cube-AmeriKKKas_Most_Wanted.html', methods=['POST','GET'])
def submita():
    dict={"1":"Endangered Species(3:22)","2":"Im Only Out for One Thang(2:11)","3":"The Bomb(3:25)","4":"The Drive-By(1:02)","5":"Rollin Wit The Lench Mob(3:44)"}
    if request.method=='POST':
        button_value=request.form['name']    
        if button_value=='1':    
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message1="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',26)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Ice_Cube-AmeriKKKas_Most_Wanted.html',message1=message1)
            else:
                message1="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Ice_Cube-AmeriKKKas_Most_Wanted.html',message1=message1)
        if button_value=='2': 
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message2="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',27)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Ice_Cube-AmeriKKKas_Most_Wanted.html',message2=message2)
            else:
                message2="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Ice_Cube-AmeriKKKas_Most_Wanted.html',message2=message2)
        if button_value=='3':  
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message3="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',28)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Ice_Cube-AmeriKKKas_Most_Wanted.html',message3=message3)
            else:
                message3="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Ice_Cube-AmeriKKKas_Most_Wanted.html',message3=message3)
        if button_value=='4':    
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message4="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',29)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Ice_Cube-AmeriKKKas_Most_Wanted.html',message4=message4)
            else:
                message4="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Ice_Cube-AmeriKKKas_Most_Wanted.html',message4=message4)
        if button_value=='5': 
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message5="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',30)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Ice_Cube-AmeriKKKas_Most_Wanted.html',message5=message5)
            else:
                message5="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Ice_Cube-AmeriKKKas_Most_Wanted.html',message5=message5)
    else:
        return render_template('songs-Ice_Cube-AmeriKKKas_Most_Wanted.html')

@app.route('/songs-Ice_Cube-Death_Certificate.html', methods=['POST','GET'])
def submitb():
    dict={"1":"I Wanna Kill Sam(3:22)","2":"Look Whos Burnin(3:53)'","3":"Death(1:03)","4":"Color Blind(4:29)","5":"Us(3:43)"}
    if request.method=='POST':
        button_value=request.form['name']    
        if button_value=='1':    
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message1="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',31)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Ice_Cube-Death_Certificate.html',message1=message1)
            else:
                message1="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Ice_Cube-Death_Certificate.html',message1=message1)
        if button_value=='2': 
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message2="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',32)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Ice_Cube-Death_Certificate.html',message2=message2)
            else:
                message2="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Ice_Cube-Death_Certificate.html',message2=message2)
        if button_value=='3':  
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message3="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',33)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Ice_Cube-Death_Certificate.html',message3=message3)
            else:
                message3="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Ice_Cube-Death_Certificate.html',message3=message3)
        if button_value=='4':    
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message4="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',34)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Ice_Cube-Death_Certificate.html',message4=message4)
            else:
                message4="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Ice_Cube-Death_Certificate.html',message4=message4)
        if button_value=='5': 
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message5="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',35)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Ice_Cube-Death_Certificate.html',message5=message5)
            else:
                message5="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Ice_Cube-Death_Certificate.html',message5=message5)
    else:
        return render_template('songs-Ice_Cube-Death_Certificate.html')

@app.route('/songs-Ice_Cube-Lethal_Injection.html', methods=['POST','GET'])
def submitc():
    dict={"1":"Ghetto Bird(3:51)","2":"Really Doe(4:28)","3":"Down for Whatever(4:40)","4":"Lil Ass Gee(4:04)","5":"When I Get to Heaven(5:01)"}
    if request.method=='POST':
        button_value=request.form['name']    
        if button_value=='1':    
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message1="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',36)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Ice_Cube-Lethal_Injection.html',message1=message1)
            else:
                message1="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Ice_Cube-Lethal_Injection.html',message1=message1)
        if button_value=='2': 
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message2="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',37)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Ice_Cube-Lethal_Injection.html',message2=message2)
            else:
                message2="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Ice_Cube-Lethal_Injection.html',message2=message2)
        if button_value=='3':  
            print(dict[button_value])   
            if dict[button_value] not in playlist:
                playlist.append(dict[button_value])
                message3="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
                result=crsr.fetchone()
                if result is None:
                    sql_command=f"insert into song values ('{dict[button_value]}',38)"
                    crsr.execute(sql_command)

                    connection.commit()
                    crsr.execute("select * from song")
                    ans=crsr.fetchall()

                    for i in ans:
                        print(i)
                else:
                    crsr.execute("select * from song")
                    ans=crsr.fetchall()

                    for i in ans:
                        print(i)

                for i in ans:
                    print(i)
                return render_template('songs-Ice_Cube-Lethal_Injection.html',message3=message3)
            else:
                message3="Already In Playlist"
                return render_template('songs-Ice_Cube-Lethal_Injection.html',message3=message3)
        if button_value=='4':    
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message4="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',39)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Ice_Cube-Lethal_Injection.html',message4=message4)
            else:
                message4="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Ice_Cube-Lethal_Injection.html',message4=message4)
        if button_value=='5': 
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message5="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',40)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Ice_Cube-Lethal_Injection.html',message5=message5)
            else:
                message5="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Ice_Cube-Lethal_Injection.html',message5=message5)
    else:
        return render_template('songs-Ice_Cube-Lethal_Injection.html')

@app.route('/songs-Ice_Cube-Straight_Outta_Compton.html', methods=['POST','GET'])
def submitd():
    dict={"1":"Fuck Tha Police(5:46)","2":"Express Yourself(4:25)","3":"Dopeman(5:25)","4":"Gangsta Gangsta(5:37)","5":"I Aint tha 1(4:44)"}
    if request.method=='POST':
        button_value=request.form['name']    
        if button_value=='1':    
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message1="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',41)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Ice_Cube-Straight_Outta_Compton.html',message1=message1)
            else:
                message1="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Ice_Cube-Straight_Outta_Compton.html',message1=message1)
        if button_value=='2': 
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message2="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',42)"
                crsr.execute(sql_command)


                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Ice_Cube-Straight_Outta_Compton.html',message2=message2)
            else:
                message2="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Ice_Cube-Straight_Outta_Compton.html',message2=message2)
        if button_value=='3':  
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message3="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',43)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Ice_Cube-Straight_Outta_Compton.html',message3=message3)
            else:
                message3="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Ice_Cube-Straight_Outta_Compton.html',message3=message3)
        if button_value=='4':    
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message4="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',44)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Ice_Cube-Straight_Outta_Compton.html',message4=message4)
            else:
                message4="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Ice_Cube-Straight_Outta_Compton.html',message4=message4)
        if button_value=='5': 
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message5="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',45)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Ice_Cube-Straight_Outta_Compton.html',message5=message5)
            else:
                message5="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Ice_Cube-Straight_Outta_Compton.html',message5=message5)
    else:
        return render_template('songs-Ice_Cube-Straight_Outta_Compton.html')

@app.route('/songs-Ice_Cube-The_Predator.html', methods=['POST','GET'])
def submite():
    dict={"1":"Check Yo Self(3:43)","2":"Wicked(3:56)","3":"Dirty Mack(4:34)","4":"Fuck em(2:02)","5":"Now I Gotta Wet cha(4:03)"}
    if request.method=='POST':
        button_value=request.form['name']    
        if button_value=='1':    
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message1="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',46)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Ice_Cube-The_Predator.html',message1=message1)
            else:
                message1="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Ice_Cube-The_Predator.html',message1=message1)
        if button_value=='2': 
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message2="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',47)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Ice_Cube-The_Predator.html',message2=message2)
            else:
                message2="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Ice_Cube-The_Predator.html',message2=message2)
        if button_value=='3':  
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message3="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',48)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Ice_Cube-The_Predator.html',message3=message3)
            else:
                message3="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Ice_Cube-The_Predator.html',message3=message3)
        if button_value=='4':    
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message4="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',49)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Ice_Cube-The_Predator.html',message4=message4)
            else:
                message4="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Ice_Cube-The_Predator.html',message4=message4)
        if button_value=='5': 
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message5="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',50)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Ice_Cube-The_Predator.html',message5=message5)
            else:
                message5="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Ice_Cube-The_Predator.html',message5=message5)
    else:
        return render_template('songs-Ice_Cube-The_Predator.html')

@app.route('/songs-Kanye-Donda.html', methods=['POST','GET'])
def submit6():
    dict={"1":"Donda(2:09)","2":"Donda Chant(4:30)","3":"Moon(3:41)","4":"Come To Life(2:55)","5":"24(1:30)"}
    if request.method=='POST':
        button_value=request.form['name']    
        if button_value=='1':    
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message1="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',51)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Kanye-Donda.html',message1=message1)
            else:
                message1="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Kanye-Donda.html',message1=message1)
        if button_value=='2': 
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message2="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',52)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Kanye-Donda.html',message2=message2)
            else:
                message2="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Kanye-Donda.html',message2=message2)
        if button_value=='3':  
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message3="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',53)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Kanye-Donda.html',message3=message3)
            else:
                message3="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Kanye-Donda.html',message3=message3)
        if button_value=='4':    
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message4="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',54)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Kanye-Donda.html',message4=message4)
            else:
                message4="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Kanye-Donda.html',message4=message4)
        if button_value=='5': 
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message5="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',55)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Kanye-Donda.html',message5=message5)
            else:
                message5="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Kanye-Donda.html',message5=message5)
    else:
        return render_template('songs-Kanye-Donda.html')

@app.route('/songs-Kanye-Jesus_is_King.html', methods=['POST','GET'])
def submit7():
    dict={"1":"Water(3:43)","2":"Hands On(2:48)","3":"Use This Gospel(3:34)","4":"Every Hour(1:52)","5":"On God(2:16)"}
    if request.method=='POST':
        button_value=request.form['name']    
        if button_value=='1':    
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message1="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',56)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Kanye-Jesus_is_King.html',message1=message1)
            else:
                message1="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Kanye-Jesus_is_King.html',message1=message1)
        if button_value=='2': 
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message2="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',57)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Kanye-Jesus_is_King.html',message2=message2)
            else:
                message2="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Kanye-Jesus_is_King.html',message2=message2)
        if button_value=='3':  
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message3="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',58)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Kanye-Jesus_is_King.html',message3=message3)
            else:
                message3="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Kanye-Jesus_is_King.html',message3=message3)
        if button_value=='4':    
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message4="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',59)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Kanye-Jesus_is_King.html',message4=message4)
            else:
                message4="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Kanye-Jesus_is_King.html',message4=message4)
        if button_value=='5': 
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message5="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',60)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Kanye-Jesus_is_King.html',message5=message5)
            else:
                message5="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Kanye-Jesus_is_King.html',message5=message5)
    else:
        return render_template('songs-Kanye-Jesus_is_King.html')

@app.route('/songs-Kanye-Watch_the_Throne.html', methods=['POST','GET'])
def submit8():
    dict={"1":"Otis(2:58)","2":"Lift Off(4:26)","3":"Niggas in Paris(3:59)","4":"Why I Love You(3:21)","5":"Made in America(4:52)"}
    if request.method=='POST':
        button_value=request.form['name']    
        if button_value=='1':    
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message1="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',61)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Kanye-Watch_the_Throne.html',message1=message1)
            else:
                message1="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Kanye-Watch_the_Throne.html',message1=message1)
        if button_value=='2': 
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message2="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',62)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Kanye-Watch_the_Throne.html',message2=message2)
            else:
                message2="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Kanye-Watch_the_Throne.html',message2=message2)
        if button_value=='3':  
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message3="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',63)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Kanye-Watch_the_Throne.html',message3=message3)
            else:
                message3="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Kanye-Watch_the_Throne.html',message3=message3)
        if button_value=='4':    
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message4="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',64)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Kanye-Watch_the_Throne.html',message4=message4)
            else:
                message4="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Kanye-Watch_the_Throne.html',message4=message4)
        if button_value=='5': 
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message5="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',65)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Kanye-Watch_the_Throne.html',message5=message5)
            else:
                message5="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Kanye-Watch_the_Throne.html',message5=message5)
    else:
        return render_template('songs-Kanye-Watch_the_Throne.html')

@app.route('/songs-Kanye-Ye.html', methods=['POST','GET'])
def submit9():
    dict={"1":"Ghost Town(4:30)","2":"Wouldnt Leave(3:26)","3":"All Mine(2:26)","4":"No Mistakes(2:03)","5":"Yikes(4:03)"}
    if request.method=='POST':
        button_value=request.form['name']    
        if button_value=='1':    
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message1="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',66)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Kanye-Ye.html',message1=message1)
            else:
                message1="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Kanye-Ye.html',message1=message1)
        if button_value=='2': 
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message2="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',67)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Kanye-Ye.html',message2=message2)
            else:
                message2="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Kanye-Ye.html',message2=message2)
        if button_value=='3':  
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message3="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',68)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Kanye-Ye.html',message3=message3)
            else:
                message3="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Kanye-Ye.html',message3=message3)
        if button_value=='4':    
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message4="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',69)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Kanye-Ye.html',message4=message4)
            else:
                message4="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Kanye-Ye.html',message4=message4)
        if button_value=='5': 
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message5="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',70)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Kanye-Ye.html',message5=message5)
            else:
                message5="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Kanye-Ye.html',message5=message5)
    else:
        return render_template('songs-Kanye-Ye.html')

@app.route('/songs-Kanye-Yezus.html', methods=['POST','GET'])
def submit10():
    dict={"1":"I Am a God(3:52)","2":"On Sight(2:37)","3":"Im in it(3:55)","4":"Guilt Trip(4:04)","5":"Bound 2(3:49)"}
    if request.method=='POST':
        button_value=request.form['name']    
        if button_value=='1':    
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message1="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',71)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Kanye-Yezus.html',message1=message1)
            else:
                message1="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Kanye-Yezus.html',message1=message1)
        if button_value=='2': 
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message2="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',72)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Kanye-Yezus.html',message2=message2)
            else:
                message2="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Kanye-Yezus.html',message2=message2)
        if button_value=='3':  
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message3="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}'73)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Kanye-Yezus.html',message3=message3)
            else:
                message3="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Kanye-Yezus.html',message3=message3)
        if button_value=='4':    
            print(dict[button_value]) 
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message4="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',74)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Kanye-Yezus.html',message4=message4)
            else:
                message4="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Kanye-Yezus.html',message4=message4)
        if button_value=='5': 
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message5="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',75)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Kanye-Yezus.html',message5=message5)
            else:
                message5="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Kanye-Yezus.html',message5=message5)
    else:
        return render_template('songs-Kanye-Yezus.html') 

@app.route('/songs-Kendrick-Butterfly.html', methods=['POST','GET'])
def submit11():
    dict={"1":"Institutionalized(4:32)","2":"Wesleys Theory(4:47)","3":"These Walls(5:01)","4":"How Much a Dollar Cost(4:22)","5":"Complexion(4:23)"}
    if request.method=='POST':
        button_value=request.form['name']    
        if button_value=='1':    
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message1="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',76)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Kendrick-Butterfly.html',message1=message1)
            else:
                message1="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Kendrick-Butterfly.html',message1=message1)
        if button_value=='2': 
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message2="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',77)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Kendrick-Butterfly.html',message2=message2)
            else:
                message2="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Kendrick-Butterfly.html',message2=message2)
        if button_value=='3':  
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message3="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',78)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Kendrick-Butterfly.html',message3=message3)
            else:
                message3="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Kendrick-Butterfly.html',message3=message3)
        if button_value=='4':    
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message4="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',79)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Kendrick-Butterfly.html',message4=message4)
            else:
                message4="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Kendrick-Butterfly.html',message4=message4)
        if button_value=='5': 
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message5="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',80)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Kendrick-Butterfly.html',message5=message5)
            else:
                message5="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Kendrick-Butterfly.html',message5=message5)
    else:
        return render_template('songs-Kendrick-Butterfly.html') 

@app.route('/songs-Kendrick-C4.html', methods=['POST','GET'])
def submit12():
    dict={"1":"Still Huslin(4:25)","2":"Misunderstood(4:44)","3":"Phone Home(2:51)","4":"Welcome to C4(6:41)","5":"Play With Fire(4:27)"}
    if request.method=='POST':
        button_value=request.form['name']    
        if button_value=='1':    
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message1="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',81)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Kendrick-C4.html',message1=message1)
            else:
                message1="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Kendrick-C4.html',message1=message1)
        if button_value=='2': 
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message2="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',82)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Kendrick-C4.html',message2=message2)
            else:
                message2="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Kendrick-C4.html',message2=message2)
        if button_value=='3':  
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message3="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',83)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Kendrick-C4.html',message3=message3)
            else:
                message3="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Kendrick-C4.html',message3=message3)
        if button_value=='4':    
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message4="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',84)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Kendrick-C4.html',message4=message4)
            else:
                message4="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Kendrick-C4.html',message4=message4)
        if button_value=='5': 
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message5="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',85)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Kendrick-C4.html',message5=message5)
            else:
                message5="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Kendrick-C4.html',message5=message5)
    else:
        return render_template('songs-Kendrick-C4.html') 

@app.route('/songs-Kendrick-Damn.html', methods=['POST','GET'])
def submit13():
    dict={"1":"LOVE(3:33)","2":"LOYALTY(3:47)","3":"XXX(4:14)","4":"HUMBLE(2:57)","5":"YEAH(2:40)"}
    if request.method=='POST':
        button_value=request.form['name']    
        if button_value=='1':    
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message1="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',86)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Kendrick-Damn.html',message1=message1)
            else:
                message1="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Kendrick-Damn.html',message1=message1)
        if button_value=='2': 
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message2="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',87)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Kendrick-Damn.html',message2=message2)
            else:
                message2="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Kendrick-Damn.html',message2=message2)
        if button_value=='3':  
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message3="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',88)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Kendrick-Damn.html',message3=message3)
            else:
                message3="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Kendrick-Damn.html',message3=message3)
        if button_value=='4':    
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message4="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',89)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Kendrick-Damn.html',message4=message4)
            else:
                message4="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Kendrick-Damn.html',message4=message4)
        if button_value=='5': 
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message5="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',90)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Kendrick-Damn.html',message5=message5)
            else:
                message5="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Kendrick-Damn.html',message5=message5)
    else:
        return render_template('songs-Kendrick-Damn.html') 

@app.route('/songs-Kendrick-mAAD.html', methods=['POST','GET'])
def submit14():
    dict={"1":"m.A.A.d city(5:50)","2":"Money Trees(6:37)","3":"Poetic Justic(5:55)","4":"Compton(3:04)","5":"Good Kid(4:49)"}
    if request.method=='POST':
        button_value=request.form['name']    
        if button_value=='1':    
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message1="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',91)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Kendrick-mAAD.html',message1=message1)
            else:
                message1="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Kendrick-mAAD.html',message1=message1)
        if button_value=='2': 
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message2="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',92)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Kendrick-mAAD.html',message2=message2)
            else:
                message2="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Kendrick-mAAD.html',message2=message2)
        if button_value=='3':  
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message3="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',93)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Kendrick-mAAD.html',message3=message3)
            else:
                message3="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Kendrick-mAAD.html',message3=message3)
        if button_value=='4':    
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message4="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',94)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Kendrick-mAAD.html',message4=message4)
            else:
                message4="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Kendrick-mAAD.html',message4=message4)
        if button_value=='5': 
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message5="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',95)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Kendrick-mAAD.html',message5=message5)
            else:
                message5="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Kendrick-mAAD.html',message5=message5)
    else:
        return render_template('songs-Kendrick-mAAD.html') 

@app.route('/songs-Kendrick-Overly_Dedicate.html', methods=['POST','GET'])
def submit15():
    dict={"1":"Ignorance Is Bliss(3:28)","2":"Cut You Off(6:04)","3":"Opposites Attract(4:32)","4":"Michael Jordan(5:51)","5":"Growing Apart(3:41)"}
    if request.method=='POST':
        button_value=request.form['name']    
        if button_value=='1':    
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message1="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',96)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Kendrick-Overly_Dedicate.html',message1=message1)
            else:
                message1="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Kendrick-Overly_Dedicate.html',message1=message1)
        if button_value=='2': 
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message2="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',97)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Kendrick-Overly_Dedicate.html',message2=message2)
            else:
                message2="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Kendrick-Overly_Dedicate.html',message2=message2)
        if button_value=='3':  
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message3="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',98)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Kendrick-Overly_Dedicate.html',message3=message3)
            else:
                message3="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Kendrick-Overly_Dedicate.html',message3=message3)
        if button_value=='4':    
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message4="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',99)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Kendrick-Overly_Dedicate.html',message4=message4)
            else:
                message4="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Kendrick-Overly_Dedicate.html',message4=message4)
        if button_value=='5': 
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message5="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',100)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Kendrick-Overly_Dedicate.html',message5=message5)
            else:
                message5="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Kendrick-Overly_Dedicate.html',message5=message5)
    else:
        return render_template('songs-Kendrick-Overly_Dedicate.html')    

@app.route('/songs-Slayer-Angel_of_Death.html', methods=['POST','GET'])
def submit16():
    dict={"1":"Evil Has No Boundaries(4:54)","2":"Final Command(3:28)","3":"Rebirth(4:59)","4":"Final Death(2:44)","5":"Until I Live(4:31)"}
    if request.method=='POST':
        button_value=request.form['name']    
        if button_value=='1':    
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message1="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',101)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Slayer-Angel_of_Death.html',message1=message1)
            else:
                message1="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Slayer-Angel_of_Death.html',message1=message1)
        if button_value=='2': 
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message2="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',102)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Slayer-Angel_of_Death.html',message2=message2)
            else:
                message2="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Slayer-Angel_of_Death.html',message2=message2)
        if button_value=='3':  
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message3="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',103)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Slayer-Angel_of_Death.html',message3=message3)
            else:
                message3="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Slayer-Angel_of_Death.html',message3=message3)
        if button_value=='4':    
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message4="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',104)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Slayer-Angel_of_Death.html',message4=message4)
            else:
                message4="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Slayer-Angel_of_Death.html',message4=message4)
        if button_value=='5': 
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message5="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',105)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Slayer-Angel_of_Death.html',message5=message5)
            else:
                message5="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Slayer-Angel_of_Death.html',message5=message5)
    else:
        return render_template('songs-Slayer-Angel_of_Death.html')    

@app.route('/songs-Slayer-Hell_Awaits.html', methods=['POST','GET'])
def submit17():
    dict={"1":"Praise of Death(5:21)","2":"Hardening of the Arteries(3:55)","3":"Crypts of Eternity(6:40)","4":"Hell Awaits(6:16)","5":"Necrophiliac(3:46)"}
    if request.method=='POST':
        button_value=request.form['name']    
        if button_value=='1':    
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message1="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',106)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Slayer-Hell_Awaits.html',message1=message1)
            else:
                message1="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Slayer-Hell_Awaits.html',message1=message1)
        if button_value=='2': 
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message2="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',107)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Slayer-Hell_Awaits.html',message2=message2)
            else:
                message2="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Slayer-Hell_Awaits.html',message2=message2)
        if button_value=='3':  
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message3="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',108)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Slayer-Hell_Awaits.html',message3=message3)
            else:
                message3="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Slayer-Hell_Awaits.html',message3=message3)
        if button_value=='4':    
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message4="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',109)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Slayer-Hell_Awaits.html',message4=message4)
            else:
                message4="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Slayer-Hell_Awaits.html',message4=message4)
        if button_value=='5': 
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message5="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',110)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Slayer-Hell_Awaits.html',message5=message5)
            else:
                message5="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Slayer-Hell_Awaits.html',message5=message5)
    else:
        return render_template('songs-Slayer-Hell_Awaits.html')    

@app.route('/songs-Slayer-Live_Undead.html', methods=['POST','GET'])
def submit18():
    dict={"1":"Black Magic(4:06)","2":"Die by the Sword(4:02)","3":"Final Command(2:33)","4":"Captor of Sin(3:29)","5":"Show No Mercy(3:03)"}
    if request.method=='POST':
        button_value=request.form['name']    
        if button_value=='1':    
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message1="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',111)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Slayer-Live_Undead.html',message1=message1)
            else:
                message1="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Slayer-Live_Undead.html',message1=message1)
        if button_value=='2': 
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message2="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',112)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Slayer-Live_Undead.html',message2=message2)
            else:
                message2="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Slayer-Live_Undead.html',message2=message2)
        if button_value=='3':  
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message3="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',113)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Slayer-Live_Undead.html',message3=message3)
            else:
                message3="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Slayer-Live_Undead.html',message3=message3)
        if button_value=='4':    
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message4="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',114)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Slayer-Live_Undead.html',message4=message4)
            else:
                message4="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Slayer-Live_Undead.html',message4=message4)
        if button_value=='5': 
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message5="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',115)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Slayer-Live_Undead.html',message5=message5)
            else:
                message5="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Slayer-Live_Undead.html',message5=message5)
    else:
        return render_template('songs-Slayer-Live_Undead.html')    

@app.route('/songs-Slayer-Reign_in_Blood.html', methods=['POST','GET'])
def submit19():
    dict={"1":"Postmertom(2:45)","2":"Reborn(2:12)","3":"Altar of Sacrifice(2:50)","4":"Jesus Saves(2:54)","5":"Criminally Insane(2:23)"}
    if request.method=='POST':
        button_value=request.form['name']    
        if button_value=='1':    
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message1="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',116)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Slayer-Reign_in_Blood.html',message1=message1)
            else:
                message1="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Slayer-Reign_in_Blood.html',message1=message1)
        if button_value=='2': 
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message2="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',117)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Slayer-Reign_in_Blood.htmll',message2=message2)
            else:
                message2="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Slayer-Reign_in_Blood.html',message2=message2)
        if button_value=='3':  
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message3="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',118)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Slayer-Reign_in_Blood.html',message3=message3)
            else:
                message3="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Slayer-Reign_in_Blood.html',message3=message3)
        if button_value=='4':    
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message4="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',119)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Slayer-Reign_in_Blood.html',message4=message4)
            else:
                message4="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Slayer-Reign_in_Blood.html',message4=message4)
        if button_value=='5': 
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message5="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',120)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Slayer-Reign_in_Blood.html',message5=message5)
            else:
                message5="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Slayer-Reign_in_Blood.html',message5=message5)
    else:
        return render_template('songs-Slayer-Reign_in_Blood.html')    

@app.route('/songs-Slayer-Show_No_Mercy.html', methods=['POST','GET'])
def submit20():
    dict={"1":"Black Magic(4:04)","2":"Tormentor(3:46)","3":"Crioinics(3:30)","4":"Show No Mercy(5:51)","5":"Antichrist(3:41)"}
    if request.method=='POST':
        button_value=request.form['name']    
        if button_value=='1':    
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message1="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',121)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Slayer-Show_No_Mercy.html',message1=message1)
            else:
                message1="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Slayer-Show_No_Mercy.html',message1=message1)
        if button_value=='2': 
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message2="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',122)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Slayer-Show_No_Mercy.html',message2=message2)
            else:
                message2="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Slayer-Show_No_Mercy.html',message2=message2)
        if button_value=='3':  
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message3="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',123)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Slayer-Show_No_Mercy.html',message3=message3)
            else:
                message3="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Slayer-Show_No_Mercy.html',message3=message3)
        if button_value=='4':    
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message4="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',124)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Slayer-Show_No_Mercy.html',message4=message4)
            else:
                message4="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Slayer-Show_No_Mercy.html',message4=message4)
        if button_value=='5': 
            print(dict[button_value]) 
            connection = sqlite3.connect("database.db")
            crsr = connection.cursor()
            crsr.execute(f"select * from song where songname = '{dict[button_value]}'")
            result=crsr.fetchone()
            if result is None:
            
                playlist.append(dict[button_value])
                message5="Added To Playlist"
                connection = sqlite3.connect("database.db")
                crsr = connection.cursor()
                
                
                sql_command=f"insert into song values ('{dict[button_value]}',125)"
                crsr.execute(sql_command)

                connection.commit()
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                
                    

                return render_template('songs-Slayer-Show_No_Mercy.html',message5=message5)
            else:
                message5="Already In Playlist"
                crsr.execute("select * from song")
                ans=crsr.fetchall()

                for i in ans:
                    print(i)
                return render_template('songs-Slayer-Show_No_Mercy.html',message5=message5)
    else:
        return render_template('songs-Slayer-Show_No_Mercy.html')    


@app.route('/playlist.html',methods=['POST','GET'])
def list_make():
    print(request.method)
    if request.method=='POST':
        delete_song=request.form['song_name']
        print(delete_song)
        connection = sqlite3.connect("database.db")
        crsr=connection.cursor()
        sql_command=f"DELETE FROM song where songname = '{delete_song}'"
        crsr.execute(sql_command)
        connection.commit()


        sql_command = "SELECT * FROM song"
        crsr.execute(sql_command)
        play = crsr.fetchall()
        song_names = [row[0] for row in play]
        return render_template('playlist.html', song_names=song_names)

    else:
        connection = sqlite3.connect("database.db")
        crsr = connection.cursor()
        sql_command = "SELECT * FROM song"
        crsr.execute(sql_command)
        play = crsr.fetchall()
        print(play)
        song_names = [row[0] for row in play]
        return render_template('playlist.html', song_names=song_names)
    

if __name__ == '__main__':
    app.run(port=5000)

