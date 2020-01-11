# 剑网3：指尖江湖脚本
## 0. 使用教程
* 本工具仅支持`Android`手机，同时需要`Windows`操作系统配合，嫌麻烦可以不用。
* 自己无聊抽空做做的东西，后期只会更新优化算法和逻辑。
* 可能会更新其他内容(比如悬赏，捡垃圾)
* 可能会开发GUI
* 可能会开发apk应用
### 0.1 ADB安装
网上直接百度ADB安装包，或者clone本文中的ADB目录到你安装的位置即可。
详情点击[这里](https://jingyan.baidu.com/article/22fe7cedf67e353002617f25.html)
### 0.2 手机USB调试/电脑模拟器调试
#### 手机USB调试
首先将手机通过USB数据线连接电脑。
进入USB调试模式，需要先进入`开发者`选项
通常的方法是，找到`关于手机`-连续点击n次`安卓版本`-进入`开发者模式`，然后找到`辅助功能`-打开`USB调试`
若此方法不行请自行百度，可以参考[这里](https://jingyan.baidu.com/article/0aa22375ea166dc8cd0d6433.html)
#### 模拟器调试
模拟器不需要预先调试，不过本人目前暂时没有修改调整模拟器端口，不建议使用模拟器
### 0.3 检测是否调试成功
`Win+R`, 输入`cmd`回车打开cmd。
查看adb版本:
```
adb version
```
这是我的返回结果:
```
Android Debug Bridge version 1.0.40
Version 4797878
Installed as D:\ADB\adb.exe
```
然后输入：
```
adb devices
```
看到有一台设备已经连接，表示调试成功
```
List of devices attached
872QEDU4223KE   device
```
### 0.4 运行脚本
打开dist目录下的exe文件即可运行。
需要手动输入三个参数：
* 需要购买的物品编号
* 每次购买数量,`0表示买越多越好`
* 脚本运行时间，单位（秒）
