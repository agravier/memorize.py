from memorize.memorize import Memorize
import time


@Memorize(check_cache_safety=True)
def test_memorize(x, y=1):
    print('invoked original test_memorize!')
    time.sleep(1)
    if x == 3:
        raise Exception()
    return x, y


if __name__ == '__main__':
    try:
        for x in range(4):
            print(test_memorize(x))
        print('You should not see this')
    except:
        print('Exception expected for x==3')
    try:
        for x in range(4):
            print(test_memorize(x))
        print('You should not see this')
    except:
        print('Exception expected for x==3')
    try:
        for x in range(4):
            print(test_memorize(x, y=2))
        print('You should not see this')
    except:
        print('Exception expected for x==3')
    try:
        for x in range(4):
            print(test_memorize(x, y=2))
        print('You should not see this')
    except:
        print('Exception expected for x==3')
