# coding=utf-8
import urllib
import urllib2


def loadPage(url, filename):
    """

    :param url: 需要爬取的url地址
    :param filename: 保存的文件名
    :return:爬取的html页面
    """
    print '正在下载' + filename
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Referer": "http: // tieba.baidu.com / f?"
    }
    request = urllib2.Request(url, headers=headers)
    return urllib2.urlopen(request).read()


def writePage(html, filename):
    """

    :param html:服务器相应文件内容
    :return:
    """
    print '正在保存' + filename
    with open(unicode(filename, 'utf-8'), "w") as f:
        f.write(html)
    print '-=-' * 30


def tiebaSpider(url, beginPage, endPage, kw):
    """

    :param url: 贴吧地址
    :param beginPage: 起始页
    :param endPage: 结束页
    :return:
    """
    for page in range(beginPage, endPage + 1):
        pn = (page - 1) * 50
        filename = kw + '吧 第' + str(page) + '页.html'
        fullurl = url + '&pn=' + str(pn)

        print fullurl
        html = loadPage(fullurl, filename)
        writePage(html, filename)


if __name__ == '__main__':
    kw = raw_input('请输入要爬取的贴吧名')
    beginPage = int(raw_input('请输入起始页'))
    endPage = int(raw_input('请输入结束页'))

    url = 'http://tieba.com/f?'
    key = urllib.urlencode({'kw': kw})
    fullurl = url + key
    tiebaSpider(fullurl, beginPage, endPage, kw)
