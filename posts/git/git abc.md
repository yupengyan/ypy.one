---
date: 2019-02-22 
category: Server
---

# Using Git in a team

## 前期准备
1. Git windows 客户端安装

## 管理者
1. 新建一个develop分支（from master）http://172.19.13.51:8929/
2. 为合作者新建一个合作者分支，如cjj

合作者在合作者分支上面修改代码，合并到develop，然后提交到Git服务器。

## 合作者
```
Git global setup
git config --global user.name "yupengyan"
git config --global user.email "ypy@example.com"
```

Create a new repository
```
git clone git@gitlab.library.gdufe.edu.cn:pengyan/ve3_smartkits.git
cd ve3_smartkits
touch README.md
git add README.md
git commit -m "add README"
git push -u origin master
```

Existing folder
```
cd existing_folder
git init
git remote add origin git@gitlab.library.gdufe.edu.cn:pengyan/ve3_smartkits.git
git add .
git commit -m "Initial commit"
git push -u origin master
```

Existing Git repository
```
cd existing_repo
git remote rename origin old-origin
git remote add origin git@gitlab.library.gdufe.edu.cn:pengyan/ve3_smartkits.git
git push -u origin --all
git push -u origin --tags
```

以项目 http://172.19.13.51:8929/pengyan/dl_documents 合作为例：
1. 安装Git   
2. Git global setup     
```
git config --global user.name "py"
git config --global user.email "ypy@gdufe.edu.cn"
```

对于需要用Key认证的，先配置。In ~/.ssh/config, add: (如果不是默认22，指定Port很重要)(windows in C:\Users\xxx\.git)

```
host gitlab.library.gdufe.edu.cn
  HostName 172.19.13.51
  Port 2289
  IdentityFile  E:/OneDrive/privates/#keys/Identity-gitlib-openssh
  User pengyan
host git-2
  HostName 172.19.13.51
  Port 2289
  IdentityFile  E:/OneDrive/privates/#keys/Identity-gitlib-openssh
  User pengyan
```

测试下：ssh -T git@github.com  看看有没有出错


 OpenSSL SSL_read: SSL_ERROR_SYSCALL, errno 10054
2012-3-5 以上方法都不管事
```shell
pengyan@tsg-d-py MINGW64 /g/private src data/# private academic (master)
$ eval $(ssh-agent -s)
Agent pid 1045

pengyan@tsg-d-py MINGW64 /g/private src data/# private academic (master)
$ ssh-add ~/.ssh/openssh_key_ras_github_2048
Enter passphrase for /c/Users/pengyan/.ssh/openssh_key_ras_github_2048:
Identity added: /c/Users/pengyan/.ssh/openssh_key_ras_github_2048 (/c/Users/pengyan/.ssh/openssh_key_ras_github_2048)

pengyan@tsg-d-py MINGW64 /g/private src data/# private academic (master)
$ git push origin master --force
fatal: unable to access 'https://github.com/XXX/XXX.git/': OpenSSL SSL_read: SSL_ERROR_SYSCALL, errno 10054

pengyan@tsg-d-py MINGW64 /g/private src data/# private academic (master)
git config --global --unset http.proxy 
git config --global --unset https.proxy

git config http.sslVerify "false"

git config https.sslVerify "true"

### 服气，ssl 可以，但git 就不行
pengyan@tsg-d-py MINGW64 /g/private src data/# private academic (master)
$ git push origin master --force
fatal: unable to access 'https://github.com/yupengyan/private-academic.git/': OpenSSL SSL_read: SSL_ERROR_SYSCALL, errno 10054

pengyan@tsg-d-py MINGW64 /g/private src data/# private academic (master)
$ ssh -T git@github.com
Hi yupengyan! You've successfully authenticated, but GitHub does not provide shell access.

## 换个证书试试
ssh-keygen -t rsa -C "pengyan.tech@gmail.com"
eval $(ssh-agent -s)
ssh-add ~/.ssh/id_rsa

## 更新客户端
git update-git-for-windows
```
参考：https://www.codenong.com/26266778/

（）

3.  Create a new repository    
```
cd my_work_place
git clone git@gitlab.library.gdufe.edu.cn:pengyan/dl_documents.git
cd dl_documents
```

## 常用操作
1. 查看有什么分支    
```
git branch
```

2. 这个命令的意思就是拉取远程的一个叫develop的分支，并在本地创建一个叫develop的分支和远程的分支匹配。    
```
git fetch origin develop:develop
```

3. 拉取自己的分支    
```
git fetch origin xzl:xzl
```

4. 每个人的所有开发工作都只在自己的分支开发。例如小谢开发，你就在本地切换到自己的xzl分支然后进行开发。   
```
git checkout xzl
```

5. 每个人只允许在自己的分支直接push远程分支。    
```
touch README.md
git add README.md
git commit -m "add README"
git push -u origin xzl
```

## 合并的时候必须遵循以下条件 
a) 首先，本地切换到develop分支    
```
git checkout develop
```

b) pull develop分支最新内容到本地      
```
git pull origin develop   
```

c) 保证develop最新前提下合并自己的分支xzl   
```
git merge xzl
```

d) 如果出现conflict那么清除conflict之后，commit.然后把本地develop push 到远程的develop.每完成一个功能就提交一次。不要累计代码。    
```
git add README.md
git commit -m "add README"
git merge xzl
git push -u origin develop
```

## 概念辨析
fork：在github页面，点击fork按钮。将别人的仓库复制一份到自己的仓库。   
clone：将github中的仓库克隆到自己本地电脑中

(1) pull request的作用   
比如在仓库的主人（A）没有把我们添加为项目合作者的前提下，我们将A的某个仓库名为“a”的仓库clone到自己的电脑中，在自己的电脑进行修改，但是我们会发现我们没办法通过push将代码贡献到B中。

所以要想将你的代码贡献到B中，我们应该：   
在A的仓库中fork项目a （此时我们自己的github就有一个一模一样的仓库a，但是URL不同）;将我们修改的代码push到自己github中的仓库B中pull request ，主人就会收到请求，并决定要不要接受你的代码;也可以可以申请为项目a的contributor，这样可以直接push   

(2) fork了别人的项目到自己的repository之后，别人的项目更新了，我们fork的项目怎么更新？   
答：首先fetch网上的更新到自己的项目上，然后再判断、merge。这里就涉及了下一个问题，pull和fetch有啥区别。   

（3）fetch+merge与pull效果一样。但是要多用fetch+merge，这样可以检查fetch下来的更新是否合适。pull直接包含了这两步操作，如果你觉得网上的更新没有问题，那直接pull也是可以的。

# 更换远程git仓库地址
git remote remove origin
git remote add origin https://gitee.com/gdufe/Annual_data.git



## 管理员
git pull origin cyc:cyc
git merge cyc

git pull origin



# 大文件
git lfs install
git lfs track "*.7z"
git add .gitattributes

git add *.7z
git commit -m "Add large file"
git push origin master 