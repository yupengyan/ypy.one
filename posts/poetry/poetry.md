## poetry
Poetry requires Python 2.7 or 3.5+. It is multi-platform and the goal is to make it work equally well on Windows, Linux and OSX.

 wget https://www.python.org/ftp/python/3.8.9/Python-3.8.9.tgz

pip3 install -U pip setuptools -i https://pypi.tuna.tsinghua.edu.cn/simple/ 
pip3 install poetry -i https://pypi.tuna.tsinghua.edu.cn/simple/ 


## 建立项目
```
poetry new project_name
```

## Initialising a pre-existing project
```shell
cd pre-existing-project
poetry init
```

## Using your virtual environment
By default, poetry creates a virtual environment in {cache-dir}/virtualenvs ({cache-dir}\virtualenvs on Windows).
You can change the cache-dir value by editing the poetry config. 
Additionally, you can use the virtualenvs.in-project configuration variable to create virtual environment within your project directory.

配置文件：Windows: C:\Users\<username>\AppData\Roaming\pypoetry
默认情况下，virtualenvs.in-project=None，虚拟环境不会安装在项目的根目录之下；如果将virtualenvs.in-project=true，虚拟环境会创建在项目根目录之下一个叫.venv的文件夹之下

If not set explicitly (default), poetry will use the virtualenv from the .venv directory when one is available. If set to false, poetry will ignore any existing .venv directory.

参考：https://python-poetry.org/docs/configuration/#virtualenvscreate

## Installing dependencies
```shell
poetry install
```

## 中国特色
```shell
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple/ poetry
```

pyproject.toml
```txt
[[tool.poetry.source]]
name="aliyun"
url="http://mirrors.aliyun.com/pypi/simple"
default=true
```

```poetry run ka
[tool.poetry.scripts]
ka = "p38_academic:keywords:keyword_analyze"
```

## 案例
```shell
Z:\dev>cd python-projects

Z:\dev\python-projects>poetry new p38_academic
Created package p38_academic in p38_academic

Z:\dev\python-projects>cd p38_academic

Z:\dev\python-projects\p38_academic>python -m venv .venv

poetry install
poetry run XXX



```
```shell
Z:\dev\python-projects>poetry config --list
cache-dir = "H:\\Users\\pengyan\\AppData\\Local\\pypoetry\\Cache"
experimental.new-installer = true
installer.parallel = true
virtualenvs.create = true
virtualenvs.in-project = true
virtualenvs.path = "{cache-dir}\\virtualenvs"  # H:\Users\pengyan\AppData\Local\pypoetry\Cache\virtualenvs
```

疑问：virtualenvs.create = true 了，为什么还要手工创建

