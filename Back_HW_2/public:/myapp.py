def app(environ, start_response):
    with open("/Users/pc/PycharmProjects/VK_Backend/Back_HW_2/public:/Krang2.jpg", "rb") as imageFile:
        f = imageFile.read()
    start_response("200 OK", [
    ("Content-Type", "image\jpeg"),
    ("Content-Length", str(len(f)))
    ])
    return iter([f])