import glob
from PIL import Image
import os

ext_list = ['.jpg', 'JPG', '.JPEG', '.jpeg', '.png', '.PNG']

def cut(where):
    print(where)
    files = glob.iglob(where)
    for f in files:
        img = Image.open(f)
        x, y = img.size

        if x > y:
            box = img.crop((x//2+1, 0, x, y))
            title, ext = os.path.splitext(f)
            box.save(title + '_001' + ext, quality = 75)

            box = img.crop((0, 0, x//2, y))
            title, ext = os.path.splitext(f)
            box.save(title + '_002' + ext, quality = 75)

            os.remove(f)
            print('分割処理==>'+f)

print('フォルダをドラッグしてください')
dir_val = input()

print('==========分割の処理を開始==========')
for e in ext_list:
    cut(dir_val+'/*%s'%e)
print('==========終了==========\n')

for i in os.listdir(path='%s'%dir_val):
    if os.path.isdir(dir_val+'/'+i):
        print('とりあえず'+dir_val+'/'+i)
        print('=========='+i+'内の分割の処理を開始==========')
        for e in ext_list:
            cut(dir_val+'/'+i+'/*%s'%e)
        print('=========='+i+'は終了==========\n')