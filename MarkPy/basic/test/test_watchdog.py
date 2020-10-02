from MarkPy.basic import WatchFile, WatchFolder


def test_watch_folder():
    wdir = WatchFolder('/tmp')
    print(wdir)

test_watch_folder()