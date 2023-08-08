## Connecting to GitHub

In this lab, you are going to build a simple program and integrate Dall-E to it. In order to showcase this project for your portfolio, you are going to use GitHub. If you do not yet have an account, please [create one](https://github.com/) now. We are going to clone a repo that will contain the code for your Chatbot.

### Connecting GitHub and Codio

You need to [connect](https://docs.codio.com/common/develop/ide/editing/connect-github-codio.html#connect-codio-github) GitHub to your Codio account. This only needs to be done one time.

* In your Codio account, click on your username 
* Click on **Applications**

![Image showing Codio account bar. The word Application is highlighted](https://docs.codio.com/_images/GitHub1.png)

* Under GitHub, click on **Connect account**

![an image displaying the words connect account in blue and upload public key in gray](https://docs.codio.com/_images/Github2.png)

* You will be using an SSH connection, so you need to click on **Upload public key**

### Fork the Repo

* Go to the [Dall-E lab](https://github.com/codio-content/Dall-E_lab.git) repo. This repo is the starting point for your project.
* Click on the `Fork` button in the top-right corner.
* Click `Create fork` green button.
* Click the `Code` button.
* Copy the **SSH** information. It should look something like this:

```txt-hide-clipboard
git@github.com:<your_username>/Dall-E_lab.git
```

|||info
## Important
If you do not use the SSH information, you will have to provide your username and Personal Access Token (PAT) to GitHub each time you push or pull from the repository. See this [documentation](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) for setting up a PAT for your GitHub account.

|||

### In the Terminal

* Clone the repo. Your command should look something like this:

```bash-hide-clipboard
git clone git@github.com:<your_username>/Dall-E_lab.git
```

* You should see a `Dall-E_Lab` directory appear in the file tree.

On the last page, we'll show you how to push to GitHub.

You are now ready for the lab!