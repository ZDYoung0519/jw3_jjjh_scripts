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
### 0.2 手机USB调试
首先将手机通过USB数据线连接电脑。
进入USB调试模式，需要先进入`开发者`选项
通常的方法是，找到`关于手机`-连续点击n次`安卓版本`-进入`开发者模式`，然后找到`辅助功能`-打开`USB调试`
若此方法不行请自行百度，可以参考[这里](https://jingyan.baidu.com/article/0aa22375ea166dc8cd0d6433.html)
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
