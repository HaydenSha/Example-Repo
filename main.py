from pytube import YouTube as yt



vid = input("put URL: " )

d = yt(vid)

dl = d.streams.filter(progressive = True, file_extension='mp4').order_by("resolution")[0]

dl.download('./')

print("download complete")