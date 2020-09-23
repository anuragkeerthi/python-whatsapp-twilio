from apscheduler.schedulers.blocking import BlockingScheduler
from source import send_message

sched = BlockingScheduler()

sched.add_job(send_message, 'interval', seconds=30)

sched.start()