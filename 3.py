def Read(filelist):
    all_lines = []
    for filename in filelist:
        with open(filename, "r") as file:
            lines = file.readlines()
            all_lines.append((filename, len(lines), [line.strip() for line in lines]))
    return all_lines


def NewFile(filelist, output_file):
    file_info = Read(filelist)
    sorted_file_info = sorted(file_info, key=lambda x: x[1])

    with open(output_file, "w") as output:
        for filename, line_count, lines in sorted_file_info:
            output.write(f"{filename}\n")
            output.write(f"{line_count}\n")
            for i, line in enumerate(lines):
                output.write(f"Строка номер {i+1} фаил номер {filename[0]}\n")
            output.write("\n")


filelist = ["1.txt", "2.txt", "3.txt"]
NewFile(filelist, "result.txt")
