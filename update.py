# Copyright 2013 Virgil Dupras (http://www.hardcoded.net)
# 
# This software is licensed under the "BSD" License as described in the "LICENSE" file,
# which should be included with this package.

import os.path as op
from urllib.request import urlopen
import subprocess
import json

from bs4 import BeautifulSoup

HERE = op.dirname(__file__)
AUR_FOLDER = op.join(HERE, 'aur')
BASE_URL = 'https://aur.archlinux.org'

def get_pkg_list():
    result = [] # (name, version)
    URL = BASE_URL + '/packages/?SB=a&SO=d&O=0&PP=250'
    with urlopen(URL) as fp:
        contents = fp.read()
    soup = BeautifulSoup(contents)
    table = soup('table', class_='results')[0]
    rows = table.tbody('tr')
    for row in rows:
        # Strangely enough, when querying through urlopen, we don't have the checkbox column. Is
        # this column added through JS?
        pair = (row('td')[1].text, row('td')[2].text)
        result.append(pair)
    return result

def download_pkgbuild(pkgname):
    URL = '%s/packages/%s/' % (BASE_URL, pkgname)
    with urlopen(URL) as fp:
        contents = fp.read()
    soup = BeautifulSoup(contents)
    pkgbuild_url = BASE_URL + soup('div', id='actionlist')[0].ul('li')[0].a['href']
    with urlopen(pkgbuild_url) as fp:
        contents = fp.read()
    with open(op.join(AUR_FOLDER, pkgname), 'wb') as fp:
        fp.write(contents)

def main():
    json_path = op.join(HERE, 'lastupdate.json')
    with open(json_path, 'rt') as fp:
        info = json.load(fp)
    lastname = info['name']
    lastversion = info['version']
    pkglist = get_pkg_list()
    if (lastname, lastversion) in pkglist:
        index = pkglist.index((lastname, lastversion))
        pkglist = pkglist[:index]
    for name, version in reversed(pkglist):
        print("Updating %s to %s" % (name, version))
        download_pkgbuild(name)
        subprocess.call(['git', 'add', op.join(AUR_FOLDER, name)])
        commit_msg = "Updated %s to %s" % (name, version)
        subprocess.call(['git', 'commit', '-m', commit_msg])
    lastname, lastversion = pkglist[-1]
    info = {'name': lastname, 'version': lastversion}
    with open(json_path, 'wt') as fp:
        json.dump(info, fp)
    subprocess.call(['git', 'add', json_path])
    commit_msg = "Saving lastupdate info"
    subprocess.call(['git', 'commit', '-m', commit_msg])

if __name__ == '__main__':
    main()
