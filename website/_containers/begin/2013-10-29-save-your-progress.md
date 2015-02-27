---
layout: post.html
title: "Save your progress - soft intro to git"
tags: [save, git, begin, rebase, squash]
---

This is an introduction on saving your code the way a developer does – through source control management. [git](http://git-scm.com/downloads) is what is used for these tutorials.

### What is git?

git is software. You use git to help manage your source code. While you still “Save” your code files the traditional way through your text editor, it is good practice (and used by professional engineers and hobbyists alike) to “save” your code with a source code management tool.

Instead of “Save” and “Save As”, you “commit” your code to your local repository. A repository (a.k.a. repo) can be thought of as the main, root directory for a project or a package.

A bit of context, git was initially designed and developed by Linus Torvalds for the development of Linux. Linus has a tendency to name things after himself (for instance, he’s the dude behind the Linux kernel); he named git after himself – [“git” is British slang for a stupid person](http://en.wikipedia.org/wiki/Git_(software)#History).

### Git and GitHub
**Do not confuse git and GitHub!***  git is software, [GitHub](http://github.com) is a company that offers remote hosting for your git repositories (rather than just having a local copy on your machine). [BitBucket](http://bitbucket.org) is also a company that offers remote hosting for your git repositories (as well as Mercurial repositories). Simply put, they offer a social aspect to coding – allowing you to connect to other developers.

To setup git locally on your machine, GitHub has a few great resources:

* [First time setup git](https://help.github.com/articles/set-up-git)
* [Create a repo with git](https://help.github.com/articles/create-a-repo)
* [Fork a repo with GitHub](https://help.github.com/articles/fork-a-repo)

Resources for using git:

* [A simple git guide](http://rogerdudler.github.com/git-guide/)
* [A visual git cheatsheet](http://www.ndpsoftware.com/git-cheatsheet.html#loc=workspace;)

### Your workflow with git

With git, users can do what’s called branching and merging. With a repo, you have a main, original branch called master. Off of master, you can make branches. Consider this to give you the ability to play around with code, break things, etc, while keeping the original/master safe. If you’re happy with what has been completed within a branch, you merge the branch into the master branch, and it becomes your new original.

It’s good to start off using git with good habits. Whenever you start something new, like as soon as you clone a repository, one good habit is to make a branch to merge in later when you’re satisfied with your progress.

When you are intermittently saving your progress on a branch, make a commit to your branch.  Commit your code regularly, whether when you’re done for the day, when you‘ve finished coding out one of the parts of the tutorial, before you answer the phone when someone calls you, etc. Rather than making one big “atomic” commit at big milestones (e.g. after the completion of one tutorial, an implementation of a feature), doing this makes it very easy to undo changes that you’ve made without losing big progress.

One awesome feature about git is that once you are ready to merge the branch into master, you can do what’s called squashing your commits into one big one. So, sure, you’ve made many commits - perhaps they’re many commits with one line of code or typos. This is a great way to group like commits together, hide embarrassing commits (maybe you were frustrated and your commit message contains a few swear words), or clean up the commit history. Squashing your commit history does not completely erase your commit history, but it gives you a cleaner log trail of your actions.

Here is a sample workflow of making a respository, branching, committing, squashing, then merging into master.

Within your terminal, we will initialize our repository and get the newcoder code base:

```bash
## make a Projects folder and move into that folder (change directories)
$ mkdir Projects && cd Projects
## initialize/create a new git repository
$ git init
## add a reference (a link) to my repository, naming it "upstream"
$ git remote add upstream https://github.com/econchick/new-coder.git
## pull in my repo (the master branch) from the above GitHub link into your
## repository
$ git pull upstream master
## check the status of your repository
$ git status
# On branch master
nothing to commit (working directory clean)
```

Now, let’s create a branch for our development:

```bash
## create a branch to start doing your work for the first tutorial, dataviz
$ git branch dataviz
## switch to the dataviz branch
$ git checkout dataviz
## go ahead and start coding and working.
```

When you are done for the day, interrupted, or want to save whatever small progress you’ve made, then commit it (save) your progress to your repo. We first have to add the file(s) that you’ve changed so that git knows to track them, then commit with a message for your reference:

```bash
## when you need to stop, or when you’ve made some changes you want
## to keep, you first add the files for git to track & commit:
$ git status
# On branch master
# Your branch is ahead of 'origin/master' by 4 commits.
#
# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#   (use "git checkout -- <file>..." to discard changes in working directory)
#
#   modified:   dataviz/tutorial_source/parse.py
#
no changes added to commit (use "git add" and/or "git commit -a")
$ git add dataviz/tutorial_source/parse.py
## then commit with a message:
$ git commit -m "part 1 of dataviz tutorial"
[master aa2a2e3] part 1 of dataviz tutorial
1 file changed, 1 insertion(+)
```

To check your commits, you can see git’s logs:

```bash
$ git log
commit aa2a2e301ef11ce27a799988354ea30b7aacb1c9
Author: Lynn Root <erin.lynn.root@gmail.com>
Date:   Thu Mar 14 10:48:25 2013 -0700

    part 1 of dataviz tutorial

commit f7629fe807a270f4bb67375cf7d3f93b0aab4381
Author: Lynn Root <erin.lynn.root@gmail.com>
Date:   Mon Mar 11 14:58:00 2013 -0700

    figured out the graph function

commit 77578d675dbf0d9f360dc1d3af399538715491c2
Author: Lynn Root <erin.lynn.root@gmail.com>
Date:   Mon Mar 11 14:48:53 2013 -0700

    fixing typo in my code
```

When you are ready to merge your progress into master (e.g. you’ve finished the whole tutorial), then squash commits via `git rebase` with the `-i` flag for interactive, and `HEAD~3` refers to the last three commits:

You first run this command:

```bash
$ git rebase -i HEAD~3
pick 77578d6 fixing typo in my code
pick f7629fe figured out the graph functions
pick aa2a2e3 part 1 of dataviz tutorial

# Rebase c59a19b..aa2a2e3 onto c59a19b
#
# Commands:
#  p, pick = use commit
#  r, reword = use commit, but edit the commit message
#  e, edit = use commit, but stop for amending
#  s, squash = use commit, but meld into previous commit
#  f, fixup = like "squash", but discard this commit's log message
#  x, exec = run command (the rest of the line) using shell
#
# These lines can be re-ordered; they are executed from top to bottom.
#
# If you remove a line here THAT COMMIT WILL BE LOST.
# However, if you remove everything, the rebase will be aborted.
```

This is a [vi](http://en.wikipedia.org/wiki/Vi) screen (a text editor within the terminal). To use vi, there are [special keys](http://www.howtogeek.com/115051/become-a-vi-master-by-learning-these-30-key-bindings/) to edit and move around. Press `i` to start editing, and move up and down with your keyboard’s arrow keys.

Notice the `pick` by each of the three commits that you’ve recently done. We will edit the latest two commits to say `squash`.  When done, press the following keys to save: `ESC` + `:` + `w` + `q`+ `Enter`:

```bash
pick 77578d6 fixing typo in my code
squash f7629fe figured out the graph functions
squash aa2a2e3 part 1 of dataviz tutorial

# Rebase c59a19b..aa2a2e3 onto c59a19b
#
# Commands:
#  p, pick = use commit
#  r, reword = use commit, but edit the commit message
#  e, edit = use commit, but stop for amending
#  s, squash = use commit, but meld into previous commit
#  f, fixup = like "squash", but discard this commit's log message
#  x, exec = run command (the rest of the line) using shell
#
# These lines can be re-ordered; they are executed from top to bottom.
#
# If you remove a line here THAT COMMIT WILL BE LOST.
# However, if you remove everything, the rebase will be aborted.
```

Now you will see a new vi screen to edit:

```bash
# This is a combination of 3 commits.
# The first commit's message is:
typo in my code

# This is the 2nd commit message:

figured out the graph functions

# This is the 3rd commit message:

part 1 of dataviz tutorial

# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
# Not currently on any branch.
# Changes to be committed:
#   (use "git reset HEAD <file>..." to unstage)
#
#   modified:   dataviz/tutorial_source/parse.py
#
```

You can now edit these messages to have one single message. This is essentially rewriting history, so let’s write a meaningful commit message. The lines starting with `#` will be ignored. When done editing, press `ESC` + `:` + `w` + `q` + `Enter`.

```bash
# This is a combination of 3 commits.
# The first commit's message is:
Completed the dataviz tutorial

# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
# Not currently on any branch.
# Changes to be committed:
#   (use "git reset HEAD <file>..." to unstage)
#
#   modified:   dataviz/tutorial_source/parse.py
#
```

Now you should see a message to the following;

```bash
Created commit 0fc4eea: Completed the dataviz tutorial
 1 files changed, 14 insertions(+), 13 deletions(-)
Successfully rebased and updated refs/heads/dataviz.
```

Ok now that we’ve squashed & rebased our many commits into one, we should merge our progress onto master:

```bash
$ git checkout master
$ git merge dataviz
```

You should now see the one squashed commit in the commit log:

```bash
$ git log
commit 90b4bdb388480529b1524b6afedbb0fab0fc4eea
Author: Lynn Root <erin.lynn.root@gmail.com>
Date:   Thu Mar 14 10:48:25 2013 -0700

    Completed the dataviz tutorial
```

However, you have not lost the commits you’ve squashed. To see all commits:

```bash
$ git reflog
0fc4eea HEAD@{0}: rebase -i (finish): returning to refs/heads/master
0fc4eea HEAD@{1}: rebase -i (squash): Completed the dataviz tutorial
aa2a2e3 HEAD@{2}: commit: part 1 of dataviz tutorial
f7629fe HEAD@{3}: commit: figured out the graph functions
77578d6 HEAD@{4}: commit: typo in my code
```

That’s it! You can find another quick tutorial on squashing git commits [here](http://gitready.com/advanced/2009/02/10/squashing-commits-with-rebase.html).



### Benefit to using GitHub or BitBucket

When you have code up on GitHub and/or BitBucket, not only do they implicitly provide backup to your code in case anything happens to your local machine, but it also is a resume for you as a developer.

As you work through these tutorials, I encourage you to use GitHub or BitBucket (or any other service that allows you to publicly share repositories) to “push” your code so others can see your progress. While I suggest you locally commit often and commit happily, only push code to GitHub/BitBucket when there is a good completion point (e.g. when you've finished a tutorial).

[git]: "http://en.wikipedia.org/wiki/Git_(software)#History"


<nav>
  <ul class="pager">
    <li class="previous"><a href="{{ get_url('/begin/setup-your-machine/') }}"><span aria-hidden="true">&larr;</span> Setup Your Machine</a></li>
    <li class="next"><a href="{{ get_url('/tutorials/') }}">Tutorial List <span aria-hidden="true">&rarr;</span></a></li>
  </ul>
</nav>
