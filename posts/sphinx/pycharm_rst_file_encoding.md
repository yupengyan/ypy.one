---
blogpost: true
date: March 2, 2022
author: yu pengyan
tags: rst,pycharm
category: Tech
language: English
---

# How to make rst file encoding correct in pycharm

## Steps
1. File -> Settings -> Editor -> Code Style -> File Encodings
2. Make Settings just like the pic below:  
![How to make rst file encoding correct in pycharm](pycharm_rst_file_encoding.png)
3. Help -> Edit Coustom VM Options, add the following option:
    ```text
    -Dfile.encoding=UTF-8
    ```
   eStructuredText use JAVA, so you have to add a VM option.
4. restart IDE.  



