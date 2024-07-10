# SkillTree
The SkillTree project is a learning plateform where the site admin
can create, update and delete courses and assign questions to each course.
Courses can be accessed by regular users after account creation.

## Repo structure
This repository has the following branches:
- dev: where the main development process is done. Developpers should
only push their code to this branch
- stage: this branch is for testing purposes. A TravisCI process
autonomously deploy the app to the staging server where tests
will be executed.
- master: after the tests in the stage branch are successfully met.
The stage branch gets pulled to the master branch where a TravisCI process
will deploy the app to the production server.
