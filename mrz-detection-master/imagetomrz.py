import os
import re
import subprocess

def ExtractData(filepath):
    base_workdir = os.getcwd()
    try:
        # Run the Node.js command with 'cwd' set to the target directory
        node_command = ["node", "run/getMrz.js", "--file", filepath]
        result = subprocess.run(node_command, cwd=base_workdir, check=True)
        # Print any error output if present
        if result.stderr:
            logging.exception("Error output:")
            logging.exception(result.stderr)
    except subprocess.CalledProcessError as e:
        logging.exception("Error running the command:", e)
    
    # Get the file name from the file_location variable
    file_name = os.path.basename(filepath)

    # Split the file name and extension
    file_name, _ = os.path.splitext(file_name)

    # Change the file extension to .png
    file_name = file_name + ".png"

    # Access the /out/crop subdirectory
    new_dir = os.path.join(os.path.dirname(filepath), "out", "crop")

    # Join the new directory with the new file name
    filepath = os.path.join(new_dir, file_name)
    
    try:
        # Run the Node.js command with 'cwd' set to the target directory
        node_command = ["node", "run/readMrz.js", "--file", filepath]
        result = subprocess.run(node_command, cwd=base_workdir, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        print("Error running the command:", e)

    result_stdout = result.stdout # Updating variable name prevents potential problems with "."
    
    # Find the index of the first occurrence of 'mrz:'
    start_mrz_index = result_stdout.find('mrz:')

    if start_mrz_index != -1:
        # Find the index of the first '[' after 'mrz:'
        start_bracket_index = result_stdout.find('[', start_mrz_index)

        # Find the index of the first ']' after 'mrz:'
        end_bracket_index = result_stdout.find(']', start_mrz_index)

        if start_bracket_index != -1 and end_bracket_index != -1:
            # Extract the substring between the first '[' and the first ']' after 'mrz:'
            result = result_stdout[start_bracket_index + 1: end_bracket_index]

        else:
            print("No matching brackets found after 'mrz:'")
    else:
        print("No 'mrz:' found in the text.")
    
    # Use regular expressions to remove the escape sequences for colors and leading/trailing whitespaces
    cleaned_result = re.sub(r'\x1b\[\d+m', '', result).strip()

    # Split the cleaned result into a list using splitlines() and then split by comma
    result_list = cleaned_result.split(',')

    # Clean up the elements by removing single quotes and extra spaces, and create a new list
    cleaned_list = [element.strip().strip("'") for element in result_list]
    return cleaned_list