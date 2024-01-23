import datetime

def record_sign_in(name):
    # 获取当前日期和时间
    now = datetime.datetime.now()
    # 格式化日期和时间
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return f"{name} has signed in at {date_time}"

def main():
    name = input("Please enter your name: ")
    print(record_sign_in(name))

if __name__ == "__main__":
    main()
