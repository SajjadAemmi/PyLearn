import pytube

link = 'https://www.youtube.com/watch?v=lVFNRrL79w0'
first_stream = pytube.YouTube(link).streams.first()
first_stream.download(output_path='./', filename='test.mp4')