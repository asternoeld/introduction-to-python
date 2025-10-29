def read_file(file_name, file_encoding):
    ''' reads file using the appropriate encoding and returns list of rows'''
    with open(file_name, "r", encoding=file_encoding) as f:
        lines = f.readlines()
    return lines

def filter_lines(L, sep, number_sep):
    '''
    Filter only elements of L that contains number_sep times the separator 'sep'.
    Each filtered element of L is represented as a list of strings, the strings separated by 'sep'
    All list of strings have the same length (number_sep+1)
    The output is the list with just the filtered lists of strings
    '''
    newL = []
    for line in L:
        # Remove trailing newline only for counting and splitting reliably:
        raw = line.rstrip("\n\r")
        # Count occurrences of separator
        if raw.count(sep) == number_sep:
            # Split and strip whitespace from each cell
            row = [cell.strip() for cell in raw.split(sep)]
            newL.append(row)
    return newL

def write_to_csv(L, output_file, sep):
    '''writes each element of L as a line in the output file'''
    # Use utf-8 for output to be broadly compatible; explicit newline to avoid blank lines on some systems
    with open(output_file, "w", encoding="utf-8", newline="") as f:
        for row in L:
           line = sep.join(row) + "\n"
           f.write(line)

def main():
    # constants
    input_file = 'INE_permanent_crops.csv'
    output_file = 'output.csv'
    sep = ';'
    number_sep = 6
    file_encoding = 'ISO-8859-1'
    # main steps
    L = read_file(input_file, file_encoding) # L is a list of the rows of the file
    L = filter_lines(L, sep, number_sep) # L is a list of lists, after we apply the separator
    write_to_csv(L, output_file, sep)

if __name__ == "__main__":
    main()

