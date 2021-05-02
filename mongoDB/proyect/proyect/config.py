from decouple import config

URL = 'mongodb+srv://Victor:{}@cluster0-qrmuf.mongodb.net/test?retryWrites=true&w=majority'.format(
    config('MongoDB_PASSWORD', default='password')
    )
