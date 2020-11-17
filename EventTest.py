# import sys
# from datetime import datetime
# from threading import *
# sys.path.append('D:\\works\\TestFile')
# print(sys.path)
from EventManager import *

# 事件名称  新文章
EVENT_ARTICLE = "Event_Article"


# 事件源 公众号
class PublicAccounts:
    def __init__(self, event_manager):
        self.__eventManager = event_manager

    def write_new_article(self):
        # 事件对象，写了新文章
        event = Event(type_=EVENT_ARTICLE)
        event.dict["article"] = u'如何写出更优雅的代码\n'

        # 发送事件
        self.__eventManager.send_event(event)
        print(u'公众号发送新文章\n')


# 监听器 订阅者
class Listener:
    def __init__(self, username):
        self.__username = username

    # 监听器的处理函数 读文章
    def read_article(self, event):
        print(u'%s 收到新文章' % self.__username)
        print(u'正在阅读新文章内容：%s' % event.dict["article"])


def test():
    # 实例化监听器
    listener1 = Listener("JK")
    listener2 = Listener("CY")
    # 实例化事件操作函数
    event_manager = EventManager()

    # 绑定事件和监听器响应函数(新文章)
    event_manager.add_event_listener(EVENT_ARTICLE, listener1.read_article)
    event_manager.add_event_listener(EVENT_ARTICLE, listener2.read_article)
    # 启动事件管理器,# 启动事件处理线程
    event_manager.start()

    public_acc = PublicAccounts(event_manager)
    timer = Timer(2, public_acc.write_new_article)
    timer.start()


if __name__ == '__main__':
    test()
