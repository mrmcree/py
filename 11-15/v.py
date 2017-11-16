import os,sys,stat
import time


def v(url):
  if not os.path.exists(url):
    print('文件不存在')
    return
  from bs4 import BeautifulSoup
  nowTime = lambda: int(round(time.time() * 1000))
  f = open(url, 'r+', encoding='UTF-8')
  html = BeautifulSoup(f.read(), 'html.parser')
  script = html.select('script')
  for i in script:
    if 'src' in i.attrs:
      i.attrs['src'] = i.attrs['src'].split('?')[0] + '?v=' + str(nowTime())[-5:]
  link = html.select('link')
  for i in link:
    if 'href' in i.attrs:
      i.attrs['href'] = i.attrs['href'].split('?')[0] + '?v=' + str(nowTime())[-5:]
  f.close()
  os.remove(url)
  newFile = url
  try:
    f = open(url, 'w+', encoding='UTF-8')
    f.write(str(html))
  except IOError:
    print("Error: 没有找到文件或读取文件失败")
  else:
    print("%s内容写入文件成功" % url)
    f.close()
