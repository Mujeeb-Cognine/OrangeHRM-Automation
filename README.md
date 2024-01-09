# OrangeHRM-Automation
## Follow the Steps before using this project automation.
1) Make sure you have installed all and imported all the modules and packages.
2) After cloning the project from GetFromVCS in PYCharm, set the bearer token in the env variables by following the steps below.
The process for setting environment variables varies depending on your operating system. Here are instructions for some common operating systems:

### Windows:
##### Using System Properties:
1) Right-click on the Computer icon and select "Properties."
2) Click on "Advanced system settings" on the left. 
3) In the System Properties window, click the "Environment Variables" button. 
4) In the Environment Variables window, under the "User variables" or "System variables" section, click "New."
5) Enter the variable name (e.g., ORANGEHRM_BEARER_TOKEN) and its value (your actual bearer token). 
6) Click "OK" to save.

##### Using Command Prompt:
1) Open a Command Prompt. 
2) Use the following command to set the environment variable temporarily for that session:

set ORANGEHRM_BEARER_TOKEN=your_actual_bearer_token_here
##### To set it permanently, you can use the setx command:
setx ORANGEHRM_BEARER_TOKEN "your_actual_bearer_token_here"

**Note**: Keep in mind that you might need to restart any applications that rely on this environment variable for the change to take effect.

### macOS and Linux:
#### In Terminal:
1) Open a terminal window. 
2) Use the following command to set the environment variable temporarily for that session: 

export ORANGEHRM_BEARER_TOKEN="your_actual_bearer_token_here"
To set it permanently for the user, add the export command to the shell profile file (e.g., ~/.bashrc, ~/.bash_profile, ~/.zshrc).
echo 'export ORANGEHRM_BEARER_TOKEN="your_actual_bearer_token_here"' >> ~/.bashrc

**Note:** Don't forget to restart the terminal or run source ~/.bashrc (or the appropriate file) to apply the changes. 

These are general guidelines, and the exact steps may vary slightly based on your system configuration. Always refer to your operating system's documentation or community resources for more detailed instructions.