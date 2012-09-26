import youtube

emkay_user_id = 'ors1xsNFIoJEkx10co4akA'

def update_videos():
	yt = youtube.Youtube()
	videos_youtube = yt.get_videos_from_user(user_id=emkay_user_id)
	videos_saved = Video.objects.all()

	for video in videos_youtube:
		if videos_saved.contains(video):
			video_update = videos_saved.get(video)
			video_update.views = video.views
		else:
			new_video = Video()
			new_video.save()