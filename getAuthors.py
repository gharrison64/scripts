#! /usr/bin/env python3

import os,re,sys,tempfile,fileinput
from collections import OrderedDict

#file   = "repositories.txt"
file   = "repo.txt"
svnurl = "https://svn.alldata.com/svn/"
svnco  = "svn co "
infoFile = "/tmp/infoFile.txt"
authors_file = "/home/hudson/myauthors.txt"
authors =[]

def getListOfRepositories(file_in):
    file = open(file_in,"r")
    return  file.readlines()

def getInfo(url_in):
    cmd    =  "/usr/bin/svn log -q " + url_in + " >> " + infoFile
    return cmd

def getAuthors(infoFile_in):
    file_ = open(infoFile_in,"r")
    for line in file_:
         line = re.sub('-','',line)
         line_ = re.match("r\d+\s+\|\s+(\w+).*",line)
         if line_:
              author =  line_.group(1)
              authors.append(author)
    return authors


def main():
    list_repos = getListOfRepositories(file)
    for i in range(len(list_repos)): 
         repoFull = svnco + svnurl + list_repos[i]
         url = svnurl + list_repos[i]
         url = url.strip('\n')
         command = getInfo(url)
         print(command)
         os.system(command)
    authors_out = getAuthors(infoFile)
    authors = list(dict.fromkeys(authors_out))
    authors.sort()
    fh = open(authors_file,"w")
    for author_ in (authors):
         print (type(author_))
         fh.write(author_ + " = <" + author_.lower() + "@alldata.com>" + '\n')
    fh.close()
          
    print(authors)


main()
