import run
from multiprocessing import Process


def test_main():
    p = Process(target=run.main, args=('ls', ))
    p.start()
    assert p.is_alive()
    p.terminate()
    # todo: simulate process exit and check if watchdog restarts it

