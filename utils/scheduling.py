import schedule
from time import sleep
from threading import Thread

from tools.config import Config


class Scheduler:
    def __init__(self, config: Config):
        self._config = config
        self._thread = None
        self._running = False
        self._scheduler = schedule.Scheduler()

    def _run(self):
        if not self._config.get_bool("DEBUG") and self._config.get_int("SCHEDULER_STARTUP_DELAY") > 0:
            sleep(self._config.get_int("SCHEDULER_STARTUP_DELAY"))

        while self._running:
            self._scheduler.run_pending()
            sleep(1)

    def start(self):
        if self._running:
            return

        self._running = True
        self._thread = Thread(target=self._run, daemon=True)
        self._thread.start()

    def stop(self):
        self._running = False

    @property
    def schedule(self):
        return self._scheduler
