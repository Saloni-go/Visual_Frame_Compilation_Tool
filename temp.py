import cv2
import os
import mysql.connector
import numpy as np

db_config={
    'host':'localhost',
    'user': 'saloni_goyal',
    'password': 'Saloni_goyal307',
    'database': 'project'
}

conn=mysql.connector.connect(**db_config)
cursor=conn.cursor()


#IMAGE->VIDEO

cursor.execute("DELETE FROM images")
conn.commit()

cursor.execute("""CREATE TABLE IF NOT EXISTS images ( id INT AUTO_INCREMENT PRIMARY KEY, image_title VARCHAR(255), image_data LONGBLOB)""")

image_folder="media/"

for image in os.listdir(image_folder):
    if image.endswith(".jpg") or image.endswith(".jpeg") or image.endswith(".png"):
        image_path=os.path.join(image_folder,image)
        with open(image_path, 'rb') as f:
            image_data=f.read()   #is reading in rb mode i.e. binary read mode , this is where its converting it into blob data
        cursor.execute("INSERT INTO images(image_title, image_data) VALUES (%s, %s)",(image,  image_data))
        conn.commit()

cursor.execute("SELECT image_data FROM images")
rows=cursor.fetchall()

if not rows: 
    print("database empty\n")
    exit()



# path="media/"
# out_path="video/"
out_video_name="output_video.mp4"
out_video_full_path=os.path.join(image_folder, out_video_name)


#video frame *STANDARD* FOR EACH PHOTO FOR US!
target_width=800
target_height=600


cv2_fourcc=cv2.VideoWriter_fourcc(*'mp4v')

video=cv2.VideoWriter(out_video_full_path, cv2_fourcc, (1), (target_width,target_height))

# print(video)
for image in os.listdir(image_folder):
    if image.endswith(".jpg") or image.endswith(".jpeg") or image.endswith(".png"):
        image_path=os.path.join(image_folder, image)
        frame=cv2.imread(image_path)
        if frame is not None:
            resized_frame=cv2.resize(frame, (target_width, target_height))
            video.write(resized_frame)
        else:
            print(f"Error loading frame {image}.")



video.release()
print("ouput video saved to:", out_video_full_path)

#AUDIO


audio_folder="audio/"
output_audio_folder="output_audio/"

os.makedirs(audio_folder, exist_ok=True) #create output folder if it not exists

cursor.execute("""CREATE TABLE IF NOT EXISTS audio_2(id INT AUTO_INCREMENT PRIMARY KEY, audio_title VARCHAR(255), audio_data LONGBLOB)""")
cursor.execute("DELETE FROM audio_2")
conn.commit()
for audio_file in os.listdir(audio_folder):
    if audio_file.endswith(".mp3") or audio_file.endswith(".wav"):
        audio_path=os.path.join(audio_folder, audio_file)
        audio_title=os.path.splitext(audio_file)[0]
        with open(audio_path, 'rb') as f:
            audio_data=f.read()
        cursor.execute("INSERT INTO audio_2 (audio_title, audio_data) VALUES (%s, %s)",(audio_title, audio_data))
        conn.commit()

def retrieve_and_save_audios():
    cursor.execute("SELECT audio_title, audio_Data FROM audio_2")
    audio_records=cursor.fetchall()
    

    for audio_record in audio_records:
        audio_title, audio_data=audio_record

        audio_file_path=os.path.join(output_audio_folder,f"{audio_title}.mp3")

        #write audio data to file
        with open(audio_file_path, 'wb') as audio_file:
            audio_file.write(audio_data)
        # print(f"Audio'{audio_title}' saved to '{audio_file_path}'")

retrieve_and_save_audios()
cursor.close()
conn.close()