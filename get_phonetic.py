from multiprocessing import Pool
import re
import urllib.request as req

def search(e,url):
    r = req.Request(url + e)
    s = req.urlopen(r)
    page = s.read().decode('utf-8')
    # print(page)
    try:
        v = re.search('>美\s+<span class="phonetic">([\S\W\]]+?)<', page)
        # print(e + "\t" + v.group(1))
        return v.group(1)

    except(AttributeError):
        print("检查单词拼写" + e)

def get_ph(words):
    url = 'http://dict.youdao.com/w/eng/'
    p = Pool(20)
    res = p.apply_async(search, args=(words,url))
    return res.get()