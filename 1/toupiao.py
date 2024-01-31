class VotingSystem:
    def __init__(self, total_people):
        self.total_people = total_people
        self.agree = 0
        self.disagree = 0
        self.abstain = 0

    def vote(self, choice):
        if choice == "同意":
            self.agree += 1
        elif choice == "不同意":
            self.disagree += 1
        elif choice == "弃权":
            self.abstain += 1
        else:
            print("无效的选项，请重新输入。")

    def get_result(self):
        print(f"同意：{self.agree}")
        print(f"不同意：{self.disagree}")
        print(f"弃权：{self.abstain}")

if __name__ == "__main__":
    total_people = int(input("请输入总人数："))
    voting_system = VotingSystem(total_people)
    for i in range(total_people):
        choice = input("请输入您的选择（同意/不同意/弃权）：")
        voting_system.vote(choice)
    voting_system.get_result()
