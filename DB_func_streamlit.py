import csv

class user:
    def __init__(self, username, password, balance):
        self.username = username
        self.password = password
        self.balance = balance


def read_db(read_to):
    with open('C:\\Users\\krist\\OneDrive\\Dokumenter\\code\\Projects\\folder_Elde_ATM\\Elde_ATM_streamlit\\pages\\Modules\\users.csv','r') as db_r:
        read_from_db = csv.reader(db_r)
        for line in read_from_db:
            if not len(line)==0:
                new_user = user(line[0],line[1],int(line[2]))
                read_to.append(new_user)
    return read_to


def write_db(write_to):
    with open('C:\\Users\\krist\\OneDrive\\Dokumenter\\code\\Projects\\folder_Elde_ATM\\Elde_ATM_streamlit\\pages\\Modules\\users.csv','w',newline='') as db_w:
        write_to_db = csv.writer(db_w,delimiter=',')
        for i in range(len(write_to)):
            data_line = write_to[i].username, write_to[i].password, write_to[i].balance
            write_to_db.writerow(data_line)


def append_db(append_to):
    with open('C:\\Users\\krist\\OneDrive\\Dokumenter\\code\\Projects\\folder_Elde_ATM\\Elde_ATM_streamlit\\pages\\Modules\\users.csv','a',newline='') as db_a:
        append_to_db = csv.writer(db_a,delimiter=',')
        for i in range(len(append_to)):
            data_line = append_to[i].username, append_to[i].password, append_to[i].balance
            append_to_db.writerow(data_line)

user1 = user('kri','123',500)
user2 = user('geir','456',6000)
user3 = user('kasp','666',900)
test_list=[user1,user2,user3]

empty_list = []
read_db(empty_list)
