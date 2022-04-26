基于sphinx的文档管理
=======
Creating the documentation layout

sphinx-quickstart docs

or

poetry run sphinx-quickstart docs

Thanks to this bootstrapping step, you already have everything needed to render the documentation as HTML for the first time. To do that, run this command:


(.venv)$ sphinx-build -b html docs/source/ docs/build/html

And finally, open docs/build/html/index.html in your browser. You should see something like this:


sphinx-build -b html docs/source/ docs/build/html


poetry run sphinx-build -b html docs/source/ docs/build/html

poetry run sphinx-build -b html documents_source/blog docs/build/html/blog

参考：https://www.sphinx-doc.org/en/master/tutorial/getting-started.html#setting-up-your-project-and-development-environment
