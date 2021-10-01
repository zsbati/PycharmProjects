def tracklist(**kwargs):
    for key in kwargs:
        print(key) 
        item = kwargs.get(key)
        for k in item.keys():
            print('ALBUM:', str(k), 'TRACK:', str(item.get(k)))
