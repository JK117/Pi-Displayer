from em.EventManager import *

# 事件名称  新显示内容
EVENT_DISPLAY_CONTENT = "Event_Display_Content"


# 事件源 显示内容
class DisplayContent:
    def __init__(self, event_manager):
        self.__eventManager = event_manager

    def generate_new_content(self):
        pass


# 监听器 屏幕
class OLEDDisplay:
    def __init__(self):
        pass

    # 监听器处理函数 显示内容
    def display_content(self):
        pass


def test():
    # 实例化监听器
    listener = OLEDDisplay()

    # 实例化事件操作函数
    event_manager = EventManager()

    # 绑定事件和监听器响应函数(新文章)
    event_manager.add_event_listener(EVENT_DISPLAY_CONTENT, listener.display_content)

    # 启动事件管理器,# 启动事件处理线程
    event_manager.start()

    oled_display = DisplayContent(event_manager)
    timer = Timer(2, oled_display.generate_new_content)
    timer.start()


if __name__ == '__main__':
    test()
