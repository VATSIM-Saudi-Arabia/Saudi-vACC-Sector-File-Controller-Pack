import os

def concatenate_files(source_directory, output_file):
    with open(output_file, 'w') as outfile:
        for root, _, files in os.walk(source_directory):
            for filename in sorted(files):
                file_path = os.path.join(root, filename)
                if os.path.isfile(file_path):
                    with open(file_path, 'r') as infile:
                        for line in infile:
                            stripped_line = line.strip()
                            if stripped_line:
                                if stripped_line.startswith('//&preserve'):
                                    # Remove the //&preserve prefix but keep the // and the rest of the line
                                    stripped_line = '//' + stripped_line[len('//&preserve'):].strip()
                                elif stripped_line.startswith('//'):
                                    # Skip lines starting with // that don't start with //&preserve
                                    continue
                                outfile.write(stripped_line + '\n')  # Write the cleaned line

def main():
    base_dir = '.data/TopSkyMaps'
    targets = [
        ('TopSky Radar', 'OEJD/Plugins/TopSky - ACC/TopSkyMaps.txt'),
        ('TopSky', 'OEJD/Plugins/TopSky/TopSkyMaps.txt'),
    ]

    for source_subdir, target_file in targets:
        source_directory = os.path.join(base_dir, source_subdir)
        print(f'Building {target_file} from {source_directory}')
        
        # Ensure the output directory exists
        output_dir = os.path.dirname(target_file)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        concatenate_files(source_directory, target_file)
        print(f'{target_file} built successfully.')

if __name__ == '__main__':
    main()