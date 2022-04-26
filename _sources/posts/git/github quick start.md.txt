---
blogpost: true
date: March 2, 2022
tags: github
category: Tech
---
# Github quick start  

df

## Quick setup   
Get started by creating a new file or uploading an existing file. 
We recommend every repository include a README, LICENSE, and .gitignore.
 
1. or create a new repository on the command line
```cmd
echo "# ve3_scrapy" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/yupengyan/ve3_scrapy.git
git push -u origin master
```

2.  push an existing repository from the command line
```
cd existing_repo
git remote rename origin old-origin
git remote add origin https://github.com/yupengyan/ve3_scrapy.git
git push -u origin master
or 
git push -u origin --all
or 
git push -u origin --tags
```
 
## How to protect your private email
1. Go to [email setting page](https://github.com/settings/emails)  
2. Choose to: Keep my email address private, and you will see your noreply email address here , like ID+username@users.noreply.github.com    
3. Unchoose: Block command line pushes that expose my email    
4. Set your email in git clinet:   
    ```shell
    git config --global user.email "ID+username@users.noreply.github.com"
    ```

## Reference   
1. https://github.blog/2017-04-11-private-emails-now-more-private
2. https://help.github.com/en/articles/about-commit-email-addresses






