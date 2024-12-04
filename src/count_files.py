import os

# Define the input and output directories
input_dir = '/data/input'
output_dir = '/data/output'
output_file = os.path.join(output_dir, 'result.txt')

# Count the number of files in the input directory
print(f'Counting the number of files in the input directory: {input_dir}')
file_count = len([name for name in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, name))])
print(f'Number of files in the input directory: {file_count}')

# Write the result to the output file
print(f'Writing the result to the output file: {output_file}')
with open(output_file, 'w') as f:
    f.write(f'{file_count}\n')