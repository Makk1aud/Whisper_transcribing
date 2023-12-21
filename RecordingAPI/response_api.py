import requests

data = {
    "name":"Makklaud",
    "Surname":32432
}

url = ("http://127.0.0.1:5000/api/text/")
file_path = "E:/PythonProjects/WhisperRecording/Recording/Oleg_new.m4a"
response = requests.post(url, files={"file":open(file_path, 'rb')})
print(response.json())