"""
Client program
"""

import requests
import interface as itfc

if __name__ == '__main__':
    np = itfc.ServeApi2('np')
    resp = np.linalg.norm([100,200,300])
    print(resp)
