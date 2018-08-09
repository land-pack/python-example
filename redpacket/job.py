from apscheduler.schedulers.background import BlockingScheduler
from project.jobs.redpacket import rollback_unspent_redpacket


if __name__ == '__main__':
    scheduler = BlockingScheduler(timezone='MST')
    scheduler.configure()
    scheduler.add_job(rollback_unspent_redpacket, 'interval', seconds=3)
    scheduler.start()
