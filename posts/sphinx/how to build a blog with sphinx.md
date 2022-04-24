---
blogpost: true
date: March 2, 2022
tags: sphinx,blog
category: Tech
---

# How to build a blog with sphinx?

## Quick start
1. Clone the [Template Project](https://github.com/choldgraf/choldgraf.github.io)
    ```shell
     git clone https://github.com/choldgraf/choldgraf.github.io.git
    ```
2. Install nox.
    ```shell
     pip install -U nox
    ```
3. Run nox
    ```shell
     nox -s docs
    ```
this should install a Sphinx environment and build the site, putting the output files in _build/html.

## Make your website
The template project is a demo.The information is all about Chris Holdgraf, you should make it to yourself.

### index Menu
```text
{toctree}
:maxdepth: 2
:hidden:
about
projects
publications
talks
blog
```
Change
```text
{toctree}
:maxdepth: 2
:hidden:
about
blog
```


### About me
There are three files containing the personal informantion. You should change the following files：
```text
index.md  
about.md  
_templates/hello.html
```
also you shuold replace the following images:
```text
_static/favicon.ico
_static/profile.jpg
_static/profile_bw.png
```
delete or replace the two files: _static/works.bib and cv.pdf    

### Social network

### Other catalog

### Sidebars
conf.py
```text
html_sidebars = {
    "index": ["hello.html"],
    "about": ["hello.html"],
    #"publications": ["hello.html"],
    #"projects": ["hello.html"],
    #"talks": ["hello.html"],
    "posts/**": ['postcard.html', 'recentposts.html', 'archives.html','categories.html'],
    "blog": ['tagcloud.html', 'archives.html','categories.html'],
    "blog/**": ['postcard.html', 'recentposts.html', 'archives.html','categories.html']
}
```

### Default conf
conf.py
```text
blog_default_author='ypy'
blog_default_language='English'
```


### Write your blog post
```text
---
blogpost: true
date: Oct 10, 2020
author: Nabil Freij
location: World
category: Manual
language: English
---
```
This project use sphinx extention ABlog to make blogs.Learn more about [ABlog](https://ablog.readthedocs.io/en/latest/). 


## giscus.app

## Manager your data
sync your data

https://ablog.readthedocs.io/en/latest/manual/notebook_support/



## Publish your website

https://www.sphinx-doc.org/en/master/tutorial/deploying.html#id5  

## Others
1. How to handle the image location?
> Just put the images in the same catalog with markdown files.

2. Image name cann't have any white space.For example, 'im a image.jpg' is not correct.You should name it 'im_a_image.jpg' .


## Ad
https://www.ethicalads.io/publishers/?ref=rtd-sidebar-join

## 附件如何处理？
https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#referencing-downloadable-files

here is a pdf file :download:`pdf <doc/mypdf.pdf>`

.. image:: doc/mypdf.pdf

## Reference
1. [ABlog manual](https://ablog.readthedocs.io/en/latest/manual)
2. 
