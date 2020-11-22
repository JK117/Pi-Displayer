from queue import Queue, Empty
from threading import *


class EventManager:
    def __init__(self):
        """初始化事件管理器"""
        # 事件对象列表
        self.__eventQueue = Queue()
        # 事件管理器开关
        self.__active = False
        # 事件处理线程
        self.__thread = Thread(target=self.run)
        self.__count = 0
        # 这里的__handlers是一个字典，用来保存对应的事件的响应函数
        # 其中每个键对应的值是一个列表，列表中保存了对该事件监听的响应函数，一对多
        self.__handlers = {}

    def run(self):
        """引擎运行"""
        print('{}_run'.format(self.__count))
        while self.__active:
            try:
                # 获取事件的阻塞时间设为1秒
                event = self.__eventQueue.get(block=True, timeout=1)
                self.event_process(event)
            except Empty:
                pass
            self.__count += 1

    def event_process(self, event):
        """处理事件"""
        print('{}_EventProcess'.format(self.__count))
        # 检查是否存在对该事件进行监听的处理函数
        if event.type_ in self.__handlers:
            # 若存在，则按顺序将事件传递给处理函数执行
            for handler in self.__handlers[event.type_]:
                handler(event)
        self.__count += 1

    def start(self):
        """启动"""
        print('{}_Start'.format(self.__count))
        # 将事件管理器设为启动
        self.__active = True
        # 启动事件处理线程
        self.__thread.start()
        self.__count += 1

    def stop(self):
        """停止"""
        print('{}_Stop'.format(self.__count))
        # 将事件管理器设为停止
        self.__active = False
        # 等待事件处理线程退出
        self.__thread.join()
        self.__count += 1

    def add_event_listener(self, type_, handler):
        """绑定事件和监听器处理函数"""
        print('{}_AddEventListener'.format(self.__count))
        # 尝试获取该事件类型对应的处理函数列表，若无则创建
        try:
            handler_list = self.__handlers[type_]
        except KeyError:
            handler_list = []
            self.__handlers[type_] = handler_list

        if handler not in handler_list:
            handler_list.append(handler)
        print(self.__handlers)
        self.__count += 1

    def remove_event_listener(self, type_, handler):
        """移除监听器的处理函数"""
        print('{}_RemoveEventListener'.format(self.__count))
        try:
            handler_list = self.__handlers[type_]
            # 如果该函数存在于列表中，则移除
            if handler in handler_list:
                handler_list.remove(handler)
            # 如果函数列表为空，则从引擎中移除该事件类型
            if not handler_list:
                del self.__handlers[type_]
        except KeyError:
            pass
        self.__count += 1

    def send_event(self, event):
        """发送事件，向事件队列中存入事件"""
        print('{}_SendEvent'.format(self.__count))
        self.__eventQueue.put(event)
        self.__count += 1


class Event:
    def __init__(self, type_=None):
        self.type_ = type_  # 事件类型
        self.dict = {}  # 字典用于保存具体的事件数据
