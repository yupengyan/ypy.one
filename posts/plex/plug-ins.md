---
blogpost: true
date: March 2, 2022
author: yu pengyan
tags: plex,plug-ins,nas,qnap
category: Tech
language: Chinese
---
# Plex Server 安装插件

## 推荐安装的插件
https://github.com/ukdtom/WebTools.bundle/wiki/Install
https://github.com/gboudreau/XBMCnfoMoviesImporter.bundle

## 通用手工安装方法
1. 下载目标插件，解压
2. 将文件夹命名为XXX.bundle
3. 将文件夹放到PLEX Server Plug-ins目录下
4. 设置文件夹所有者为plex server
5. 重启plex server

## XBMCnfoMoviesImporter.bundle
注意事项：
> 1.XBMCnfoMoviesImporter.bundle 不会出现在插件里面，媒体库代理里面安装成功后直接能用  
> 2.XBMCnfoMoviesImporter.bundle 安装后，能识别nfo里面的元数据

## 元素搜刮器

https://github.com/yoshiko2/Movie_Data_Capture

## 其他信息
### QNAP Plex plug-ins 目录
```txt
/share/CACHEDEV2_DATA/.qpkg/PlexMediaServer/Library/Plex Media Server/Plug-ins
```
可以用SecureFXP SSH(admin)登陆，然后将数据上传。

