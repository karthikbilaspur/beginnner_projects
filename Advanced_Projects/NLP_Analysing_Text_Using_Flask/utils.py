def save_results(results, output_file):
    """
    Save results to file.

    Args:
        results (dict): Analysis results.
        output_file (str): Output file path.
    """
    with open(output_file, 'w') as f:
        f.write(str(results))

def load_text(input_file):
    """
    Load text from file.

    Args:
        input_file (str): Input file path.

    Returns:
        str: Text content.
    """
    with open(input_file, 'r') as f:
        text = f.read()
    return text