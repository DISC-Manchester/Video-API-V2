from flask import Flask, request

app = Flask("VideoAPI")

videos = {}

@app.route('/videos/<video_id>', methods=["POST"])
def create_video(video_id):
  data = request.json
  videos[video_id] = data
  return "", 201

@app.route('/videos', methods=["GET"])
def read_all_videos():
  return videos, 200

@app.route('/videos/<video_id>', methods=["GET"])
def read_one_video(video_id):
  if video_id not in videos.keys():
    return "", 404
  return videos[video_id], 200

@app.route('/videos/<video_id>', methods=["PUT"])
def update_one_video(video_id):
  data = request.json
  if video_id not in videos.keys():
    return "", 404
  videos[video_id] = data
  return videos[video_id], 200

@app.route('/videos/<video_id>', methods=["DELETE"])
def delete_one_video(video_id):
  if video_id not in videos.keys():
    return "", 404
  del videos[video_id]
  return "", 204

if __name__ == "__main__":
  app.run()