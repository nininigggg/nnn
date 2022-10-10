#'a+'表示追加，若没有文件则创建，有则追加
fp = open('/Users/nnn/Downloads/001.txt', 'a+')
print('helloworld', file=fp)
fp.close()
