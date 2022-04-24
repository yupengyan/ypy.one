# coding=utf-8
'''
功能：在endnote元数据文件附上全文地址
'''
import os

# 获取e-study论文文件路径、名称
def get_all_files(pdf_dir):
    files=[]
    files_dic={} # 文件名：文件路径;可能有重名文件，路径会被后面的覆盖
    for dir in os.listdir(pdf_dir):
        path=pdf_dir+'/'+dir
        if os.path.exists(path):
            for file_name in os.listdir(path):
                file_and_path =path+'/'+file_name
                file_name_without_ext=os.path.splitext(file_name)[0]
                files_dic[file_name_without_ext]=file_and_path
    return files_dic



def endnote_dc_formatter(source_file,save_file,pdf_dir):
    pdf_files=get_all_files(pdf_dir) # 返回 dic ,文件名：文件路径; 使用文件名可以取得路径。
    #print(pdf_files)
    lines=[]
    lines_new = []
    with open(source_file,'r',encoding='utf-8') as f:
        for line in f.readlines():
            #print(line.index())
            lines.append(str(line))
    for line in lines:
        if line.startswith('%T '):
            title=line[3:]
            t = title[0:-1]
            print(t)
            if pdf_files.get(t):# 避免pdf_files[key],key不存在触发错误
                pdf_file_path=pdf_files[t]
                line=line+ '%> '+ pdf_file_path +'\n'
        lines_new.append(line)
    f=''.join(lines_new)
    with open(save_file,'w',encoding='utf-8') as new_file:
        new_file.write(f)


if __name__=='__main__':
    source_file='H:/Users/pengyan/Downloads/CNKI-20.txt'
    save_file='H:/Users/pengyan/Downloads/CNKI-20_new.txt'
    pdf_dir='G:/private src data/e-study/pengyansrc/Literature'
    endnote_dc_formatter(source_file,save_file,pdf_dir)

