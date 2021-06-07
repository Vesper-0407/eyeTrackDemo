conda create -n eyeTrack python=3.6
conda activate eyeTrack
python -m pip install -U pip setuptools

### tobiiresearch应该默认安装的是1.8版本 所以代码和教程有点出入
pip install tobii_research numpy pandas

### 通过USB连接设备之后 find_all_eyetrackers()可以找出追踪系统

## http://developer.tobiipro.com/python/python-sdk-reference-guide.html 

### eye_images.py 提供了获取视野图像的方法
