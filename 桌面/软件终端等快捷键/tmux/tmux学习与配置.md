## tmux学习与配置

### 一、 主线教程

**请根据下面链接中的教程进行学习**

<https://my.oschina.net/am313/blog/865915>

**重要的：这里提供了两种不同的配置方案，分别是1和2是一种，另一种是3，两者并不兼容，如果按照顺序依次配置，最后3会将1和2新添加的配置顶掉，请自行选择。**

#### 1. 直到链接中的“简易美化”一栏，这里出现了关于tmux的配置问题的坑，我们先按照如下方式进行配置：

(1).若无配置文件，则创建配置文件：终端输入：touch ~/.tmux.conf 
(2).终端打开配置文件（conf文件）: open -e ~/.tmux.conf 
` -e [指的是使用文本编辑器打开]`
` open -a 应用名 被打开文件地址 [指定软件打开文件地址]`
` open -t 文件地址 ［默认应用打开文件］`

(3).输入如下内容，并保存：
```
# Send prefix
set-option -g prefix C-a
unbind-key C-a
bind-key C-a send-prefix

# Use Alt-arrow keys to switch panes
bind -n M-Left select-pane -L
bind -n M-Right select-pane -R
bind -n M-Up select-pane -U
bind -n M-Down select-pane -D

# Shift arrow to switch windows
bind -n S-Left previous-window
bind -n S-Right next-window

# Mouse mode
set -g mouse on


# Set easier window split keys
bind-key v split-window -h
bind-key h split-window -v

# Easy config reload
bind-key r source-file ~/.tmux.conf \; display-message "tmux.conf reloaded"
```

(4).现在返回iterm终端界面，查看是否有还在后台的session,只有删除所有的旧的session后，配置才能在新建的session中生效。

```
tmux ls
tmux kill-session -t <session-name>
```
**第一行的意思是：查看当前所有的session**
**第二行的意思是：删除指定的session**

这个点子来源于来自如下链接中的“4”：
<https://www.jianshu.com/p/fd3bbdba9dc9>

(5).tmux发生的改变

(5.1)前缀键变为: ctrl + a (下面统称ca)

(5.2)切换屏幕的几种方式：
ca + 方向键; 
alt + 方向键中的上下键 [只能上下移动，无法左右];
鼠标点击切换

(5.3)分屏的方式：
ca + v 竖分屏 ca + v 横分屏;
ca + % 竖分屏 ca + “ 横分屏

(5.4)alt + 方向键左右键，跳到单词的首尾

#### 2.现在我们返回主线教程，开始学习如何将“简易美化”中的配置加入到配置文件中：

`用1.中(2)的方式打开配置文件，输入配置，并保存。`
`用1.中(4)的方式删除旧的session，新建session,然后即可看到生效。`

#### 3.另一种配置

打开主线教程“进阶美化”一栏中的`github链接`，记住不要按照主线链接中所说的方式进行安装，这会安装失败。
我推荐，github中配置作者的安装方式：

打开终端，依次输入以下命令(是$ 后面的那个)：
```
$ cd
$ git clone https://github.com/gpakosz/.tmux.git
$ ln -s -f .tmux/.tmux.conf
$ cp .tmux/.tmux.conf.local .
```
即可配置成功，然后在重新清除和新建session，就能看到效果了。
安装完此配置后：前缀键变成了ctrl + a

**另外可以重新打开~/.tmux.conf,输入以下内容**
```
bind j split-window -h
bind l split-window -v

setw -g window-status-current-fg white
setw -g window-status-current-bg red
setw -g window-status-current-attr bright
 
set -g status-justify left
 
setw -g monitor-activity on

# 支持鼠标选择窗口，调节窗口大小
set -g mouse on
set -s escape-time 1

# 调节窗口大小快捷键,左下上右
bind -r H resize-pane -L 3
bind -r J resize-pane -D 3
bind -r K resize-pane -U 3
bind -r L resize-pane -R 3
```
新添加的功能：
可将竖分屏快捷键改为：cb + j;横分屏：cb + l
支持鼠标选择窗口，调节窗口大小。

## 二.通用的快捷键总结

**tmux:**

```
前缀键：ctrl + b (以下简称cb)

tmux new -s <name>             创建一个新的session,同时创建默认的window
tmux new -s <name> -n <name1>  同时创建名称为name1的window
tmux ls                        查看有多少会话

cb + d                         暂时离开session，但并不会删除会话
tmux attach(-a) -t <name>      返回对应的session
tmux a                         快速连接第一个回话

tmux kill-session -t <name>    彻底删除对应的session


window(窗口)操作

cb + c                         当处于一个window下时，可以创建一个新的窗口
cb + p                         自动切换到上一个窗口
cb + n                         切换到下一个
cb + ,                         重命名当前窗口，重命名的方式在窗口下面
cb + w                         列出所有的窗口

pane(分屏)操作
cb + （shift(以下称sh) + 5 )/[即％]       创建竖分屏
cb + “                                  创建横分屏
cb + 方向键                              切换各分屏
cb + 1                                  显示分屏编号
exit                                  退出本分屏／退出最后一个分屏后，同时永久删除本会话
cb + x                                  关闭当前分屏，下面的提示界面要求要输入y,进行确认
cb + q                                  显示分屏编号
cb + d                                  暂时退出会话
cb + (sh + 7 即&)                    退出当前所有分屏，并关闭该会话
cb + 空格                                对当前所有pane进行重新布局
cb + z                                  最大化当前所在的pane,再按一次后恢复

cb + s              列出当前所有会话

[一行代码]
opt + 方向键左右键    单词间的跳转
ct + a/e           行头/行尾
ctrl + u           清除当前行
ct + d             删除光标所在位置的单词字母
ct + h             删除光标前一个字母
ct + w             删除光标前的单词
ct + k             删除光标至行末
```

**iterm2:**

```
[分屏]
cmd(下称cm) + d                         垂直分屏
cm + sh + d                            水平分屏
(cm + [ / ]) or (cm + opt + 方向键)     分屏切换

[快照]
cm + sh + s                            保存当前快照
cm + opt + b                           回放快照

[一行]
opt + 方向键左右键                        单词间的跳转
ct + a/e                               行头/行尾
ctrl + u                               清除当前行
ct + d                                 删除光标所在位置的单词字母
ct + h                                 删除光标前一个字母
ct + w                                 删除光标前的单词
ct + k                                 删除光标至行末


[标签]
cm + t                       新建标签
cm + w                       关闭标签
cm + 数字／数字键左右键          切换标签

cm + ;                       查看历史命令
cm + sh + h                  剪切版历史
ct + p                       上一条命令

cm + .                       iterm快速出现或消失
cm + Enter                   全屏／当前屏幕大小切换

cm + f                       查找
cm + e + r; cm + r; ct + l   清屏

鼠标双击，智能选择整个单词

[字体]
preferences-profiles-Text-change Font-
size 14; Horizontal 100%；Vertical 100-150%中间

[背景半透明]：
profiles-window-Transparency、Blur
半透明开关快捷键：cm + u

```

**其他推荐的链接:**

<https://www.cnblogs.com/piperck/p/4992159.html>
<https://xiaozhou.net/learn-the-command-line-tmux-2018-04-27.html>