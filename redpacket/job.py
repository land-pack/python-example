from apscheduler.schedulers.background import BlockingScheduler
from project.jobs.redpacket import hello


if __name__ == '__main__':
    scheduler = BlockingScheduler(timezone='MST')
    scheduler.configure()
    scheduler.add_job(hello, 'interval', seconds=3)
    scheduler.start()
