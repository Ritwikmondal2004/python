import json
def load_data():
    try:
        with open('youtube.txt','r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_data(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos,file)

def list_all_videos(videos):
    for index, video in enumerate(videos, start=1):
        print(f"{index}. Name: {video['name']}, Time: {video['time']}")# The enumerate function in the code is used to pair each video in the videos list with an index starting from 1, but its result is currently unused.
    

def add_video(videos):
    name=input("Enter video name:")
    time=input("Enter video time:")
    videos.append({"name":name,"time":time})
    save_data(videos)
def update_video(videos):
    pass
def delete_video(videos):
    pass
def main():
    videos=load_data()
    while True:
        print("\n youtube manneger |choose an option")
        print("1. list a favourite video")
        print("2. add a youtube video")
        print("3. update a youtube viddeo details")
        print("4. delete a youtube video")
        print("5. exit the app")
        choice=input("Enter your choice:")
        print(videos)

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                print("Thank you for using the app")
                break
            case _:
                print("Invalid choice, please try again")

if __name__ =="__main__":
    main()
# The above code is a basic structure for a YouTube manager application.
