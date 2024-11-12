import datetime
import random
import sqlite3

def main():
    add_data_to_all(get_data())


def get_data():
    # Get list of bus stops
    bus_stops = list()
    with open(r"C:\Users\nafla\OneDrive\Documents\Hackathon\GTFS_MATA\stops.txt") as stops_file:
        for line in stops_file:
            current_line = line.split(",")
            bus_stops.append(current_line[0])

    # Get random Ids
    ids = list()
    for _ in range(500):
        id = random.randint(100,150)
        if id not in ids:
            ids.append(id)
    print(ids)

    # Get random times
    times = list()
    start_time = datetime.time(6,0)
    end_time = datetime.time(18,0)

    for _ in range(100):
        random_seconds = random.randint(0, (end_time.hour * 3600) + (end_time.minute * 60) + end_time.second)
        random_time = (datetime.datetime.combine(datetime.date.today(), start_time) + datetime.timedelta(seconds=random_seconds)).time()
        times.append(random_time)
   

    # Generate random scenarios for database
    datas = list()
    for i in range(len(ids)):
        data = list()
        data.append(ids[i])
        pt = random.randint(0,len(bus_stops)-1)
        data.append(bus_stops[pt])
        pt = random.randint(0,len(times)-1)
        data.append(times[pt])
        datas.append(data)
    print(datas)
    return datas
        


def add_data_to_all(datas):

    # Add data to database
    
    for data in datas:
        id = data[0]
        location = data[1]
        pre_time = data[2]
        hour = f"{pre_time.hour:02d}"
        minute = f"{pre_time.minute:02d}"
        second = f"{pre_time.second:02d}"
        time = f"{hour}:{minute}:{second}"
        
        # Add to SQL database
        conn = sqlite3.connect('all.db')
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS allData (id REAL, location char, time TIME)')
        cursor.execute('INSERT INTO allData (id, location, time) VALUES (?, ?, ?)', (id, location, time))
        conn.commit()
        conn.close()
    
def drop_all():
    table_name = 'allData'
    conn = sqlite3.connect('all.db')
    cursor = conn.cursor()
    cursor.execute(f'DROP Table IF EXISTS {table_name}')
    conn.commit()
    conn.close()

  
    


      


if __name__ == "__main__":
    main()
