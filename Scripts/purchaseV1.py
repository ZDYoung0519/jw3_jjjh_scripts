import os
import re
import time
import cv2


item_name = ['心魔票', '白帝票', '蛋']
score_bound = [0.90, 0.90, 0.8]


class ADBTools(object):

    def __init__(self):
        self.device_name = ''
        self.screen_size = ()
        self.log = ''
        self.screen_rate = ()
        self.port = ''

    def connect(self, port=0):
        os.system('adb start-sever | find"xxx"')
        if port == 0:
            os.system('adb devices | find "xxx"')
            self.port = 'USB'
        else:
            os.system('adb connect 127.0.0.1:5555')
            self.port = '127.0.0.1:5555'

        devices = re.match(r'attachedn(.*?)tdevice',
                           eval(repr(os.popen('adb devices').read()).replace('\\', ''))[16:]).group(1)
        self.device_name = devices
        self.screen_size = eval(os.popen('adb shell wm size | find "Physical size"').read()[15:19]), \
               eval(os.popen('adb shell wm size | find "Physical size"').read()[20:24])
        self.screen_rate = (self.screen_size[0]/1080, self.screen_size[1]/2160)
        print(self.write_log('连接设备成功'))

    def print_device_information(self):
        print('检测到设备：', self.device_name)
        print('屏幕分辨率：', self.screen_size)
        print('连接端口：', self.port)

    def tap(self, location):
        location = (round(location[0]*self.screen_rate[1]), round(location[1]*self.screen_rate[0]))
        os.system('adb shell input touchscreen tap' + ' ' + str(location[0]) + ' ' + str(location[1]))

    def swipe(self, start, end):
        start = (round(start[0] * self.screen_rate[1]), round(start[1] * self.screen_rate[0]))
        end = (round(end[0] * self.screen_rate[1]), round(end[1] * self.screen_rate[0]))
        os.system('adb shell input touchscreen swipe '
                   + str(start[0]) + " " + str(start[1]) + " " + str(end[0]) + " " + str(end[1]) + " ")

    def write_log(self, s):
        ss = time.strftime("%y-%m-%d, %H:%M:%S") + ':' + s
        self.log += ss + '\n'
        return ss

    def screen_shot(self, path='/sdcard/temp.png'):
        os.system('adb shell screencap -p' + ' ' + path)

    def pull(self, path1='/sdcard/temp.png', path2='./doc/temp.png'):
        os.system('adb pull ' + path1 + ' ' + path2 + ' ' + '|find "xxxx"')

    def hold_on(self, location, last_time):
        os.system('adb shell input swipe ' +
                  str(location[0]) + ' ' + str(location[1]) + ' ' +
                  str(location[0]) + ' ' + str(location[1]) + ' ' + str(last_time))


def get_target_location(img_target, img_template):
    H, W = img_template.shape[:2]
    res = 1-cv2.matchTemplate(img_target, img_template, cv2.TM_SQDIFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    center_loc = round(max_loc[0] + 0.5*W), round(max_loc[1] + 0.5*H)
    '''
    img = cv2.rectangle(img_target, max_loc, (max_loc[0] + W, max_loc[1] + H), (0, 0, 255), 3)
    img = cv2.circle(img, center_loc, 5, (0, 0, 255), -1)
    cv2.namedWindow('Image', 0)
    cv2.imshow('Image', img)
    cv2.waitKey(0)
    print(max_val)
    '''
    return max_val, center_loc


def purchase(port, id, num, duration):
    adb = ADBTools()
    print('-------------------')
    print(adb.write_log('开始连接设备'))
    try:
        adb.connect(port=port)
        adb.print_device_information()
        template = cv2.imread('../doc/template/' + str(id) + '.png', cv2.IMREAD_GRAYSCALE)
        start_time = time.time()
        now_time = start_time
        print('-------------------')
        print(adb.write_log('开始运行'))
        while now_time-start_time <= duration:
            t = 6
            t1 = time.time()
            while t > 0:
                adb.screen_shot(path='/sdcard/temp.png')
                adb.pull(path1='/sdcard/temp.png', path2='../doc/temp.png')
                target = cv2.imread('../doc/temp.png', cv2.IMREAD_GRAYSCALE)
                score, loc = get_target_location(target, template)
                if score <= score_bound[id]:
                    adb.swipe((1000, 850), (1000, 250))
                    time.sleep(0.0001)
                else:
                    # 点击物品
                    adb.tap(loc)
                    time.sleep(0.3)
                    # 增加数量
                    if num == 0:
                        adb.swipe((1520, 470), (1800, 470))
                    else:
                        for i in range(num - 1):
                            adb.tap((1835, 470))
                            time.sleep(0.001)
                    time.sleep(0.3)
                    # 点击购买
                    adb.tap((1670, 600))
                    time.sleep(0.3)
                    # 返回
                    adb.tap((0, 1000))
                    time.sleep(0.3)
                    t2 = time.time()
                    print(adb.write_log('找到' + item_name[id] + '并尝试购买') +
                          ',耗时：{:.2f}s'.format(t2-t1))
                    break
                t -= 1
            t2 = time.time()
            if t == 0:
                print(adb.write_log('没有找到' + item_name[id] +
                                    ',耗时：{:.2f}s'.format(t2-t1)))
            adb.tap((500, 940))
            now_time = time.time()
        print(adb.write_log('程序结束'))

        with open('../log/log.txt', 'a') as f:
            f.write(adb.log+'\n')
            f.close()
    except:
        print(adb.write_log('连接失败'))


if __name__ == '__main__':
    purchase(port=eval(input('输入端口')),
             id=eval(input('请输入所需物品的编号')),
             num=eval(input('请输入每次购买数量')),
             duration=eval(input('输入脚本运行时间(秒)'))
             )
