# face2face
Facing the past, embracing the future.
# steps
1. 创建一个包含 Python 解释器环境的虚拟环境文件夹，名称为face2face-env
```python3
python3 -m venv face2face-env
```
2. 激活虚拟环境
```bash
# linux
.face2face-env/bin/activate
# windows
face2face-en\Scripts\activate
```
```
激活虚拟环境后，无论操作系统和 Python 版本，都可以统一使用 python 和 pip 命令来调用当前虚拟环境内的 Python 和 pip 程序/二进制文件。此时执行 python 或 pip 命令指向的程序和激活脚本在同一个目录下，在 Windows 下所在目录为 env\Scripts\，Linux 和 macOS 下所在目录为 env/bin/。  
执行 deactivate 即可退出虚拟环境：  
(env) $ deactivate
$
```
3. 配置python下载源
```bash
mkdir ~/.pip && echo "[global]
index-url = http://mirrors.aliyun.com/pypi/simple
[install]
trusted-host = mirrors.aliyun.com" > ~/.pip/pip.conf
```
4. 安装flask
```bash
./face2face-env/bin/pip install flask 
```
