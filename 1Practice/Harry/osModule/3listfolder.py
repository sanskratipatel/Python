import os

folders = os.listdir("data")
print(folders)

for fold in folders:
    print(os.listdir(f"data/{fold}"))
