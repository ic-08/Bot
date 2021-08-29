#Used for testing, will most likely be deleted in the release version

def foo(pos=None, *, forcenamed):
    print(pos, forcenamed)

foo(1, forcenamed=2)