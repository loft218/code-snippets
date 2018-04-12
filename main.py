'''
主函数
'''
import sys
import getopt
import time

from threading import Thread

import task_order
import task_money


def usage():
    '''
    帮助
    '''
    print('订单、销售、演出收入汇总统计')
    print('useage: python3 main.py [option]')
    print('Options and arguments:')
    print('-s, --start_date    :', '开始日期，格式：“YYYY-MM-DD”，默认为昨天')
    print('-e, --end_date      :', '结束日期，格式：“YYYY-MM-DD”，默认为今天')
    print('-d, --days          :',
          '开始日期跨度，默认为1；开始日期默认为昨天，如果设置该值，则默认日期为当前日期-{d}天')
    print('--only              :', '仅执行指定的任务，"task_order"或"task_money"')
    print('-h, --help          :', '查看帮助')


def main():
    '''
    主函数
    '''
    opts, args = getopt.getopt(sys.argv[1:], 'hs:e:d:', [
        "start_date=", "end_date=", "only=", "days=", 'help'
    ])
    diff_days = 1
    date_start = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    date_end = None
    only = None
    for op, value in opts:
        if op == "-s" or op == '--start_date':
            date_start = value
        elif op == "-e" or op == '--end_date':
            date_end = value
        if op == "-d" or op == '--days':
            diff_days = int(value)
        elif op == '--only':
            only = value
        elif op == "-h" or op == '--help':
            usage()
            sys.exit()

    date_format = "%Y-%m-%d"

    date_start = time.strftime(
        '%Y-%m-%d',
        time.localtime(
            int(time.mktime(time.strptime(date_start, date_format))) -
            86400 * diff_days))

    date_end = date_end or time.strftime(
        '%Y-%m-%d',
        time.localtime(
            int(time.mktime(time.strptime(date_start, date_format))) +
            86400 * diff_days))
    try:
        tm_start = int(time.mktime(time.strptime(date_start, date_format)))
        tm_end = int(time.mktime(time.strptime(date_end, date_format)))
    except:
        print('[错误]日期格式错误')
        sys.exit()
    if tm_end < tm_start:
        print('[错误]结束日期不得小于开始日期')
        sys.exit()
    while tm_end >= tm_start:
        _day = time.strftime('%Y-%m-%d', time.localtime(tm_start))
        print('>>> Task %s 正在执行' % _day)

        threads = []
        if not only or only == 'task_order':
            t1 = Thread(target=task_order.run, args=[_day])
            t1.setDaemon(True)
            t1.start()
            threads.append(t1)
        if not only or only == 'task_money':
            t2 = Thread(target=task_money.run, args=[_day])
            t2.setDaemon(True)
            t2.start()
            threads.append(t2)

        for t in threads:
            t.join()

        print('>>> Task %s 执行完成' % _day)
        tm_start = tm_start + 86400


if __name__ == '__main__':
    main()
