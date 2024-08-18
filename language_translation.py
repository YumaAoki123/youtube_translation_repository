import os

# ダウンロード先のフォルダパス
download_path = 'C:/download_youtube'

# ダウンロードしたいYouTube動画のURL（正しいURLに置き換えてください）
video_url = ''


# YouTubeオブジェクトを作成
yt = YouTube(video_url)

stream = yt.streams.first()

# ダウンロード先のフォルダが存在しない場合は作成
os.makedirs(download_path, exist_ok=True)

# 指定したフォルダに動画をダウンロード
stream.download(output_path=download_path, filename='downloaded_video.mp4')

print("動画のダウンロードが完了しました！")
