from cv2 import imshow
import firebase_admin
from firebase_admin import credentials, storage
import numpy as np
import cv2



cred = credentials.Certificate('key.json')
app = firebase_admin.initialize_app(cred, {'storageBucket': 'camera-bird-feeder-f06ef.appspot.com'})

bucket = storage.bucket()
blob = bucket.blob('rick.png')

arr = np.frombuffer(blob.download_as_string(), dtype=np.uint8)

img = cv2.imdecode(arr, cv2.COLOR_RGB2BGR555)

imshow('rick', img)
cv2.waitKey(0)