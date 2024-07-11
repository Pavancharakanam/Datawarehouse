import subprocess

def run_command(command):
    process = subprocess.run(command, shell=True, capture_output=True, text=True)
    if process.returncode != 0:
        print(f"Error: {process.stderr}")
    else:
        print(process.stdout)

run_command('git init')

# Step 2: Add remote repository (if not already added)
remote_url = 'https://github.com/Pavancharakanam/Datawarehouse/tree/1ff93646f3549c487020ddb4433e1e796098e29d/DEV'  
run_command(f'git remote add origin {remote_url}')

# Step 3: Add the file to the staging area
run_command('git add gitpush.py')

# Step 4: Commit the file
commit_message = 'file added successfully'  # Replace with your commit message
run_command(f'git commit -m "{commit_message}"')

# Step 5: Push the changes to the remote repository
run_command('git push origin main')  # Replace 'main' with your branch name if different
