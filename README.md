# read me

工作流程：
- 下载数据 wget -i ./dataLoad/result.txt -P ~/BC  
- 解压    ls  ~/BC/*.tar.gz | xargs -n1 tar xzvf
- 切割成小图    python3 cropImage.py
- 软连接到工作目录    ln -s ～/BC/BC/train ~/Documents/landsat/VOC2012; ln -s ～/BC/BC/val ~/Documents/landsat/VOC2012
- 训练模型    python3 landsat.py

训练好模型后，写论文：

    1. 用show_image.py 挑选表现优异的图像
    2. 用log/plotRect.py 从挑选出来0的图像中截取合适的方框
    3. cd doc; python img2tex.py 用doc/img2tex.py 生成tex文本