
# pbr
pbr是python的发布工具，结合Travis CI，设置好库的.travis.yml就可以实现代码提交触发库的自动发布到pypi。


### 用 github account 登录travis shell 
需要在本地安装一个travis shell,然后用github账号登录这个shell。
这里关键点是，登录的github账号，需要有对这个库的github repo有owner权限。否则在Travis CI的自动集成时会出现账号不一致：“ You must be identified to  ” 的出错信息：


```
Uploading robotframework-interfacelibrary-1.0.1.dev6.tar.gz

[================================] 137962/137962 - 00:00:00

HTTPError: 401 Client Error: You must be identified to edit package information for url: https://pypi.python.org/pypi

running upload_docs

creating build/docs
```



### setup pypi
接下来在travis shell中输入：  

```travis setup pypi```

然后按照提示，输入pypi的user和passwd。

接下来对话框会提示，是否加密passwd,只由这个repo触发pypi更新，只当commit带tag时，触发自动发布。

那么这里就有一个trick了，我们需要带tag和不带tag都触发，所以这里的deploy写两遍。




## More option
还有```- install``` , ```- script```等选项，用来安装和运行code test脚本。
