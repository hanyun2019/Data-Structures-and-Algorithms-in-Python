Data Structures and Algorithms in Python

$ pwd
/Users/algorithms/python/dsa
Start Jupyter: $ jupyter notebook

Local directory: /Users/Algorithms/python/dsa
Github: https://github.com/hanyun2019/Data-Structures-and-Algorithms-in-Python.git

Steps：
1. git init //初始化仓库

2. git add .(文件name) //添加文件到本地仓库

3. git commit -m "first commit" //添加文件描述信息

4. git remote add origin + 远程仓库地址 //链接远程仓库，创建主分支

5. git pull origin master // 把本地仓库的变化连接到远程仓库主分支

6. git push -u origin master //把本地仓库的文件推送到远程仓库


使用强制push的方法：
$ git push -u origin master -f


Push an existing repository from the command line

$ git remote add origin https://github.com/hanyun2019/Data-Structures-and-Algorithms-in-Python.git

$ git add .

$ git commit -m "update for git commit test"

$ git push origin master
