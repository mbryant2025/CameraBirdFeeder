import picamera
from firebase_admin import credentials, initialize_app, storage


with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)

    camera.capture('image.jpg')

cred = credentials.Certificate('/home/pi/Documents/key.json')
initialize_app(cred, {'storageBucket': 'camera-bird-feeder-f06ef.appspot.com'})

# Put your local file path 
fileName = "image.jpg"
bucket = storage.bucket()
blob = bucket.blob(fileName)
blob.upload_from_filename(fileName)

# Opt : if you want to make public access from the URL
blob.make_public()


