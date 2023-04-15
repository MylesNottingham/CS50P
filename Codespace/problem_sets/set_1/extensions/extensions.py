# File Extensions



# Prompts user for input then remove case and remove whitespace
e = input("File name: ").lower().strip()

# Checks file name for extension type and prints appropriate media type
if e.endswith(".gif") == True:
    print("image/gif")
elif e.endswith(".jpg") or e.endswith(".jpeg")== True:
    print("image/jpeg")
elif e.endswith(".png")== True:
    print("image/png")
elif e.endswith(".pdf")== True:
    print("application/pdf")
elif e.endswith(".txt")== True:
    print("text/plain")
elif e.endswith(".zip")== True:
    print("application/zip")
else:
    print("application/octet-stream")