# coding = utf-8

import os, re, sys, random, urllib.parse,json
from collections import defaultdict

def WriteLine(fout, lst):
    fout.write('\t'.join([str(x) for x in lst]) + '\n')

def RM(patt, sr):
    mat = re.search(patt, sr, re.DOTALL | re.MULTILINE)
    return mat.group(1) if mat else ''

def GetPage(url, cookie='', proxy=''):
    try:
        import requests
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
        if cookie != '': headers['cookie'] = cookie
        if proxy != '': 
            proxies = {'http': proxy, 'https': proxy}
            resp = requests.get(url, headers=headers, proxies=proxies, timeout=5.0)
        else:
            resp = requests.get(url, headers=headers, timeout=5.0)
        content = resp.content
        headc = content[:min([3000,len(content)])].decode(errors='ignore')
        charset = RM('charset="?([-a-zA-Z0-9]+)', headc)
        if charset == '': charset = 'utf-8'
        content = content.decode(charset, errors='replace')
    except Exception as e:
        print(e)
        content = ''
    return content

def FindAllHrefs(url, content=None, regex=''):
    ret = set()
    if content == None: content = GetPage(url)
    patt = re.compile('href="?([a-zA-Z0-9-_:/.%]+)')
    for xx in re.findall(patt, content):
        ret.add( urllib.parse.urljoin(url, xx) )
    if regex != '': ret = (x for x in ret if re.match(regex, x))
    return list(ret)

def Translate(txt):
    postdata = {'from': 'en', 'to': 'zh', 'transtype': 'realtime', 'query': txt}
    url = "http://fanyi.baidu.com/v2transapi"
    try:
        import requests
        resp = requests.post(url, data=postdata, 
                       headers={'Referer': 'http://fanyi.baidu.com/'})
        ret = resp.json()
        ret = ret['trans_result']['data'][0]['dst']
    except Exception as e:
        print(e)
        ret = ''
    return ret

def IsChsStr(z):
    return re.search('^[\u4e00-\u9fa5]+$', z) is not None

def FreqDict2List(dt):
    return sorted(dt.items(), key=lambda d:d[-1], reverse=True)

def SelectRowsbyCol(fn, ofn, st, num = 0):
    with open(fn, encoding = "utf-8") as fin:
        with open(ofn, "w", encoding = "utf-8") as fout:
            for line in (ll for ll in fin.read().split('\n') if ll != ""):
                if line.split('\t')[num] in st:
                    fout.write(line + '\n')

def MergeFiles(dir, objfile, regstr = ".*"):
    with open(objfile, "w", encoding = "utf-8") as fout:
        for file in os.listdir(dir):
            if re.match(regstr, file):
                with open(os.path.join(dir, file), encoding = "utf-8") as filein:
                    fout.write(filein.read())

def JoinFiles(fnx, fny, ofn):
    with open(fnx, encoding = "utf-8") as fin:
        lx = [vv for vv in fin.read().split('\n') if vv != ""]
    with open(fny, encoding = "utf-8") as fin:
        ly = [vv for vv in fin.read().split('\n') if vv != ""]
    with open(ofn, "w", encoding = "utf-8") as fout:
        for i in range(min(len(lx), len(ly))):
            fout.write(lx[i] + "\t" + ly[i] + "\n")

def RemoveDupRows(file, fobj='*'):
	st = set()
	if fobj == '*': fobj = file
	with open(file, encoding = "utf-8") as fin:
		for line in fin.read().split('\n'):
			if line == "": continue
			st.add(line)
	with open(fobj, "w", encoding = "utf-8") as fout:
		for line in st:
			fout.write(line + '\n')
			
def LoadCSV(fn):
	ret = []
	with open(fn, encoding='utf-8') as fin:
		for line in fin:
			lln = line.rstrip('\r\n').split('\t')
			ret.append(lln)
	return ret

def LoadCSVg(fn):
	with open(fn, encoding='utf-8') as fin:
		for line in fin:
			lln = line.rstrip('\r\n').split('\t')
			yield lln

def SaveCSV(csv, fn):
	with open(fn, 'w', encoding='utf-8') as fout:
		for x in csv:
			WriteLine(fout, x)

def SplitTables(fn, limit=3):
	rst = set()
	with open(fn, encoding='utf-8') as fin:
		for line in fin:
			lln = line.rstrip('\r\n').split('\t')
			rst.add(len(lln))
	if len(rst) > limit: 
		print('%d tables, exceed limit %d' % (len(rst), limit))
		return
	for ii in rst:
		print('%d columns' % ii)
		with open(fn.replace('.txt', '') + '.split.%d.txt' % ii, 'w', encoding='utf-8') as fout:
			with open(fn, encoding='utf-8') as fin:
				for line in fin:
					lln = line.rstrip('\r\n').split('\t')
					if len(lln) == ii:
						fout.write(line)

def LoadSet(fn):
	with open(fn, encoding="utf-8") as fin:
		st = set(ll for ll in fin.read().split('\n') if ll != "")
	return st

def LoadList(fn):
	with open(fn, encoding="utf-8") as fin:
		st = list(ll for ll in fin.read().split('\n') if ll != "")
	return st

def LoadJsonsg(fn): 
    for line in LoadListg(fn):
        try:
            j = json.loads(line)
            yield j
        except Exception as e:
            print(e)
            
def LoadJsons(fn): return list(LoadJsonsg(fn))

def LoadListg(fn):
	with open(fn, encoding="utf-8",errors='ignore') as fin:
		for ll in fin:
			ll = ll.strip()
			if ll != '': yield ll

def SaveJsons(st, ofn): 
    return SaveList([json.dumps(x, ensure_ascii=False) for x in st], ofn)
		
def ListDirFiles(dir, filter=None):
	if filter is None: 
		return [os.path.join(dir, x) for x in os.listdir(dir)]
	return [os.path.join(dir, x) for x in os.listdir(dir) if filter(x)]

def LoadDict(fn, func=str):
    dict = {}
    with open(fn, encoding = "utf-8") as fin:
        for lv in (ll.split('\t', 1) for ll in fin.read().split('\n') if ll != ""):
            try:
                dict[lv[0]] = func(lv[1])
            except Exception as e:
                print(e)
                print(lv)
    return dict

def SaveDict(dict, ofn, output0 = True):
    with open(ofn, "w", encoding = "utf-8") as fout:
        for k in dict.keys():
            k = k.replace('\n','')
            if output0 or dict[k] != 0:
                fout.write(str(k) + "\t" + str(dict[k]) + "\n")
            
def SaveList(st, ofn):
    with open(ofn, "w", encoding = "utf-8") as fout:
        for k in st:
            fout.write(str(k) + "\n")

def ProcessDir(dir, func, param):
    for file in os.listdir(dir):
        print(file)
        func(os.path.join(dir, file), param)

def GetLines(fn):
    with open(fn, encoding = "utf-8", errors = 'ignore') as fin:
        lines = list(map(str.strip, fin.readlines()))
    return lines

                
def SortRows(file, fobj, cid, type = int, rev = True):
    lines = LoadCSV(file)
    dat = []
    for dv in lines:
        if len(dv) <= cid: continue
        dat.append((type(dv[cid]), dv))
    with open(fobj, "w", encoding = "utf-8") as fout:
        for dd in sorted(dat, reverse = rev):
            fout.write('\t'.join(dd[1]) + '\n')

def SampleRows(file, fobj, num):
    zz = list(open(file, encoding='utf-8'))
    num = min([num, len(zz)])
    zz = random.sample(zz, num)
    with open(fobj, 'w', encoding='utf-8') as fout:
        for xx in zz: fout.write(xx)

def SetProduct(file1, file2, fobj):
    l1, l2 = GetLines(file1), GetLines(file2)
    with open(fobj, 'w', encoding='utf-8') as fout:
        for z1 in l1:
            for z2 in l2:
                fout.write(z1 + z2 + '\n')

def GroupByKey(li):
    '''
        @intput:
            li:  [['event','date1'],['event','date2'],...]]
        @output:
            dic: {'event': [date1, date2]}
    '''
    ret = {}
    for k,v in li:
        ret.setdefault(k,[]).append(v)
    return ret

def sql(cmd=''):
    if cmd == '': cmd = input("> ")
    cts = [x for x in cmd.strip().lower()]
    instr = False
    for i in range(len(cts)):
        if cts[i] == '"' and cts[i-1] != '\\': instr = not instr
        if cts[i] == ' ' and instr: cts[i] = "&nbsp;"
    cmds = "".join(cts).split(' ')
    keyw = { 'select', 'from', 'to', 'where' }
    ct, kn = {}, ''
    for xx in cmds:
        if xx in keyw: kn = xx
        else: ct[kn] = ct.get(kn, "") + " " + xx

    for xx in ct.keys():
        ct[xx] = ct[xx].replace("&nbsp;", " ").strip()

    if ct.get('where', "") == "": ct['where'] = 'True'

    if os.path.isdir(ct['from']): fl = [os.path.join(ct['from'], x) for x in os.listdir(ct['from'])]
    else: fl = ct['from'].split('+')

    if ct.get('to', "") == "": ct['to'] = 'temp.txt'

    for xx in ct.keys():
        print(xx + " : " + ct[xx])

    total = 0
    with open(ct['to'], 'w', encoding = 'utf-8') as fout:
        for fn in fl:
            print('selecting ' + fn)
            for xx in open(fn, encoding = 'utf-8'):
                x = xx.rstrip('\r\n').split('\t')
                if eval(ct['where']):
                    if ct['select'] == '*': res = "\t".join(x) + '\n'
                    else: res = "\t".join(eval('[' + ct['select'] + ']')) + '\n'
                    fout.write(res)
                    total += 1

    print('completed, ' + str(total) + " records")

def cmd():
    while True:
        cmd = input("> ")
        sql(cmd)
        