import os
import json


txt_dirs = './labels'  # json文件路径
out_dir = './txt_labels'  # 输出的 txt 文件路径

def main():
    txt_files = os.listdir(txt_dirs)
    for file in txt_files:
        print('!!!!!!!!!!!!!!!!!', file)
        folder_number = file.split('_')[0]
        dir_name = os.path.join(out_dir, folder_number)
        if os.path.isdir(dir_name):
            pass
        else:
            os.mkdir(dir_name)
        txt_file = txt_dirs + '/' + file
        with open(txt_file, 'r') as load_f:
            for line in load_f.readlines():
                frame = line.strip().split(',')[1]
                num = "%03d"%int(frame)
                filename = dir_name + '/' + 'SEQ_' + folder_number + '_' + num + '.txt'
                fp = open(filename, mode="a+", encoding="utf-8")
                fp.write(line)
                fp.close()

if __name__ == '__main__':
    main()