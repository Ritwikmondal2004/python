import sqlite3

conn = sqlite3.connect('youtube.db')

cursor =conn.cursor()
cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )

''')

def list_all_videos():
    print("\n")
    print("*"*70)
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)
    print("\n")
    print("*"*70)
def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()
def update_video(video_id, new_name, new_time):
    cursor.execute("update videos set name=?, time=? where id=?",(new_name, new_time, video_id))
    conn.commit()
def video_id():
    cursor.execute("delete from videos where id=?",(video_id,))
    conn.commit()
    
def delete_video(video_id):
    cursor.execute("delete from videos where id=?",(video_id,))
    conn.commit()
    
def main():
    while True:
        print("\n youtube manager app with DB")
        print("1. list a favourite video")
        print("2. add a youtube video")
        print("3. update a youtube video details")
        print("4. delete a youtube video")
        print("5. exit the app")
        choice = input("Enter your choice: ")

        if not choice.strip():
            print('--------------------empty--------------------')
            continue

        if choice=='1':
            list_all_videos()
        elif choice=='2':
            name=input("Enter video name:")
            time=input("Enter video time:")
            add_video(name, time)
        elif choice=='3':
            video_id= input("enter a video id to update: ")
            name=input("Enter video name: ")
            time=input("Enter video time: ")
            add_video(name, time)
        elif choice== '4':
            video_id= input("enter a video id to delete: ")
            delete_video(video_id)
        elif choice=='5':
            print("Thank you for using the app")
            break
        else:
            print("Invalid choice, please try again")
    conn.commit()
# def save_data(videos):

if __name__ == "__main__":
    main()
# def load_data():