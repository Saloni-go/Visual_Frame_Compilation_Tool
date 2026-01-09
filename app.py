from flask import Flask, render_template
import subprocess

app=Flask(__name__)

def generate_video_resolutions(input_video,resolutions):
    for res in resolutions:
        output_video=f'output_video_{res}.mp4'
        cmd=f'ffmpeg -i {input_video} -vf scale={res} -c:v libx264 -crf 23 -preset medium -c:a aac -b:a 128k {output_video}'
        subprocess.run(cmd,shell=True)

@app.route('/')
def index():
    input_video="Mera saya sath hoga @MakeJokeOf _ Saurabh Shukla.mp4"
    resolutions=['1920x1080', '1280x720', '854x480']


    generate_video_resolutions(input_video, resolutions)
    return render_template('resolution.html')

if __name__=='__main__':
    app.run(debug=True)


