# 用sphinx生成文档

## sys.path 路径


当conf.py，make.bat等sphinx文件和代码分别位于不同的目录中时。（为了使repo结构清晰，往往conf.py和code分置不同目录）。  
此时需要在conf.py开头插入src的目录路径，使sphinx能够找到代码。
```
import os
import sys
__dir__ = os.path.dirname(os.path.abspath(__file__))
__pkg__ = os.path.dirname(__dir__)
sys.path.insert(0, __pkg__)
sys.path.insert(0, os.path.join(__pkg__,"./src"))
```


## extensions 插件

在conf.py中,选择需要应用的插件。
```
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.coverage',
    'sphinx.ext.viewcode',
]
```

- __autodoc__：根据注释自动生成文档。可以用autoclass, automenber等关键字根据class中的所有函数的注释生成文档。


- __viewcode__: 在生成文档每个函数右侧插入```[viewcode]``` ，点击可以跳转到对应代码，方便查看。



 

## Latex encode 中文编码问题
当代码注释中包含中文时，除了在*.py开头声明：   
    ```# -*- coding: utf-8 -*-```
    
还需要在conf.py的开头添加以下代码，使Latex可以生成中文文档。
```
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
if on_rtd:
    latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    'preamble': r'''
    \hypersetup{unicode=true}
    \usepackage{CJKutf8}
    \DeclareUnicodeCharacter{00A0}{\nobreakspace}
    \DeclareUnicodeCharacter{2203}{\ensuremath{\exists}}
    \DeclareUnicodeCharacter{2200}{\ensuremath{\forall}}
    \DeclareUnicodeCharacter{2286}{\ensuremath{\subseteq}}
    \DeclareUnicodeCharacter{2713}{x}
    \DeclareUnicodeCharacter{27FA}{\ensuremath{\Longleftrightarrow}}
    \DeclareUnicodeCharacter{221A}{\ensuremath{\sqrt{}}}
    \DeclareUnicodeCharacter{221B}{\ensuremath{\sqrt[3]{}}}
    \DeclareUnicodeCharacter{2295}{\ensuremath{\oplus}}
    \DeclareUnicodeCharacter{2297}{\ensuremath{\otimes}}
    \begin{CJK}{UTF8}{gbsn}
    \AtEndDocument{\end{CJK}}
    ''',
    }
else:
    latex_elements = {
        'papersize' : 'a4paper',
        'utf8extra' : '',
        'inputenc'  : '',
        'babel'     : r'''\usepackage[english]{babel}''',
        'preamble' : r'''
        \usepackage{ctex}
        ''',
}
```


## theme 主题

本地默认的主题是白色的，可以注释掉```html_theme = 'alabaster'```，此后本地生成的html仍为白色，但是在readthedocs上会默认采用蓝白sphinx主题。



## Mock  解决模块依赖

- 某些module可能需要手动加载，无法填写在requirements.txt中实现自动安装。
- readthedocs在生成手册前检查依赖，import失败将无法生成文档。
- 为了解决以上矛盾，可以用Mock屏蔽某些库依赖。详见 => [**Mock**](http://read-the-docs.readthedocs.io/en/latest/faq.html#i-get-import-errors-on-libraries-that-depend-on-c-modules)
```
import sys
from unittest.mock import MagicMock

class Mock(MagicMock):
    @classmethod
    def __getattr__(cls, name):
            return Mock()

MOCK_MODULES = ['pygtk', 'gtk', 'gobject', 'argparse', 'numpy', 'pandas']
sys.modules.update((mod_name, Mock()) for mod_name in MOCK_MODULES)
```

以上这段代码mock掉pygtk等模块，这样即使 代码中有```import pygtk``` && 远程主机中没有安装pygtk，文档仍然可以生成。 

> 举个例子，cv2就需要mock。



# pbr
pbr是python的发布工具，结合Travis CI，设置好库的.travis.yml就可以实现代码提交触发库的自动发布到pypi。

