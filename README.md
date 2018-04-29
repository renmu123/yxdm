# 用处
这是一个订阅每天更新的番剧的小东西，里面的数据来源皆来自[怡萱动漫](www.yxdm.tv)

# 使用

## 一般使用
修改config.py的设置，开始使用，暂时支持qq邮箱，想要支持别的邮箱的自行修改mail.py的17,18行

修改user.txt增加订阅人邮箱

需要安装requests和bs4

## 服务器使用
在Linux服务器上使用定时脚本，即可实现每天固定时间推送。

    crontab -e
    # 例子
    10 0 * * * python3 /root/yxdm/run.py

如果懒得弄，可以在issues中留言

# TODO
增加数据库查询（懒）
制作成api（懒）
