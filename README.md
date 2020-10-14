# 实验室的图片上传展示项目
第一个 Django 项目，学长和同学给了个前端模板和 Django 项目的模板然后边学边改。

# 安装

1. 按照个人的习惯将项目导入 pycharm 中。
2. environment.yml 是该项目导出的 conda 环境。所以在 pycharm 中的命令行运行 

```python
conda env create -f environment.yml
```

等待时间应该比较长，毕竟要下载相关的第三方包，耐心等待即可。

3. 将 settings.py 中数据库的名称用户密码更改为自己的。

# 运行
0. 确保 mysql8.0 服务启动并创建该数据库。
1. 导入的环境名为：myDjangoEnv，所以进入到环境中:

```python
activate  myDjangoEnv` 

```

2. 在数据库中创建表:

```python
python manage.py migrate
```

3. 启动服务:
```python
python manage.py runserver
```

4. 浏览器 `127.0.0.1:8000` 访问

# 相关文章：

[第一次Django实战](https://mikasalee.github.io/2020/10/07/FirstDjangoDemo/)

# 日志：
2020-10-14：第一阶段任务完成：图片上传功能基本实现，接下来等待前端的同学把前端写完之后再次修改 view 层和 model层。
