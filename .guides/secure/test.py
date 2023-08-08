import os

def main():
    script_name = "/home/codio/workspace/main.py"  # Student's script name
    output_files = ["resized_image.png", "filtered_image.png", "image_var.png", "image_created.png"]

    # Change directory to the workspace
    os.chdir("/home/codio/workspace")

    # Attempt to run the student's script
    print(f"Running {script_name}...")
    return_code = os.system(f"python3 {script_name}")

    if return_code != 0:
        print(f"{script_name} ran with errors.")
    else:
        print(f"{script_name} ran successfully.")

    # Check if output files are created and not empty
    for file_name in output_files:
        if os.path.exists(file_name):
            print(f"{file_name} exists.")
            
            if os.path.getsize(file_name) > 0:
                print(f"{file_name} is not empty.")
            else:
                print(f"{file_name} is empty.")
        else:
            print(f"{file_name} does not exist.")

if __name__ == "__main__":
    main()
