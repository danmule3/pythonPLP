def read_and_modify_file(input_filename, output_filename):  
    try:  
        # Attempt to open and read the input file  
        with open(input_filename, 'r') as infile:  
            contents = infile.read()  
        
        # Modify the contents (for example, converting to uppercase)  
        modified_contents = contents.upper()  # Modify according to your requirements  

        # Write the modified contents to the output file  
        with open(output_filename, 'w') as outfile:  
            outfile.write(modified_contents)  

        print(f"Successfully modified and wrote to {output_filename}")  

    except FileNotFoundError:  
        print(f"Error: The file '{input_filename}' does not exist.")  
    except PermissionError:  
        print(f"Error: You do not have permission to read '{input_filename}'.")  
    except Exception as e:  
        print(f"An error occurred: {e}")  

def main():  
    # Ask the user for the input filename  
    input_filename = input("Please enter the filename to read: ")  
    output_filename = input("Please enter the filename to write to: ")  
    
    read_and_modify_file(input_filename, output_filename)  

if __name__ == "__main__":  
    main()