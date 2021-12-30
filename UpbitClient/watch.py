import client
import schedule
import time

def watch():
    

if __name__ == "__main__":
    schedule.every(1).seconds.do(watch)

    while True:
        schedule.run_pending()
        time.sleep(1)
