from TwitterAPI import TwitterAPI

consumer_key = 'S2Q3pQciEhSrBFAmOJuGjWgTP'
consumer_secret = 'cPiDwjIil0bfr9BFPEDhmPLHVb4Ozbtou3k0K2ky3nhazuRPpq'
access_token_key = '2797388610-osYUypGsFiO419HvefvLoXaIQ7EX7vENQ1UFG0f'
access_token_secret = 'xvhTkypU2uF7Kx17U1wa0SOeOVnNWEnyOOWohPitC3NEf'

api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)
r = api.request('statuses/filter', {'locations':'-74,40,-73,41'})
for item in r:
        print(item)
