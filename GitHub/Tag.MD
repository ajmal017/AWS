## Tags   

Tags are ref's that point to specific points in Git history. Tagging is generally used to capture a point in history that is used for a marked version release (i.e. v1.0.1). A tag is like a branch that doesn’t change. 

## Tags vs Branches  
Both tags and branches point to a commit, they are thus aliases for a specific hash and will save you time by not requiring to type in a hash.
The difference between tags and branches are that a branch always points to the top of a development line and will change when a new commit is pushed whereas a tag will not change. Thus tags are more useful to "tag" a specific version and the tag will then always stay on that version and usually not be changed.

- Git supports two different types of tags, annotated and lightweight tags

- A best practice is to consider Annotated tags as public, and Lightweight tags as private.

### Annotated Tags

 - Annotated tags store extra meta data such as: the tagger name, email, and date. This is important data for a public release
 
 - Additionally, for security, annotated tags can be signed and verified with GNU Privacy Guard (GPG). 
 
 Executing this command will create a new annotated tag with message
 ```
 git tag -m <msg> <tagname>
 ```
- annotated tags point to a tag object in the object database.
```
git tag -as -m msg annot
cat .git/refs/tags/annot
```
contains the SHA of the annotated tag object:
```
c1d7720e99f9dd1d1c8aee625fd6ce09b3a81fef
```
and then we can get its content with:
```
git cat-file -p c1d7720e99f9dd1d1c8aee625fd6ce09b3a81fef
```
sample output:
```
object 4284c41353e51a07e4ed4192ad2e9eaada9c059f
type commit
tag annot
tagger FirstName LastName <your@mail.com> 1411478848 +0200

msg
-----BEGIN PGP SIGNATURE-----
Version: GnuPG v1.4.11 (GNU/Linux)

<YOUR PGP SIGNATURE>
-----END PGP SIGNAT
```
And this is how it contains extra metadata. As we can see from the output, the metadata fields are:

 ### Lightweight Tags
 
  - A lightweight tag is similar to a branch; it’s just a pointer to a specific commit.
```
git tag <tagname>
```

### Display Tag object
```
git show <tagname>
```


### Listing Tags
```
git tag
```

### List Existing Tags with wildcards

```
git tag -l *-rc*
```

### Tagging Old Commits
```
git tag -a v1.2 <commitSHA>
```
### ReTagging/Replacing Old Tags or Tagging Later
```
git tag -a -f v1.4 <commitSHA>
```

### Sharing: Pushing Tags to Remote
By default, the git push command doesn’t transfer tags to remote servers. You will have to explicitly push tags to a shared server after you have created them. This process is just like sharing remote branches — you can run git push origin <tagname>.
```
git push origin v1.4
```

### Checking Out Tags
This puts the repo in a detached HEAD state. This means any changes made will not update the tag. They will create a new detached commit. This new detached commit will not be part of any branch and will only be reachable directly by the commits SHA hash. Therefore it is a best practice to create a new branch anytime you're making changes in a detached HEAD state.
```
git checkout v1.4 
```
Thus, if you need to make changes — say you’re fixing a bug on an older version, for instance — you will generally want to create a branch:
```
git checkout -b version2 v2.0.0
```


### Deleting a Tag
```
git tag -d <tagname>
```

### Deleting a tag from your remote server
```
git push origin :refs/tags/v2.4-lightweight
or
git push origin --delete v2.4-lightweight
```

## Notes
-  A tag annotation is not a commit message. You can't see it with git-log(1); you need to use git-show(1)
- Push annotated tags, keep lightweight local
- both lightweight and annotated tags are a file under .git/refs/tags that contains a SHA-1
- annotated tags point to a tag object in the object database.
- Determine if a tag is annotated:
  ```
  git cat-file -t tag

  ```
- If knowing who tagged what and when is relevant for you, then use annotated tags. If you just want to tag a specific point in your development, no matter who and when did that, then lightweight tags are good enough.
- git push --follow-tags will only push annotated tags
- git describe without command line options only sees annotated tags
- Using the git push command won’t push the tags you’ve created; you must explicitly push each tag after they’ve been created.
- To push multiple tags, you can use the --tags option to the push command.
- Tagger name and Commit Author name can be different

