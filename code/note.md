##### CondaError: Run 'conda init' before 'conda activate'

```shell
$ conda activate ML
CondaError: Run 'conda init' before 'conda activate'

$ source activate
(base) 

$ conda activate ML
(ML) 
```

好像是`windows`上的问题，使用`activate`之前要`source activate`一次

##### 导入matplotlib时报DLL load fail的错误

```shell
from . import _imaging as core
ImportError: DLL load failed while importing _imaging: The specified module could not be found
```

* `pillow`版本问题，重新安装更低版本的`pillow`:

```shell
conda uninstall pillow
conda install pillow==8.0.0
```

