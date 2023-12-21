from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import shutil


app = Flask(__name__)
CORS(app)
@app.route("/api/text/", methods=["POST"])
def translatetext():
    if 'file' not in request.files:
        data = {
            "text": "No File"
        }
        return jsonify(data)
    file = request.files['file']
    SaveUserFile(file)
    CopyFile(file.filename)
    text = WhisperFromCmd(file.filename)

    data = {
        "text": text
    }
    return jsonify(data)

current_file = os.path.realpath(__file__)
current_directory = os.path.dirname(current_file)

audio_files_path = current_directory + "/AudioFiles/"
audio_text_files_path = current_directory + "/AudioAndTextFiles/"
def SaveUserFile(file):
    filename = file.filename
    file_save_path = "E:/PythonProjects/RecordingAPI/AudioFiles"
    file.save(os.path.join('AudioFiles', filename))

def CopyFile(filename):
    baseDirectory = audio_files_path + filename
    necDirectory = audio_text_files_path + filename
    shutil.copy(baseDirectory, necDirectory)

def WhisperFromCmd(filename):
    path = audio_text_files_path
    os.chdir(path)
    userFileNameWithType = filename.rsplit('.', 1)[0] + '.txt'

    commandToWhisper = "whisper " + filename + " --language Russian"
    os.system(commandToWhisper)
    file = open(f"{path}/{userFileNameWithType}", "r", encoding="utf-8", errors='ignore')

    os.chdir(current_directory)
    return file.read()

if __name__ == "__main__":
    app.run()
