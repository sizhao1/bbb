import random

class XiuXian:
    def __init__(self):
        self.xiuwei = 0 # 当前修为
        self.jingjie = 0 # 当前境界
        self.need_xiuwei = 10 # 升级所需修为
        self.need_jingjie = [10, 20, 30, 50] # 升级所需境界

    def xiuLian(self):
        # 随机获取修炼增加的修为值
        xiuwei_inc = random.randint(1, 5)
        print(f"你进行修炼，增加了 {xiuwei_inc} 点修为")
        self.xiuwei += xiuwei_inc

        # 判断是否升级境界
        if self.xiuwei >= self.need_xiuwei:
            self.jingjie += 1
            self.need_xiuwei += 10
            print(f"恭喜你晋升到了 {self.getJingJieName()}")

    def getJingJieName(self):
        if self.jingjie == 0:
            return "凡人"
        elif self.jingjie == 1:
            return "修行者"
        elif self.jingjie == 2:
            return "筑基者"
        elif self.jingjie == 3:
            return "金丹者"
        elif self.jingjie == 4:
            return "元婴者"
        else:
            return "无敌仙神"

    def play(self):
        print("欢迎来到修仙世界！")
        print("你现在是一名凡人，开始修炼吧！")
        while True:
            print(f"当前修为：{self.xiuwei}，当前境界：{self.getJingJieName()}")

            # 判断是否达到最高境界
            if self.jingjie == 5:
                print("你已成为无敌仙神，修仙之路已经结束了！")
                break

            # 打印菜单
            print("请选择你的操作：")
            print("1. 修炼")
            print("2. 退出游戏")
            choice = input()

            # 处理用户选择
            if choice == "1":
                self.xiuLian()
            elif choice == "2":
                print("谢谢游玩，再见！")
                break
            else:
                print("无效的选择，请重新输入")

# 运行游戏
xiuxian = XiuXian()
xiuxian.play()