from flask import Flask
import subprocess
import json

app = Flask(__name__)

@app.route("/soundcards")
def getSoundcards():
    indexCmd = ["pacmd list-sinks | grep index:"]
    indexP = subprocess.Popen(indexCmd,
                                    shell=True,
                                    stdout = subprocess.PIPE,
                                    stderr=subprocess.PIPE,
                                    stdin=subprocess.PIPE)
    indexRawData, err = indexP.communicate()
    indexRawData = indexRawData.replace('index:','').replace('*','')
    indexArray = indexRawData.split('\n')

    nameCmd = ["pacmd list-sinks | grep name:"]
    nameP = subprocess.Popen(nameCmd,
                                    shell=True,
                                    stdout = subprocess.PIPE,
                                    stderr=subprocess.PIPE,
                                    stdin=subprocess.PIPE)
    nameRawData, err = nameP.communicate()
    nameRawData = nameRawData.replace('name:','').replace('\t', '').replace('<', '').replace('>', '')
    nameArray = nameRawData.split('\n')

    mutedCmd = ["pacmd list-sinks | grep muted:"]
    mutedP = subprocess.Popen(mutedCmd,
                                    shell=True,
                                    stdout = subprocess.PIPE,
                                    stderr=subprocess.PIPE,
                                    stdin=subprocess.PIPE)
    mutedRawData, err = mutedP.communicate()
    mutedRawData = mutedRawData.replace('muted:','').replace('\t', '')
    mutedArray = mutedRawData.split('\n')

    soundcards = []
    class Object(object):
        pass
    for i in range(len(indexArray)-1):
        soundcard = Object()
        soundcard.index = indexArray[i].strip()
        soundcard.name = nameArray[i].strip()
    #    soundcard.volume = volumeArray[i].strip()
        soundcard.muted = mutedArray[i].strip()
        soundcards.append(soundcard)

    def obj_dict(obj):
        return obj.__dict__

    jsonData = json.dumps(soundcards, default=obj_dict)

    return jsonData


@app.route("/volume/<soundcardId>/<percentValue>", methods=['POST'])
def volumeChange(soundcardId, percentValue):
    cmd = ["pactl", "set-sink-volume", soundcardId, percentValue + "%"]
    p = subprocess.Popen(cmd,
                            stdout = subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)
    out,err = p.communicate()
    return out

@app.route("/play", methods=['POST'])
def play():
    cmd = ["echo \"loadfile %s" > pipe", % weatherFile.soundFile]
    playP = subprocess.Popen(cmd,
                            shell = True,
                            stdout = subprocess.PIPE,
                            stderr = subprocess.PIPE,
                            stdin = subprocess.PIPE)
    out,err = playP.communicate()
    return out

@app.route("/pause", methods=['POST'])
def pause():
    cmd = ["echo \"pause\" > pipe"]
    pauseP = subprocess.Popen(cmd,
                            shell = True,
                            stdout = subprocess.PIPE,
                            stderr = subprocess.PIPE,
                            stdin = subprocess.PIPE)
    out,err = pauseP.communicate()
    return out

@app.route("/stop", methods=['POST'])
def stop():
    cmd = ["echo \"stop\" > pipe"]
    stopP = subprocess.Popen(cmd,
                            shell = True,
                            stdout = subprocess.PIPE,
                            stderr = subprocess.PIPE,
                            stdin = subprocess.PIPE)
    out,err = stopP.communicate()
    return out

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug = 'True')
