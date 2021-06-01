import os
import json


json_dirs = './annos/video_annos'  # json文件路径
out_dir = './labels'  # 输出的 txt 文件路径


def main():
    # 读取 json 文件数据
    json_files = os.listdir(json_dirs)
    for file in json_files:
        json_file = json_dirs + '/' + file + '/' + 'tracks.json'
        with open(json_file, 'r') as load_f:
            content = json.load(load_f)
        # 循环处理
        filename = out_dir + '/' + file + '.txt'
        fp = open(filename, mode="w", encoding="utf-8")
        for t in content:
            if os.path.exists(filename):
                length = len(t['frames'])
                for i in range(length):
                    fp = open(filename, mode="r+", encoding="utf-8")
                    file_str = str(t['frames'][i]['frame id']) + ',' + str(t['track id']) + ',' + str(t['frames'][i]['rect']['tl']['x']) + ',' + str(t['frames'][i]['rect']['tl']['y']) +','\
                            + str(t['frames'][i]['rect']['br']['x']-t['frames'][i]['rect']['tl']['x']) + ',' + str(t['frames'][i]['rect']['br']['y']-t['frames'][i]['rect']['tl']['y']) + ','\
                            + str('-1') + ',' + str('-1') + ',' + str('-1') + ',' + str('-1')
                    line_data = fp.readlines()
                    if len(line_data) != 0:
                        fp.write('\n' + file_str)
                    else:
                        fp.write(file_str)
                    fp.close()
                    # 不存在则创建文件
            else:
                fp = open(filename, mode="w", encoding="utf-8")
                fp.close()
if __name__ == '__main__':
    main()