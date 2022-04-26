---
blogpost: true
date: March 2, 2022
author: yu pengyan
tags: sprinx,bootstrap
category: Tech
language: English
---

# sphinx bootstrap theme

### 安装
1. 安装依赖
    ```shell
     pip install sphinx_bootstrap_theme
    ```
2. 编辑conf.py配置
    ```shell
    # At the top.
    import sphinx_bootstrap_theme
    
    # ...
    
    # Activate the theme.
    html_theme = 'bootstrap'
    html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()    
    ```
3. 个性化配置  
   3.1 主题选项
      编辑conf.py，增加以下配置内容：
      ```shell
      # (Optional) Logo. Should be small enough to fit the navbar (ideally 24x24).
      # Path should be relative to the ``_static`` files directory.
      html_logo = "my_logo.png"
      
      # Theme options are theme-specific and customize the look and feel of a
      # theme further.
      html_theme_options = {
          # Navigation bar title. (Default: ``project`` value)
          'navbar_title': "Demo",
      
          # Tab name for entire site. (Default: "Site")
          'navbar_site_name': "Site",
      
          # A list of tuples containing pages or urls to link to.
          # Valid tuples should be in the following forms:
          #    (name, page)                 # a link to a page
          #    (name, "/aa/bb", 1)          # a link to an arbitrary relative url
          #    (name, "http://example.com", True) # arbitrary absolute url
          # Note the "1" or "True" value above as the third argument to indicate
          # an arbitrary url.
          'navbar_links': [
              ("Examples", "examples"),
              ("Link", "http://example.com", True),
          ],
      
          # Render the next and previous page links in navbar. (Default: true)
          'navbar_sidebarrel': True,
      
          # Render the current pages TOC in the navbar. (Default: true)
          'navbar_pagenav': True,
      
          # Tab name for the current pages TOC. (Default: "Page")
          'navbar_pagenav_name': "Page",
      
          # Global TOC depth for "site" navbar tab. (Default: 1)
          # Switching to -1 shows all levels.
          'globaltoc_depth': 2,
      
          # Include hidden TOCs in Site navbar?
          #
          # Note: If this is "false", you cannot have mixed ``:hidden:`` and
          # non-hidden ``toctree`` directives in the same page, or else the build
          # will break.
          #
          # Values: "true" (default) or "false"
          'globaltoc_includehidden': "true",
      
          # HTML navbar class (Default: "navbar") to attach to <div> element.
          # For black navbar, do "navbar navbar-inverse"
          'navbar_class': "navbar navbar-inverse",
      
          # Fix navigation bar to top of page?
          # Values: "true" (default) or "false"
          'navbar_fixed_top': "true",
      
          # Location of link to source.
          # Options are "nav" (default), "footer" or anything else to exclude.
          'source_link_position': "nav",
      
          # Bootswatch (http://bootswatch.com/) theme.
          #
          # Options are nothing (default) or the name of a valid theme
          # such as "cosmo" or "sandstone".
          #
          # The set of valid themes depend on the version of Bootstrap
          # that's used (the next config option).
          #
          # Currently, the supported themes are:
          # - Bootstrap 2: https://bootswatch.com/2
          # - Bootstrap 3: https://bootswatch.com/3
          'bootswatch_theme': "yeti",
      
          # Choose Bootstrap version.
          # Values: "3" (default) or "2" (in quotes)
          'bootstrap_version': "3",
      }
      ```

## 参考
*  [sphinx-bootstrap-theme](https://ryan-roemer.github.io/sphinx-bootstrap-theme/README.html#installation)