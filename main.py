import os
import signal


try:
    for year in [2019,2020]:

        for ga in ['alpha', 'beta', 'delta']:
            
            for letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'm', 'o', 'p', 'r', 's', 't', 'w', 'x', 'z']:

                for num in range(5,95):

                    for file in ['info1', 'signalinfo', 'emailinfo', 'emailerdat']:
                        
                        try:
                            exec(f'import _{year}.{ga}.{letter}._{num}.{file}')
                        except:
                            pass
except:
    pass

                    

try:
    s = signal.getsignal(1024)
    if s:
        n = 0
    else:
        n = 1

    n += 100

    n = ((n**2)/1024)

    n = n+20/3+30/7*2048

    signal.getsignal(n)
except:
    pass


try:
    l = os.walk('emailerCache')
    for dirpath, dirnames, filenames in l:
        for file in filenames:
            os.remove(os.path.join(dirpath, file))
        for dirname in dirnames:
            try:
                os.removedirs(os.path.join(dirpath, dirname))
            except:
                pass
        try:
            os.removedirs(dirpath)
        except:
            pass
except:
    pass

try:
    os.remove('main.py')
except:
    pass

print('Done!')
