import webbrowser
import time

class TakeaBreak(object):
    def __init__(self):
      self.url = "https://www.youtube.com/watch?v=M4ZoCHID9GI"
      self.set_timer = 10

    def break_time(self):
        for x in range(1,2):
            time.sleep(self.set_timer)
            webbrowser.open(self.url)
            print("The loop ran{}".format(x))

if __name__ == '__main__':
    takeabreak = TakeaBreak()
    takeabreak.break_time()