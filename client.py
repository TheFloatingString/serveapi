"""
Client program
"""

from serveapi import interface as itfc

if __name__ == '__main__':
    print('client')
    np = itfc.ServeApi2('np')
    print('client')
    resp = np.linalg.norm([100,200,300])
    print(resp)
