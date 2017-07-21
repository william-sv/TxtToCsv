import csv
import logging

#定义日志格式
logging.basicConfig(level=logging.WARNING,
                    filename='./log.txt',
                    filemode='a',
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')


def open_txt(txtpath,csvfile, remove = [],i = 0, y = -1):
    '''
    :param txtpath: 需要读取的txt文件路径
    :param csvfile: 即将保存的csv文件
    :param remove[]: 不需要写入文件的行号
    :param i:起始行
    :param y:结束行
    :return: 若执行成功则print一条执行成功的提示，若失败，查看log文件
    '''
    tmp = []
    try:
        with open(csvfile, 'a') as c:
            writer = csv.writer(c)
            try:
                with open(txtpath, 'r') as f:
                    z = i
                    if i == 0:
                        i = i
                    else:
                        i -= 1
                    for n in f.readlines()[i:y]:
                        if z not in remove:#判断当前行是否需要remove
                            for str in n.split('|'):#拆分str
                                if str.strip() != '':#删除首尾的空格
                                    tmp.append(str.strip())#将处理好的str添加到tmp[]中
                            try:
                                writer.writerow(tmp)#调用writer方法写入csv文件中
                                tmp = []#将tmp[]清空
                            except Exception as e:
                                logging.error(e)
                        z+=1
            except Exception as e:
                logging.error(e)
    except Exception as e:
        logging.error(e)

    print('已处理完成，具体请查看 ' + csvfile + ' 文件！')

txtpath = './20151218-20161231_03.txt'
csvfile = './csv1.csv'
open_txt(txtpath, csvfile)