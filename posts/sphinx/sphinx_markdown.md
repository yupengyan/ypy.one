---
blogpost: true
date: March 2, 2022
tags: sprinx,markdown
category: Tech
language: Chinese
---

## Sphinx对Markdown文件的支持

Sphinx可以通过 **[MyST-Parser](https://myst-parser.readthedocs.io/en/latest/)** 支持基础功能的Markdown文档。

## 配置步骤
1. 安装  
    ```shell
    pip install --upgrade myst-parser
    ```

2. 配置extensions  
    在conf.py的extensions部分加入如下内容：
    ```text
    extensions = ['myst_parser']
    ```

3. 配置后缀  
    在conf.py中加入以下内容：
    ```text
    source_suffix = {
        '.rst': 'restructuredtext',
        '.txt': 'markdown',
        '.md': 'markdown',
    }
    ```

## 测试
```shell
poetry run sphinx-build -b html documents_source/blog docs/build/html/blog

```
在相应目录下，出现相应的文档，证明安装并配置成功！


## 参考
*   [在sphinx中使用Markdown](https://www.sphinx-doc.org/en/master/usage/markdown.html)
*   [Markdown语法](https://markdown.com.cn/)  

