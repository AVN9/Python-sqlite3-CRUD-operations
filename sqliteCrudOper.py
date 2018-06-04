import sqlite3

def createTables():
    conn=sqlite3.connect('example.db')

    createTables='''CREATE TABLE IF NOT EXISTS user (id integer primary key, name varchar, position varchar, phone varchar, office varchar);
                    CREATE TABLE IF NOT EXISTS experiment (id integer primary key, name varchar, researcher integer, description text, foreign key(researcher) references user(id));'''
    
    conn.executescript(createTables)
    conn.close()

def populateTables():
    conn=sqlite3.connect('example.db')

    script='''delete from user;
			delete from experiment;
			insert into user values (0, 'Namit', 'Research Director', '9998884321', '4b');
			insert into user values (1, 'Suresh', 'Research assistant', '8889994321', '17');
			insert into user values (2, 'Kirti', 'Research assistant', '6667774321', '24');
			insert into user values (3, 'Gaurav', 'Research assistant', '0225346789', '8');
			insert into user values (4, 'Mahesh', 'Toadie', 'None', 'Basement');
			insert into experiment values (0, 'Python anaconda', 0, 'A installer for python');
			insert into experiment values (1, 'Python matplolib', 2, 'Study of chart and data anlysis');'''

    conn.executescript(script)
    conn.commit()
    conn.close()

def printUsertable():
    print "\n"
    print "-------USER TABLE-------"
    print "\n"

    conn=sqlite3.connect('example.db')

    query="select * from user;"
    r = conn.execute(query)

    for i in r:
        print i

    conn.close()

def printExperimentTable():
    print "\n"
    print "-------EXPERIMENT TABLE-------"
    print "\n"

    conn=sqlite3.connect('example.db')

    query="select * from experiment;"
    r = conn.execute(query)

    for i in r:
    	print i

    conn.close()

def printExperimentDetails():
    print "\n"
    print "-------EXPERIMENT OWNER DETAILS-------"
    print "\n"

    conn=sqlite3.connect('example.db')

    query="select p.name, e.name from user as p join experiment as e where e.researcher == p.id;"
    r = conn.execute(query)

    for i in r:
    	print 'Name: %s\n\tExperiment: %s' % (i[0],i[1])    

def addNewUser(id,name,position,phone,office):
    conn = sqlite3.connect('example.db')

    query="insert into user values ( %d, '%s', '%s', '%s', '%s');" %(id,name,position,phone,office)
    conn.execute(query)
    conn.commit()

    conn.close()

def addNewExperiments(id,name,researcher,text):
    conn = sqlite3.connect('example.db')

    query="insert into experiment values ( %d, '%s', %d, '%s');" %(id,name,researcher,text)
    conn.execute(query)
    conn.commit()

    conn.close()

def removeUserReassignExp(addUserId):
    conn = sqlite3.connect('example.db')
    query="select p.name, e.id from user as p join experiment as e where e.researcher == p.id;"

    r = conn.execute(query)
    for i in r:
        if i[0] == 'Namit':
            removeUserId=i[1]

    query="update experiment set researcher = %d where researcher = %d;" %(addUserId,removeUserId)
    conn.execute(query)
    conn.commit()

    query="delete from user where id = %d;" %(removeUserId)
    conn.execute(query)
    conn.commit()

    conn.close()


if __name__ == "__main__":
    
    #Creating DB and Tables
    createTables();

    #Populating Tables
    populateTables();

    #Printing People Table 
    printUsertable();

    #Printing Experiment Table
    printExperimentTable();

    #Printing Experiment Owner Details
    printExperimentDetails();

    #Adding New User in People table 
    addNewUser(5,"Bret","Developer","9028690973","ABC");

    #Printing People Table
    printUsertable();
    
    #Adding New Experiment in Experiment table
    addNewExperiments(2, "Computer Study", 5, "Study in computer science");

    #Printing Experiment Table
    printExperimentTable();

    #Remove Alice and reassign her experiments
    removeUserReassignExp(5);

    #Printing People Table
    printUsertable();

    #Printing Experiment Table
    printExperimentTable();

    #Printing Experiment Owner Details
    printExperimentDetails();


