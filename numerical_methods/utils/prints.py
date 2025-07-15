def print_table(headers, data, decimal_places=4):
    """
    Prints a formatted table to the console with aligned columns.
        - headers (list of str): List of column headers.
        - data (list of list): List of rows, where each row is a list of values corresponding to the headers.
        - decimal_places (int, optional): Number of decimal places to display for float values. Defaults to 4.

    The function automatically adjusts column widths based on the longest header and data entry in each column.
    Float values are formatted to the specified number of decimal places.
    """
    
    # Calculate column widths considering the longest header and the longest integer part in data
    widths = {}
    for i, header in enumerate(headers):
        max_data_width = max(
            len(f"{row[i]:.{decimal_places}f}") if isinstance(row[i], float) else len(str(row[i]))
            for row in data
        ) if data else 0
        header_width = len(header)
        widths[header] = max(header_width, max_data_width)

    # Prepare separator line
    sep_line = "+"
    for i, header in enumerate(headers):
        sep_line += "-" * (widths[header] + 2)
        sep_line += "+"

    # Print header row
    sep = "| "
    header_row = sep + " | ".join(f"{header:<{widths[header]}}" for header in headers) + " |"
    print(f"{sep_line}\n{header_row}\n{sep_line}")

    # Print data rows
    for row in data:
        row_str = sep + " | ".join(
            f"{row[i]:<{widths[headers[i]]}.{decimal_places}f}" if isinstance(row[i], float)
            else f"{str(row[i]):<{widths[headers[i]]}}"
            for i in range(len(headers))
        ) + " |"
        print(f"{row_str}\n{sep_line}")