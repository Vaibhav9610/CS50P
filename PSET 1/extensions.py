file_name=input("File name: ")
file_name=file_name.lower()

if file_name.find(".gif")>=0:
    print("Image/gif")
elif file_name.find(".png")>=0:
    print("Image/png")
elif file_name.find(".jpg")>=0:
    print("Image/jpg")
elif file_name.find(".jpeg")>=0:
    print("Image/jpeg")
elif file_name.find(".pdf")>=0:
    print("Image/pdf")
elif file_name.find(".txt")>=0:
    print("Image/txt")
elif file_name.find(".zip")>=0:
    print("Image/zip")