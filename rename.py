#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import sys

def rename(location, separators):
    skip_all_input = False
    rename_count = 0
    for root, _, files in os.walk(location):
        for file in files:
            new_name = file
            need_rename = False
            for separator in separators:
                if(new_name.find(separator) != -1):
                    new_name = new_name.replace(separator, "")
                    need_rename = True
                    
            if need_rename == True: 
                old_path = os.sep.join([root, file])
                new_path = os.sep.join([root, new_name])
                if skip_all_input == True:
                    os.rename(old_path, new_path)
                    rename_count +=1
                    print("重命名成功，新的地址为：" + new_path)
                else:
                    user_rename_result = input("准备命名：\n" + old_path + " ->\n" + new_path + "\n同意请回车, 同意全部输入1并回车, 跳过请输入2并回车, 输入其他回车就退出\n")
                    if user_rename_result == "" or user_rename_result == "1":
                        if user_rename_result == "1":
                            skip_all_input = True
                        os.rename(old_path, new_path)
                        rename_count +=1
                        print("重命名成功，新的地址为：" + new_path)
                    elif user_rename_result == "2":
                        continue
                    else:
                        return
    print("已经处理完成重命名个数：" + str(rename_count))

                

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    rename_location = []
    separators = ["蠔"]
    

    if len(rename_location) == 0:
        input_location = input("如果是执行文件所在目录, 请直接回车。\n如果想输入其他地址,请输入处理地址后, 按enter \n")
        if len(input_location) != 0:
            rename_location.append(input_location)
        
    if len(rename_location) == 0:
        rename_location.append(os.path.dirname(sys.executable))
        
    print("准备处理地址为：", rename_location)
    continue_result = input("如果想继续请按回车，如果不想继续请按其他键结束程序。\n")
    
    if continue_result == '':
        for location in rename_location:
            rename(location, separators)
    print("处理已经完成, 随意按键推出")
    input()


        
        
        
