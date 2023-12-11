file_names = ['1.txt', '2.txt', '3.txt']
files_content = []

for file_name in file_names:
    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.readlines()
        files_content.append((file_name, len(content), content))
files_content.sort(key=lambda x: x[1])

with open('result.txt', 'w', encoding='utf-8') as result_file:
    for file_info in files_content:
        result_file.write(f'{file_info[0]}\n{file_info[1]}\n')
        result_file.writelines(file_info[2])
        result_file.write('\n')