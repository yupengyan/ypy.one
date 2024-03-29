----
blogpost: true
Title: github pages
date: April 26, 2022
category: Tech
Tags: github pages
----


# Github pages 


## Set up a Custom domain    
1. DNS: Add an A record point to github server.    

```text
185.199.108.153
185.199.109.153
185.199.110.153
185.199.111.153
```
![gh-pages-dns-records](gh-pages-dns-records.jpg)

2. Go to your repo setting.      
    1. Rename your repositry name to :example.com   
![gh-pages-repo-name](gh-pages-settings.png)
    2. Setting -> Github pages -> Custom domain -> example.com    
![gh-pages-custom-domain](gh-pages-custom-domain.jpg)
  
3. Add a CNAME file in your repositry.    
```text
examle.com
```
![gh-pages-CNAME](gh-pages-CNAME.jpg)


That's it!

## 利用Github action （2022.4.16 更新）
1. 源代码放main分支
2. html代码放gh-page分支


## FAQ:
Q: CNAME already taken, what should I do?

A: Ask github for help! They are very nice.Go to see more [detail](https://help.github.com/en/articles/troubleshooting-custom-domains#cname-already-taken).

## 参考
1. https://docs.github.com/cn/pages/configuring-a-custom-domain-for-your-github-pages-site