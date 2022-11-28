# soccer-player-fastapi-1

The following is my first api project. The purpose of this project is to enable users to create, read, update, and delete soccer players.


Users will be able to give players a name, age, nationality, and overall rating.

## Instructions on how to run the code

In the terminal, run the following command:
```aidl
git clone https://github.com/jcxsanchz/soccer-player-api-project.git
```
then, cd into soccer-player-api-project:
```aidl
cd soccer-player-api-project
```
create and activate a virtual environment within your IDE with the following commands:
```aidl
python3 -m venv venv
. venv/bin/activate
```
Install the dependencies in the requirements.txt file:
```aidl
pip install -r requirements.txt
```
Once the dependencies have been installed, the project will now be ready to run with the following command:
```aidl
uvicorn main:api
