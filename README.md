# kudeki-chain
kudeki-chain inspired by https://github.com/dj-shin/gitchain

## Merging pull request without merge commit
```bash
git checkout -b jh05013-master master
git pull https://github.com/jh05013/kudeki-chain.git master
git checkout master
git merge --ff-only jh05013-master # not --no-ff
git push origin master
```
Refer to https://shinglyu.com/web/2018/03/25/merge-pull-requests-without-merge-commits.html
z
ㅊ
