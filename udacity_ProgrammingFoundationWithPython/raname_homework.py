import os
def rename_files():
    #(1) 파일이름을 폴더에서 가져온다.
    file_list = os.listdir(r"/Users/dusskapark/Documents/workspace/python101/udacity_ProgrammingFoundationWithPython/please")
    saved_path = os.getcwd()
    print("사용 디렉토리는"+ saved_path)
    os.chdir(r"/Users/dusskapark/Documents/workspace/python101/udacity_ProgrammingFoundationWithPython/please")
    #디랙토리 변경 (확인용)
    saved_path = os.getcwd()
    print("변경된 디렉토리는"+ saved_path)

    #(2)for - loop 파일명을 모두 수정하자. 
    for file_name in file_list:
        print("Old Name - "+file_name)
        print("New Name - "+file_name.strip(".qwertyuiopasdfghjklzxcvbnm")+".jpg")
        #파이썬2.7의 경우 
        #os.rename(file_name, file_name.translate(None,"0123456789")) 
        ##string.translate()로 숫자를 삭제함.
        
        #파이썬3의 경우,
        os.rename(file_name, file_name.strip(".qwertyuiopasdfghjklzxcvbnm")+".jpg")
        
        
    os.chdir(saved_path)
         
rename_files()