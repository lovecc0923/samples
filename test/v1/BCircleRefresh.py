# -*- coding: UTF-8 -*-
'''
Created on 2014年7月25日

@author: luorc
'''

import redis, logging

# formatter = logging.Formatter('%(asctime)s %(name)s -%(levelname)s -%(message)s')
formatter = logging.Formatter('[%(asctime)s %(levelname)s] %(message)s')

fh = logging.FileHandler('log.log')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)

logger = logging.getLogger('b.circle.refresh')
logger.setLevel(logging.DEBUG)
logger.addHandler(fh)
logger.addHandler(ch)

if __name__ == '__main__':
    logger.info('榜单刷新开始')
    try:
        res = redis.Redis(host='121.37.30.15', port=6380, db=0)
        end = res.zcard("msg.hot.list")
        for member in res.zrange("msg.hot.list", 0, end, True):
            print '%s\t%s' % (member , res.zscore("msg.hot.list", member))
    except Exception, e:
        logger.info('榜单刷新失败')
        logger.exception(e)
    finally:
        logger.info('榜单刷新结束')
   
