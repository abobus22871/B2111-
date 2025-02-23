import os, datetime


def collector(path, res_path):
    path = os.path.normpath(path)
    res_path = os.path.normpath(res_path)
    for pathname, dirname, filename in os.walk(path):
        for file in filename:
            file_time = os.path.getmtime(f"{pathname}\\{file}")
            date_time = datetime.datetime.fromtimestamp(file_time)
            file_date = date_time.strftime('%d.%m.%Y')
            if os.path.isdir(f"{res_path}\\{file_date}"):
                shutil.copyfile(f"{pathname}\\{file}", f"{res_path}\\{file_date}\\{file}")
            else:
                os.mkdir(f"{res_path}\\{file_date}")
                shutil.copyfile(f"{pathname}\\{file}", f"{res_path}\\{file_date}\\{file}")


path_tar = "C:/Windows/Web"
path_dest ="D:\goronovich michail\B2111-\Yakovenko Anna\H4311\Para2\Result"
collector(path_tar, path_dest)