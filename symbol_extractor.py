import os, sys, json

__author__ = 'kmoonsun95@gmail.com'


def isTarget(ext):
    file_exts = ['.c', '.cc', '.cpp']
    for i in file_exts:
        if i == ext:
            return True
    return False


def init_path(root):
    files_path = list()
    print(root)
    for path, dir, files in os.walk('./' + root):
        print(path)
        for file_name in files:
            ext = os.path.splitext(file_name)[-1]
            if isTarget(ext):
                version = path.split('/')[1]
                files_path.append({
                    'path' : path + '/' + file_name,
                    'name' : file_name,
                    'version' : version
                    })

    return files_path, version
 

def ast(path):
    res = os.popen('clang -Xclang -ast-dump ' + path + ' | grep FunctionDecl').read()
    
    tmp1 = res.replace('036m', '\n').replace('[0m', '\n').split('\n')
    
    symbol_lst = list()
    for i in tmp1:
        if '36m ' in i:
            tmp2 = i.split(' ')[-1].replace('\x1b', '')
            symbol_lst.append(tmp2)


    return list(set(symbol_lst))


def main():
    output=list()

    for path in sys.argv[1:]:
        print(sys.argv[1:])
        files, version = init_path(path)

        template = { version : list() }
   
        for i in files: 
            res = ast(i['path'])
            template[version].append({'version': version, 'name' : i['name'],'symbols' : res})
        output.append(template)  

    with open('symbol.json', 'w') as f:
        json.dump(output, f, indent='\t')
      
 
if __name__ == '__main__':
    main()
