import os
import shutil


def concatenate_files(source_directory, output_file):
    with open(output_file, 'w') as outfile:
        for root, _, files in os.walk(source_directory):
            files.sort()

            for filename in files:
                file_path = os.path.join(root, filename)

                if os.path.isfile(file_path):
                    with open(file_path, 'r', encoding='utf-8') as infile:
                        for line in infile:
                            stripped_line = line.strip()

                            if not stripped_line:
                                continue

                            if stripped_line.startswith('//&preserve'):
                                stripped_line = '//' + stripped_line[len('//&preserve'):].strip()
                            elif stripped_line.startswith('//'):
                                continue

                            outfile.write(stripped_line + '\n')


def main():
    source_directory = '.data/TopSkyMSAW'

    targets = [
        'OEJD/Plugins/TopSky/TopSkyMSAW.txt',
        'OEJD/Plugins/TopSky - ACC/TopSkyMSAW.txt',
    ]

    # Build once
    temp_file = 'TopSkyMSAW.tmp'
    concatenate_files(source_directory, temp_file)

    # Copy to both destinations
    for target in targets:
        os.makedirs(os.path.dirname(target), exist_ok=True)
        shutil.copyfile(temp_file, target)
        print(f'Built {target}')

    os.remove(temp_file)


if __name__ == '__main__':
    main()