import shutil

#shutil.copyfile(src, dst)

# 2nd option
#shutil.copy(src, dst)  # dst can be a folder; use shutil.copy2() to preserve timestamp

#shutil.copy2('/src/dir/file.ext', '/dst/dir/newname.ext') # complete target filename given
#shutil.copy2('/src/file.ext', '/dst/dir') # target filename is /dst/dir/file.ext
src='G:/dev/projects_py/p39_docs/documents_source/blog_source'
dst='G:/dev/projects_py/ypy.one/posts'
shutil.copytree(src, dst, dirs_exist_ok=True)