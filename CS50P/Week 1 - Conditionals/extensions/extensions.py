def main():
    file = input("File Name: ")
    print(extension(file))

def extension(file):
    if(len(file.split(".")) == 1):
        return "application/octet-stream"

    types = ["gif","jpg","jpeg","png",
             "pdf","txt","zip"]
    exten = file.split(".")[-1].lower().strip()
    name = file.split(".")[0].lower().strip()
    if(exten not in types):
        return "application/octet-stream"
    else:
        if(exten=="pdf" or exten=="zip"):
            return (f'application/{exten}')
        elif(exten=="txt"):
            return (f'text/{name}')
        elif(exten=="gif" or exten=="png"):
            return (f'image/{exten}')
        else:
            return ('image/jpeg')




main()
