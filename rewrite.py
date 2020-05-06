# Read file
def read_file(filename):
    with open(filename, 'r', encoding='utf-8-sig') as f:
        lines = []
        for line in f:
            lines.append(line.strip())
    return lines


# Convert the format
def convert(lines):
    converters = []
    person = None  # Prevent from system crash if no specific value
    for line in lines:
        if line == 'Allen':
            person = 'Allen'
            continue  # Next loop
        elif line == 'Tom':
            person = 'Tom'
            continue  # Next loop
        else:
            converters.append(person + ': ' + line)
    for converter in converters:
        print(converter)
    return converters


# Write the new file to existing one
def write_file(filename, lines):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')


# Create main function
def main():
    lines = read_file('input.txt')
    lines = convert(lines)
    write_file('output.txt', lines)


main()
