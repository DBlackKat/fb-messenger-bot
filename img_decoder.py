import qrtools,urllib

def decode_img(url_img,img_name):
    image = urllib.URLopener()
    image.retrieve(url,img_name)
    qr = qrtools.QR()
    qr.decode(img_name)
    return qr.data
