def getMimeType(fileName):
    extension = fileName.split('.')[-1].lower()

    if extension == 'gif':
        return 'image/gif'
    elif extension in ['jpg', 'jpeg']:
        return 'image/jpeg'
    elif extension == 'png':
        return 'image/png'
    elif extension == 'pdf':
        return 'application/pdf'
    elif extension == 'txt':
        return 'text/plain'
    elif extension == 'zip':
        return 'application/zip'
    else:
        return 'application/octet-stream'

fileName = input("File name: ")
mimeType = getMimeType(fileName)
print(mimeType)