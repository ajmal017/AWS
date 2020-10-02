## Git Branch
- A branch in Git is simply a lightweight movable pointer to one the commit. The default branch name in Git is master. As you start making commits, you’re given a master branch that points to the last commit you made. Every time you commit, the master branch pointer moves forward automatically.

### Creating a New Branch
This creates a new pointer to the same commit you’re currently on.
```
git branch <branchname>
```
- How does Git know what branch you’re currently on? It keeps a special pointer called HEAD.
- You can easily see this by running a simple git log command that shows you where the branch pointers are pointing. This option is called --decorate.
```
git log --oneline --decorate
```

### Switching Branches
```
git checkout <branchname>
```
- This moves HEAD to point to the testing branch.
- To show all of the branches, add --all to your git log command.

### Show all branching history
```
git log --oneline --decorate --graph --all
```

### Creating a new branch and switching to it at the same time
```
git checkout -b <newbranchname>
or 
git switch -c new-branch
or
git switch testing-branch
```
- Return to your previously checked out branch: git switch -.

### Basic Merge Conflicts
- Occasionally, this process doesn’t go smoothly. If you changed the same part of the same file differently in the two branches you’re merging, Git won’t be able to merge them cleanly. 
- If you want to see which files are unmerged at any point after a merge conflict, you can run git status:
- Git adds standard conflict-resolution markers to the files that have conflicts, so you can open them manually and resolve those conflicts

## Branch Management
- To see the last commit on each branch, you can run 
 ```
 git branch -v
 ```
 
 - To see which branches are already merged into the branch you’re on, you can run 
 ```
 git branch --merged
 ```
 
 - To see all the branches that contain work you haven’t yet merged in, you can run 
 ```
 git branch --no-merged
 ```
 
 - If you create new branch, make changes and commmit the changes without merging Git will fail
 ```
 git branch -d <branchname>
 error: The branch 'testing' is not fully merged.
 If you are sure you want to delete it, run 'git branch -D testing'.
 ```

 - Rename the branch locally with the git branch --move command:
```
git branch --move bad-branch-name corrected-branch-name
```

- You can delete the bad branch from the remote:
```
git push origin --delete bad-branch-name
```

- Rename your local master branch into main with the following command
```
git branch --move master main
```

- To let others see the new main branch, you need to push it to the remote. This makes the renamed branch available on the remote.
```
git push --set-upstream origin main
```










 
