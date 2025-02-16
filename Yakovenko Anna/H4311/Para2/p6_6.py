import os


def collector(path_w):
    path = os.path.normpath(path_w)
    result = {"dirs": [], "files":[]}
    for path, dirnames in os.walk(path):
        for dir in dirnames:
            result["dirs"]. append(dir)
            for file in filenames:
                result["files"].append(file)
    with open("result_check.txt","w") as res:
        res.write(f"{'Directory':=^35}\n")
        for i in result["dirs"]:
            res.write(f)





path_check = "C:\Windows\Web"
collector(path_check)
