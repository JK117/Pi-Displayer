from em.EventManager import *

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


def start_event():
    public_acc = PublicAccounts(event_manager)
    timer = Timer(2, public_acc.write_new_article)
    timer.start()